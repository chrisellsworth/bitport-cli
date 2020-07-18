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
        if raw_json['status'] == 'success':
            return raw_json['data']
        elif raw_json['status'] == 'error':
            raise APIException(raw_json['errors'])
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


def post(path, data):
    response = requests.post(
        API_URL + path,
        data=data,
        headers=auth_headers())
    return parse_response(response)
