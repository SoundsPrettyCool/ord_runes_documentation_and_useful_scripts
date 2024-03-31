#!/usr/bin/env python3

import subprocess
import argparse
from utils import run_command_with_logging

BITCOIN_DATA_DIR = "/mnt/e/bitcoin/.bitcoin"
COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/.cookie"
CONFIG_DIR = "/mnt/e/bitcoin/.bitcoin/bitcoin.conf"
INDEX = "/mnt/e/bitcoin/index.redb"
PORT = "2222"
SIGNET_PORT = "8000"
parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
parser.add_argument("--index-sats", help="add -index-sats at the end of the script", action="store_true")
parser.add_argument("--index-runes", help="add -index-runes at the end of the script", action="store_true")
parser.add_argument("--server", help="add -server at the end of the script", action="store_true")
parser.add_argument('args', nargs=argparse.REMAINDER)  # pass all the arguments after the options

args = parser.parse_args()
if args.signet:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/signet/.cookie"
    PORT = SIGNET_PORT
    if args.index_sats:
        INDEX = "/mnt/e/bitcoin/index_signet_sats.redb"
    elif args.index_runes:
        INDEX = "/mnt/e/bitcoin/index_signet_runes.redb"
    else:
        INDEX = "/mnt/e/bitcoin/index_signet.redb"
elif args.index_sats:
    INDEX = "/mnt/e/bitcoin/index.redb"
elif args.index_runes:
    INDEX = "/mnt/e/bitcoin/index_runes.redb"
else:
    INDEX = "/mnt/e/bitcoin/index_no_index.redb"

command = f"../ord/target/release/ord --bitcoin-data-dir {BITCOIN_DATA_DIR} --cookie-file {COOKIE_FILE} --config-dir {CONFIG_DIR} --index {INDEX}"

if args.signet:
    command += " --signet"
if args.index_sats:
    command += " --index-sats"
if args.index_runes:
    command += " --index-runes"

if args.server:
    command += f" server --http-port {PORT}"
if args.args:
    command += ' ' + ' '.join(args.args)
run_command_with_logging("ord_server.log", command)
