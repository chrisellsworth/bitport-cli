import requests

import json
import sys
import auth

API_URL = 'https://api.bitport.io/v2'


class APIException(Exception):
    def __init__(self, raw_json):
        self.json = raw_json
        super(APIException, self).__init__(json.dumps(raw_json))


def auth_headers():
    return {'Authorization': 'Bearer {}'.format(auth.token())}


def parse_response(response):
    try:
        raw_json = response.json()
        if 'status' in raw_json:
            if raw_json['status'] == 'success':
                return raw_json['data']
            elif raw_json['status'] == 'error':
                raise APIException(raw_json['errors'])
            else:
                return raw_json
        elif 'error' in raw_json:
            # oauth responses do not have a status key
            raise APIException(raw_json['error'])
        else:
            return raw_json
    except ValueError:
        return response.text


def print_json(raw_json):
    print(json.dumps(raw_json, indent=4))


def get(path, params={}):
    response = requests.get(
        API_URL + path,
        params=params,
        headers=auth_headers())
    return parse_response(response)


def post(path, data, authenticated=True):
    headers = {}
    if authenticated:
        headers = auth_headers()
    response = requests.post(
        API_URL + path,
        data=data,
        headers=headers)
    return parse_response(response)
