headers = {
    'x-amz-access-token': 'token',
    'x-flex-instance-id':  'instanceId',
    'X-Flex-Client-Time': 'time',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'User-Agent': 'AmazonWebView/Amazon Flex/0.0/iOS/15.2/iPhone',
    'X-Amzn-RequestId': 'requestid',
    'Connection': 'Keep-Alive',
}

del headers['X-Flex-Client-Time']