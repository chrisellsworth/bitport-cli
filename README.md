# bitport-cli

Command-line interface for [Bitport.io](https://bitport.io)

## Installation
`pip install bitport-cli`

## Setup
1. Visit https://bitport.io/get-access to get an access code
1. `bitport --auth [code]`

## Usage
- `bitport --transfer [torrent]` - add a torrent
- `bitport --transfers` - list ongoing transfers
- `bitport --help` - show more options

## Notes
- The authentication token is stored in `~/.bitport.ini`

## Tips
- All output is JSON. Pipe output to something like [`jq`](https://stedolan.github.io/jq/) to further parse as desired.
- Set this interface as the handler for `magnet` links in the `links` browser.
  - Add `magnet "/path/to/bitport --transfer \"%\"" 1` to `links.cfg`
