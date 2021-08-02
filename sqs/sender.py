import boto3
import os

QUEUE_NAME = os.environ.get('QUEUE_NAME', 'PocQueue')

client = boto3.client('sqs')

def handler(event, context):
    print(event, context)
