import getAuth
import userdata.header_data as header_data
import getServiceAreas
import time
import debug




def header_refresh():
    with open("userdata/token", "w") as t:
        print(getAuth.getAuthToken(),  end='', file=t)
    current_header()

def current_header():
    with open("userdata/token", "r") as t:
        token = t.read()
        header_data.headers['x-amz-access-token'] = token

def requestId_refresh():
    header_data.headers['X-Amzn-RequestId'] = getAuth.requestIdSelfSingleUse()

def manual_token():
        token = getAuth.manualTokenRefresh()
        header_data.headers['x-amz-access-token'] = token
        with open('userdata/token', 'w') as t:
            print(token, end='', file=t)

def test():
    lst = getServiceAreas.getEligibleServiceAreas()
    if None in lst:
        print('Token expired........', end='\r')
        time.sleep(1)
        raise Exception
    else:
        pass


def authCycle():
    try:
        print('Reading from file ...', end='\r')
        time.sleep(1)
        current_header()
        test()
    except:
        try:
            debug.request_print()
            header_refresh()
        except:
            debug.blocked_print()
            manual_token()