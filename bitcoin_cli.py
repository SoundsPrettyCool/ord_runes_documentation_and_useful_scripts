#!/usr/bin/env python3

import subprocess
import argparse
from utils import run_command_with_logging
parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
parser.add_argument("--rpcwallet", help="specify the wallet", default="")
parser.add_argument('args', nargs=argparse.REMAINDER)  # pass all the arguments after the options
args = parser.parse_args()

DATADIR="/mnt/e/bitcoin/.bitcoin"
CONF="/mnt/e/bitcoin/.bitcoin/bitcoin.conf"
COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/.cookie"

if args.signet:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/signet/.cookie"

command = f"bitcoin-cli --datadir={DATADIR} --conf={CONF}  --rpccookiefile={COOKIE_FILE}"
if args.signet:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/signet/.cookie"
    command += " -signet"
if args.rpcwallet:
    command += f" -rpcwallet={args.rpcwallet}"
if args.args:
    command += ' ' + ' '.join(args.args)
run_command_with_logging("bitcoin_cli.log", command)