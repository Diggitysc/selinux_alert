#!/usr/bin/python
import json
import sys
from urllib2 import Request, urlopen
import ConfigParser

message = sys.argv[3]
config_location = '/home/{user}/hipchat.ini'.format(user=sys.argv[2])

config = ConfigParser.ConfigParser()
config.read(config_location)

USERID = config.get('hipchat', 'user')
APITOKEN = config.get('hipchat', 'api_token')
ORG = config.get('hipchat', 'org')

url = "https://{org}.hipchat.com/v2/user/{userid}/message".format(
    userid=USERID, org=ORG)

headers = {
    "content-type": "application/json",
    "authorization": "Bearer {apitoken}".format(apitoken=APITOKEN)
}

datajson = json.dumps({
    'message': message,
    'message_format': 'text',
    'notify': False
    })

request = Request(url, headers=headers, data=datajson)
info = urlopen(request)
response = ''.join(info)
info.close()
