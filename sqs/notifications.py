import boto3
import json
from notification_base import BaseNotification


class SMS(BaseNotification):
    def __init__(self, message):
        super().__init__()
        self.message = message
        print('this is sending message :', self.message)
        self.client = boto3.client('sns', region_name='us-east-1')

    def send(self):
        res = self.client.publish(
            PhoneNumber="+821042707227",
            Message=str(self.message)
        )
        return json.dumps(res)
