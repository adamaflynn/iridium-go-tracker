import string
import json
import datetime

import config
import lib

def handler(event, context):
    print event

    vessel_id = event.get('queryStringParameters', {}).get('vessel', None)

    if vessel_id not in config.PROPER_NAME:
        return {'statusCode': 400,
                'body': "Unknown vessel ID %s" % vessel_id}

    boat_name = config.PROPER_NAME[vessel_id]

    since_days = int(event.get('queryStringParameters', {}).get('since_days', 180))
    positions = lib.get_recent_positions(vessel_id, since_days=since_days)

    # make a list of positions in JSON
    polyline_list = []
    for position in positions:
        polyline_list.append([float(position['lat']), float(position['lon'])])
    position_json = json.dumps(polyline_list)

    if not positions:
        return {'statusCode': 500,
                'body': "No data for vessel ID %s" % vessel_id}

    current_position = positions[0]

    # return a nicely-formatted string of the position in DMS
    formatted_position = lib.format_position(current_position['lat'],
                                             current_position['lon'])

    last_report_time = datetime.datetime.fromtimestamp(current_position['most_recent_ts'])
    last_report_time_string = last_report_time.strftime("%b %d %Y %H:%M:%S UTC")

    template = string.Template(open('map.tpl').read())
    body = template.substitute(boat_name=boat_name,
                               position_json=position_json,
                               formatted_position=formatted_position,
                               last_report_time=last_report_time_string)

    return {"statusCode": 200,
            "headers": {
                "Content-Type": "text/html; charset=utf-8"
            },
            "body": body}
