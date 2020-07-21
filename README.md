# bitport-cli

Command-line interface for [Bitport.io](https://bitport.io)

## Installation
`pip install bitport-cli`

## Setup
1. Visit https://bitport.io/get-access to get an access code
1. `bitport --auth [code]`

## Usage

```
usage: bitport [-h]
               (--auth code | --folder [folderCode] | --zip folderCode | --file fileCode | --me | --transfer torrent | --transfers [token] | --version)

Bitport.io command-line client

optional arguments:
  -h, --help            show this help message and exit
  --auth code           authenticate the client with a code from
                        https://bitport.io/get-access
  --folder [folderCode]
                        get folder info (default is root folder)
  --zip folderCode      get zip URL
  --file fileCode       get file info
  --me                  info about logged in user
  --transfer torrent    add a new torrent
  --transfers [token]   list of ongoing transfer(s) or a specific transfer
  --version             show program's version number and exit
```

## Notes
- The authentication token is stored in `~/.bitport.ini`

## Tips
- All output is JSON. Pipe output to something like [`jq`](https://stedolan.github.io/jq/) to further parse as desired. For example, to list all folders and their codes:
  - `bitport --folder | jq '.[0].folders[] | {name, code}'`
- Set this interface as the handler for `magnet` links in the `links` browser.
  - Add `magnet "/path/to/bitport --transfer \"%\"" 1` to `links.cfg`
