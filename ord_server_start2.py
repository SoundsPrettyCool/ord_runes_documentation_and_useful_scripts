#!/usr/bin/env python3
import argparse
import json
import yaml
from utils import run_command_with_logging
with open("ord_constants.json", "r", encoding='utf-8') as f:
    constants = json.load(f)

#constants default to mainnet values
CONFIG_YAML = constants["CONFIG_YAML"]
PORT = "2222"
COOKIE_FILE = "/mnt/c/bitcoin/.bitcoin/.cookie"
SERVER_URL = f"http://localhost:{PORT}"

#arguments passed into the script
parser = argparse.ArgumentParser()
parser.add_argument("--signet", help="add -signet at the end of the script", action="store_true")
parser.add_argument("--testnet", help="add -testnet at the end of the script", action="store_true")
parser.add_argument("--regtest", help="add -regtest at the end of the script", action="store_true")
parser.add_argument("--server", help="add -server at the end of the script", action="store_true")
parser.add_argument("--wallet", help="specify the wallet", action="store_true")
parser.add_argument("--batch", help="specify the batch", default=None)
parser.add_argument("--fee-rate", help="specify the fee-rate", default=None)
parser.add_argument("--inscribe", help="specify that you want to inscribe", action="store_true")
parser.add_argument("--mint", help="specify that you want to mint", action="store_true")
parser.add_argument("--rune", help="specify that you want to mint runes", default=None)
parser.add_argument('args', nargs=argparse.REMAINDER)  # pass all the arguments after the options
args = parser.parse_args()

with open(CONFIG_YAML, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)


if args.signet or args.testnet or args.regtest:
    chain = args.signet and 'SIGNET' or args.testnet and 'TESTNET' or 'REGTEST'
    chain_constants = constants[chain]

    #constants are updated here
    COOKIE_FILE = chain_constants["COOKIE_FILE"]
    PORT = chain_constants["PORT"]
    SERVER_URL = f"http://localhost:{PORT}"

    config['chain'] = chain
else:
    config['chain'] = "mainnet"

with open(CONFIG_YAML, 'w', encoding='utf-8') as f:
    yaml.safe_dump(config, f)

#command to start the ord binary
#need to update the path to the ord binary
command = f"../ord/target/release/ord --config {CONFIG_YAML} --cookie-file {COOKIE_FILE}"

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

#print command to execute
print(command)
run_command_with_logging("ord_server.log", command)
