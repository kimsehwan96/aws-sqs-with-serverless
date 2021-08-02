import boto3
import os

QUEUE_NAME = os.environ.get('QUEUE_NAME', 'PocQueue')
QUEUE_URL = os.environ.get('QUEUE_URL')

client = boto3.client('sqs')

def handler(event, context):
    print(event)
    if event.get('body'):
        try:
            res = client.send_message(
                QueueUrl=QUEUE_URL,
                MessageBody=event.get('body')
            )
            print(res)
            return res
        except Exception as e:
            print(e)
            return "fail"
    else:
        print('there is no body in this request.')
        return "fail"