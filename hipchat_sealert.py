#!/usr/bin/python
import json
from urllib2 import Request, urlopen
import sys

message = sys.argv[1]

APITOKEN = ''
ROOMID = ''
ORG = ''

url = "https://{org}.hipchat.com/v2/room/{roomid}/notification".format(roomid=ROOMID, org=ORG)

headers = {
    "content-type": "application/json",
    "authorization" : "Bearer {apitoken}".format(apitoken=APITOKEN)
}

datajson = json.dumps({
    'message': message,
    'color': 'red',
    'message_format': 'text',
    'notify': False
    })

request = Request(url, headers=headers, data=datajson)
info = urlopen(request)
response = ''.join(info)
info.close()

