import boto3
import os
import json

QUEUE_NAME = os.environ.get('QUEUE_NAME', 'PocQueue')
QUEUE_URL = os.environ.get('QUEUE_URL')

client = boto3.client('sqs')

def handler(event, context):
    print(event)
    print(QUEUE_URL)
    if event.get('body'):
        try:
            res = client.send_message(
                QueueUrl=QUEUE_URL,
                MessageBody=event.get('body')
            )
            print(res)
            return json.dumps(res)
        except Exception as e:
            print(e)
            return event
    else:
        print('there is no body in this request.')
        return event