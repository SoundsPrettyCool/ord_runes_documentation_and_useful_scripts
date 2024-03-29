#!/usr/bin/env python3

import subprocess

BITCOIN_DATA_DIR = "/mnt/e/bitcoin/.bitcoin"
COOKIE_FILE = "/mnt/c/bitcoin/.bitcoin/.cookie"
CONFIG_DIR = "/mnt/e/bitcoin/.bitcoin/bitcoin.conf"
INDEX = "/mnt/e/bitcoin/index.redb"

command = f"../ord/target/release/ord --bitcoin-data-dir {BITCOIN_DATA_DIR} --cookie-file {COOKIE_FILE} --config-dir {CONFIG_DIR} --index {INDEX}"
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
