import argparse
import requests
import json
import client
import auth
import base64


def print_json(raw_json):
    print(json.dumps(raw_json, indent=4))


def authenticate(code):
    response = requests.post(
        client.API_URL + "/oauth2/access-token",
        data={
            'client_id': auth.APPLICATION_ID,
            'client_secret': auth.SECRET,
            'grant_type': 'code',
            'code': code})
    json = response.json()
    access_token = json['access_token']
    auth.save_token(access_token)
    expires_in = json['expires_in']
    print("Authorized. Expires in {} seconds".format(expires_in))


def folders(folder_path):
    params = {}
    if folder_path != 'all':
        params = {'folderPath': base64.b64encode(folder_path.encode('ascii'))}
    print_json(client.get("/cloud/byPath", params))


def files(file_code):
    print_json(client.get("/files/{}".format(file_code)))


def me():
    print_json(client.get("/me"))


def transfer(torrent):
    print_json(client.post("/transfers", {'torrent': torrent}))


def transfers(token):
    if token == 'all':
        print_json(client.get("/transfers"))
    else:
        print_json(client.get("/transfers/{}".format(token)))