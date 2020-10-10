import argparse
import requests
import json
import client
import auth


def print_json(raw_json):
    print(json.dumps(raw_json, indent=4))


def authenticate(code):
    response = client.post(
        "/oauth2/access-token",
        data={
            'client_id': auth.APPLICATION_ID,
            'client_secret': auth.SECRET,
            'grant_type': 'code',
            'code': code
        },
        authenticated=False)
    access_token = response['access_token']
    auth.save_token(access_token)
    expires_in = response['expires_in']
    print("Authorized. Expires in {} seconds".format(expires_in))


def folders(folder_code):
    print_json(client.get("/cloud/{}".format(folder_code)))


def zip(file_code):
    print(client.get_raw("/cloud/{}/download-as-zip".format(file_code)).headers['Location'])


def files(file_code):
    print_json(client.get("/files/{}".format(file_code)))


def me():
    print_json(client.get("/me"))


def transfer(torrent):
    print_json(client.post("/transfers", {'torrent': torrent}))


def delete_transfer(token):
    print_json(client.delete("/transfers/{}".format(token)))


def transfers(token):
    if token == 'all':
        print_json(client.get("/transfers"))
    else:
        print_json(client.get("/transfers/{}".format(token)))
