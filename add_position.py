import json
import boto3
import email
import re
import decimal

import lib
import config

LAT_LONG_RE = re.compile('Lat([+-][0-9.]+) Lon([+-][0-9.]+)')

def get_fake_email_content(event):
    return config.FAKE_EMAIL

def get_s3_email_content(event):
    s3 = boto3.resource('s3')
    email_object = s3.Object(event['Records']['bucket']['name'],
                             event['Records']['s3']['key'])

    email_content = email_object.get()['Body'].read()

    return email_content

def get_lat_long_from_email(body):
    match = LAT_LONG_RE.search(body)

    # return lat, long as Decimals
    return map(decimal.Decimal, match.group(1, 2))


def handler(event, context):
    email_raw_content = get_fake_email_content(event)

    parsed_email = email.message_from_string(email_raw_content)
    from_address = parsed_email['From']

    if from_address not in config.USER_MAP:
        return {"message": "From address %s is unknown" % from_address,
                "email_debug": parsed_email.items(),
                "email_content": email_raw_content,
                "event": event}

    # pull the user, lat, and long
    user = config.USER_MAP[from_address]
    lat, long = get_lat_long_from_email(parsed_email.get_payload())

    is_new = lib.add_position_to_dynamo(user, lat, long)

    return {
        "message": "Successfully added %s at %f, %f" % (user, lat, long),
        "is_new_position": is_new,
        "event": event
    }
