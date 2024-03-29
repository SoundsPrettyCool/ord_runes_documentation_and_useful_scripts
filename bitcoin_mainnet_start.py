#!/usr/bin/env python3

import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
args = parser.parse_args()

DATADIR="/mnt/e/bitcoin/.bitcoin"
CONF="/mnt/e/bitcoin/.bitcoin/bitcoin.conf"

command = f"../bitcoin-25.0/bin/bitcoind -datadir={DATADIR} -conf={CONF}"
if args.signet:
    command += " -signet"

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