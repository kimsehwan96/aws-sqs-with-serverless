import boto3
from notification_base import BaseNotification


class SMS(BaseNotification):
    def __init__(self, message):
        super.__init__(self)
        self.message = message
        self.client = boto3.client('sms')

    def send(self):
        self.client.publish(
            PhoneNumber="+821042707227",
            Message=str(self.message)
        )
