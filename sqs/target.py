import boto3
from notifications import SMS

def handler(event, context):
    records = event.get('Records')
    if len(records) != 1:
        pass # 길이가 1이 아니라는건 중복 메시지가 들어왔다는 의미일듯
    else:
        sms = SMS(records.get('body'))
        res = sms.send()
        print(res)


# below is event's example.
"""
{'Records': [{'messageId': '37cb6046-e35e-4d32-b35c-a9886fc9887d',
              'receiptHandle': 'AQEBhOgLRh5s17eHdTr0ij+uGIy/tjgyfu3dyc0Ha+mB7e5F/Pi7TQo1ea3+qRTnDEvWlyJTcRN+iF/asxnOH2ptjq8h4P6i1ud22wnXD/kspOib8Dv3e3DgNQ3LrEgBoK2kMCRXpomWeK3g7UyPqHRhSRhCxzfTOyCnWUQKPTSeBJlOrO4jkGHSPEejxUozE9oNYsBeuILHGTFeVGc0cU4k1yuwqLjd9/L2eEI2jRTcDfYo+pzzvke6Idwvrhy3Xvfkeh4W0A7e/BAXqTzuQ5AkyabAH5VYL8mW+cdOo632rxOQiAJGHmKK8NM/psj+E7b7Hr5UkRfb0JEQnI1zdYw+9q75zdNtWpCuA2AT/X3KyvSrBmqhuy8TQX1X2oa5YBg1Rutz/WVqtRQDcWFLwnFyXg==',
              'body': 'Helo', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1627892199372',
                                             'SenderId': 'AROAZYR7D2FBP4HFJCVKS:sqs-poc-dev-sender',
                                             'ApproximateFirstReceiveTimestamp': '1627892199374'},
              'messageAttributes': {}, 'md5OfBody': '825bd435c12978e8492330c2a0d823db', 'eventSource': 'aws:sqs',
              'eventSourceARN': 'arn:aws:sqs:ap-northeast-2:671221010754:PocQueue', 'awsRegion': 'ap-northeast-2'}]}
"""