#!/usr/bin/env python

import argparse
import sys
import os.path
import client
import api


def main():
    parser = argparse.ArgumentParser(
        description='Bitport.io command-line client')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--auth',
        metavar='code',
        help='authenticate the client with a code from https://bitport.io/get-access')
    group.add_argument(
        '--folder',
        metavar='folderCode',
        nargs='?',
        const='byPath',
        help='get folder info (default is root folder)')
    group.add_argument(
        '--file',
        metavar='fileCode',
        help='get file info')
    group.add_argument(
        '--me',
        action='store_true',
        help='info about logged in user')
    group.add_argument(
        '--transfer',
        metavar='torrent',
        help='add a new torrent')
    group.add_argument(
        '--transfers',
        metavar='token',
        const='all',
        nargs='?',
        help='list of ongoing transfer(s) or a specific transfer')
    group.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0')

    try:
        args = parser.parse_args()
        if args.auth:
            api.authenticate(args.auth)
        elif args.folder:
            api.folders(args.folder)
        elif args.file:
            api.files(args.file)
        elif args.me:
            api.me()
        elif args.transfer:
            api.transfer(args.transfer)
        elif args.transfers:
            api.transfers(args.transfers)
    except client.APIException as exc:
        api.print_json(exc.json)
        sys.exit(1)
    except Exception as exc:
        print(exc.message)
        sys.exit(1)


if __name__ == "__main__":
    main()
