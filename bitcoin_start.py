#!/usr/bin/env python3

import argparse
from utils import run_command_with_logging
parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
parser.add_argument("--testnet", help="add -testnet at the end of the script", action="store_true")
parser.add_argument("--regtest", help="add -regtest at the end of the script", action="store_true")
parser.add_argument('args', nargs=argparse.REMAINDER)  # pass all the arguments after the options
args = parser.parse_args()

DATADIR="/mnt/c/bitcoin/.bitcoin"
CONF="/mnt/c/bitcoin/.bitcoin/bitcoin.conf"

command = f"../bitcoin-25.0/bin/bitcoind -datadir={DATADIR} -conf={CONF}"
if args.signet:
    command += " -signet"
elif args.testnet:
    command += " -testnet"
elif args.regtest:
    command += " -regtest"

if args.args:
    command += ' ' + ' '.join(args.args)
print(command)
run_command_with_logging("bitcoin_start.log", command)
