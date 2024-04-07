#!/usr/bin/env python3

import subprocess
import argparse
from utils import run_command_with_logging
parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
parser.add_argument("--regtest", help="add -regtest at the end of the script", action="store_true")
parser.add_argument("--rpcwallet", help="specify the wallet", default="")
parser.add_argument("--generate", help="generate n blocks", type=int, default=0)
parser.add_argument('args', nargs=argparse.REMAINDER)  # pass all the arguments after the options
args = parser.parse_args()

DATADIR="/mnt/e/bitcoin/.bitcoin"
CONF="/mnt/e/bitcoin/.bitcoin/bitcoin.conf"
COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/.cookie"

if args.signet:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/signet/.cookie"
if args.regtest:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/regtest/.cookie"

command = f"bitcoin-cli --datadir={DATADIR} --conf={CONF}  --rpccookiefile={COOKIE_FILE}"
if args.signet:
    command += " -signet"
elif args.regtest:
    command += " -regtest"
if args.rpcwallet:
    command += f" -rpcwallet={args.rpcwallet}"
if args.generate:
    command += f" -generate {args.generate}"
if args.args:
    command += ' ' + ' '.join(args.args)
run_command_with_logging("bitcoin_cli.log", command)
