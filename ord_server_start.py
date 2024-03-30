#!/usr/bin/env python3

import subprocess
import argparse

BITCOIN_DATA_DIR = "/mnt/e/bitcoin/.bitcoin"
COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/.cookie"
CONFIG_DIR = "/mnt/e/bitcoin/.bitcoin/bitcoin.conf"
INDEX = "/mnt/e/bitcoin/index.redb"
PORT = "2222"
SIGNET_PORT = "38332"
parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
parser.add_argument("--index-sats-and-runes", help="add -index-sats at the end of the script", action="store_true")

args = parser.parse_args()
if args.signet:
    COOKIE_FILE = "/mnt/e/bitcoin/.bitcoin/signet/.cookie"
    PORT = SIGNET_PORT
    if args.index_sats_and_runes:
        INDEX = "/mnt/e/bitcoin/index_signet_sats_and_runes.redb"
    else:
        INDEX = "/mnt/e/bitcoin/index_signet.redb"
elif args.index_sats_and_runes:
    INDEX = "/mnt/e/bitcoin/index.redb"

command = f"../ord/target/release/ord --bitcoin-data-dir {BITCOIN_DATA_DIR} --cookie-file {COOKIE_FILE} --config-dir {CONFIG_DIR} --index {INDEX}"

if args.signet:
    command += " --signet"
if args.index_sats_and_runes:
    command += " --index-sats"
    command += " --index-runes"

command += f" server --http-port {PORT}"

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())
returncode = process.poll()

if returncode != 0:
    print(f"Error occurred with return code: {returncode}")
