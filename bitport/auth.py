import configparser
import os.path
import sys

APPLICATION_ID = 43764
SECRET = 'dipyhu21qu'
CONFIG_PATH = os.path.expanduser('~/.bitport.ini')


def save_token(token):
    config = configparser.ConfigParser()
    config['DEFAULT']['token'] = token
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)


def token_if_available():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config['DEFAULT']['token']


def token():
    try:
        return token_if_available()
    except KeyError:
        print("Not authorized. Did you run --auth?")
        sys.exit(1)
