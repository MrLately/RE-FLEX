import requests
from datetime import datetime
import getAuth
import debug
import userdata.header_data as header_data


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


def __getAmzDate() -> str:
    """
        Returns Amazon formatted timestamp as string
        """
    return datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

def test():
    requestId_refresh()
    header_data.headers["X-Amz-Date"] = __getAmzDate()
    lst = getAllServiceAreas()
    if "serviceAreaPoolList" in lst:
        pass
    else:
        raise

def getEligibleServiceAreas():
    try:
        current_header()
    except:
        try:
            debug.request_print()
            header_refresh()
        except:
            debug.blocked_print()
            manual_token()

    requestId_refresh()
    header_data.headers["X-Amz-Date"] = __getAmzDate()
    response = requests.get(
    "https://flex-capacity-na.amazon.com/eligibleServiceAreas",
    headers=header_data.headers)
    return response.json().get("serviceAreaIds")

def getAllServiceAreas():
    try:
        current_header()
    except:
        try:
            debug.request_print()
            header_refresh()
        except:
            debug.blocked_print()
            manual_token()

    requestId_refresh()

    header_data.headers["X-Amz-Date"] = __getAmzDate()

    serviceAreaPoolList = requests.get(
    "https://flex-capacity-na.amazon.com/getOfferFiltersOptions",
    headers=header_data.headers
    ).json().get("serviceAreaPoolList")
    with open("userdata/serviceAreaIds.py", "w") as s:
        print('stationlist = {', file=s)
        for serviceArea in serviceAreaPoolList:
            Name = serviceArea["serviceAreaName"]
            ID = serviceArea["serviceAreaId"]
            print('"{1}":"{0}",'.format(Name, ID), file=s)
        print('}', file=s)