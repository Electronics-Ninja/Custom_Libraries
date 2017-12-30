#!/usr/bin/env python

import requests
import sys
import json
import configparser

# from https://gist.github.com/bdclark/4bc8ed06643e077fa620

#config = configparser.ConfigParser()
#config.read("../../lib/customLibrary.cfg")
#hc_server = config.get("HipChat", "HIPCHAT_HOST")
#hc_api = config.get("HipChat", "HIPCHAT_API")

#hipchat_api = hc_api
#host = hc_server

def hipchat_notify(token, room, message, color='gray', notify=False, format='text', host=''):

    if len(message) > 10000:
        raise ValueError('Message too long')
    if format not in ['text', 'html']:
        raise ValueError("Invalid message format '{0}'".format(format))
    if color not in ['yellow', 'green', 'red', 'purple', 'gray', 'random']:
        raise ValueError("Invalid color {0}".format(color))
    if not isinstance(notify, bool):
        raise TypeError("Notify must be boolean")

    url = "https://{0}/v2/room/{1}/notification".format(host, room)
    headers = {'Content-type': 'application/json'}
    headers['Authorization'] = "Bearer " + token
    payload = {
        'message': message,
        'notify': notify,
        'message_format': format,
        'color': color
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    r.raise_for_status()


if __name__ == '__main__':
    try:
        hipchat_notify(hipchat_api, 'ThreatIntel', 'TEST TEST TEST')
    except Exception as e:
            msg = "[ERROR] HipChat notify failed: '{0}'".format(e)
            print(msg, file=sys.stderr)
            sys.exit(1)
