# -*- coding: utf-8 -*-

import boto3
from boto3.dynamodb.conditions import Key
import math
import time

_TABLE = None

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def decimal_degrees_to_dms(dd):
    dd = abs(dd)
    minutes, seconds = divmod(dd*3600,60)
    degrees, minutes = divmod(minutes,60)

    return degrees, minutes, seconds

def format_position(lat, long):
    d, m, s = decimal_degrees_to_dms(lat)
    formatted_string = '%dº %d\\\' %d\\" ' % (d, m, s)
    formatted_string += 'N' if lat > 0 else 'S'

    d, m, s = decimal_degrees_to_dms(long)
    formatted_string += ', %dº %d\\\' %d\\" ' % (d, m, s)
    formatted_string += 'E' if long > 0 else 'W'

    return formatted_string

def get_table():
    global _TABLE

    if _TABLE is None:
        dynamodb = boto3.resource('dynamodb')
        _TABLE = dynamodb.Table('tracker-points')

    return _TABLE

def get_recent_positions(vessel, count=None, since_days=180):
    table = get_table()

    kwargs = {
        'KeyConditionExpression': 'vessel = :vessel AND ts >= :ts',
        'ScanIndexForward': False,
        'ExpressionAttributeValues': {':vessel': vessel,
                                      ':ts': int(time.time()) - since_days * 86400},
        'ProjectionExpression': 'ts, most_recent_ts, lat, lon',
        'Select': 'SPECIFIC_ATTRIBUTES'
    }

    if count:
        kwargs['Limit'] = count

    results = table.query(**kwargs)

    return results['Items']


def add_position_to_dynamo(vessel, lat, long, ts=None, skip_last_position_check=False):
    if ts is None:
        ts = int(time.time())

    table = get_table()

    if not skip_last_position_check:
        # check the most recent position for the vessel
        position = get_recent_positions(vessel, count=1)

        # if there has been a position, and it's within 1km of the last position, just update the ts
        if position:
            position = position[0]

            distance_from_last = distance((lat, long),
                                          (position['lat'], position['lon']))

            if distance_from_last < 1:
                table.update_item(Key={'vessel': vessel,
                                       'ts': position['ts']},
                                  UpdateExpression='SET most_recent_ts = :ts',
                                  ExpressionAttributeValues={':ts': ts})
                return False

    # if we couldn't update the last position, we need to add a new one
    table.put_item(Item={
        'vessel': vessel,
        'lat': lat,
        'lon': long,
        'ts': ts,
        'most_recent_ts': ts
    })

    return True

def clear_vessel(vessel):
    table = get_table()

    positions = get_recent_positions(vessel, since_days=1000) # hack attack

    for position in positions:
        table.delete_item(Key={'vessel': vessel,
                               'ts': position['ts']})

    return len(positions)

