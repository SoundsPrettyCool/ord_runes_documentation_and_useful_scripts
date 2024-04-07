#!/usr/bin/env python3

import subprocess
import argparse
from utils import run_command_with_logging

BITCOIN_DATA_DIR = "/mnt/e/bitcoin/.bitcoin"
COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/.cookie"
CONFIG_DIR = "/mnt/e/bitcoin/.bitcoin/bitcoin.conf"
INDEX = "/mnt/e/bitcoin/index.redb"
PORT = "2222"
TEST_PORT = "8000"
SERVER_URL = f"http://localhost:{PORT}"
parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
parser.add_argument("--testnet", help="add -testnet at the end of the script", action="store_true")
parser.add_argument("--regtest", help="add -regtest at the end of the script", action="store_true")
parser.add_argument("--index-sats", help="add -index-sats at the end of the script", action="store_true")
parser.add_argument("--index-runes", help="add -index-runes at the end of the script", action="store_true")
parser.add_argument("--index-sats-and-runes", help="add -index-sats-and-runes at the end of the script", action="store_true")
parser.add_argument("--server", help="add -server at the end of the script", action="store_true")
parser.add_argument("--wallet", help="specify the wallet", action="store_true")
parser.add_argument("--batch", help="specify the batch", default=None)
parser.add_argument("--fee-rate", help="specify the fee-rate", default=None)
parser.add_argument("--inscribe", help="specify that you want to inscribe", action="store_true")
parser.add_argument("--mint", help="specify that you want to mint", action="store_true")
parser.add_argument("--rune", help="specify that you want to mint runes", default=None)
parser.add_argument('args', nargs=argparse.REMAINDER)  # pass all the arguments after the options

args = parser.parse_args()
if args.signet:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/signet/.cookie"
    PORT = TEST_PORT
    SERVER_URL = f"http://localhost:{TEST_PORT}"
    if args.index_sats:
        INDEX = "/mnt/e/bitcoin/index_signet_sats.redb"
    elif args.index_runes:
        INDEX = "/mnt/e/bitcoin/index_signet_runes.redb"
    else:
        INDEX = "/mnt/e/bitcoin/index_signet.redb"
elif args.testnet:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/testnet3/.cookie"
    PORT = TEST_PORT
    SERVER_URL = f"http://localhost:{TEST_PORT}"
    if args.index_sats:
        INDEX = "/mnt/e/bitcoin/index_testnet_sats.redb"
    elif args.index_runes:
        INDEX = "/mnt/e/bitcoin/index_testnet_runes.redb"
    else:
        INDEX = "/mnt/e/bitcoin/index_testnet.redb"
elif args.regtest:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/regtest/.cookie"
    PORT = TEST_PORT
    SERVER_URL = f"http://localhost:{TEST_PORT}"
    if args.index_sats:
        INDEX = "/mnt/e/bitcoin/index_regtest_sats.redb"
    elif args.index_runes:
        INDEX = "/mnt/e/bitcoin/index_regtest_runes.redb"
    else:
        INDEX = "/mnt/e/bitcoin/index_regtest.redb"
elif args.index_sats:
    INDEX = "/mnt/e/bitcoin/index.redb"
elif args.index_runes:
    INDEX = "/mnt/e/bitcoin/index_runes.redb"
elif args.index_sats_and_runes:
    INDEX = "/mnt/e/bitcoin/index-0.17-with.redb"
else:
    INDEX = "/mnt/e/bitcoin/index_no_index.redb"

command = f"../ord/target/release/ord --bitcoin-data-dir {BITCOIN_DATA_DIR} --cookie-file {COOKIE_FILE} --config-dir {CONFIG_DIR} --index {INDEX}"

if args.signet:
    command += " --signet"
elif args.testnet:
    command += " --testnet"
elif args.regtest:
    command += " --regtest"

if args.index_sats:
    command += " --index-sats"
elif args.index_runes:
    command += " --index-runes"
elif args.index_sats_and_runes:
    command += " --index-runes"
    command += " --index-sats"

if args.server:
    command += f" server --http-port {PORT}"
elif args.wallet:
    command += f" wallet --server-url {SERVER_URL}"
    if args.batch:
        command += f" batch --batch {args.batch}"
        if args.fee_rate:
            command += f" --fee-rate {args.fee_rate}"
    elif args.inscribe:
        command += " inscribe"
        if args.fee_rate:
            command += f" --fee-rate {args.fee_rate}"
    elif args.mint:
        command += " mint"
        if args.fee_rate and args.rune:
            command += f" --fee-rate {args.fee_rate} --rune {args.rune}"

if args.args:
    command += ' ' + ' '.join(args.args)
print(command)
run_command_with_logging("ord_server.log", command)
