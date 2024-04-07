# useful commands
- `ps -ef` see running processes on your machine
- `kill -9 <pid>` kills the process based on the pid
- `ps -l` see more info about the process.  the s column tells you about the state of the process.  a `D` state tell you that it is in zombie mode. 

- python3 bitcoin_cli.py --regtest --getbalance
- python3 bitcoin_cli.py --regtest createwallet banana
- python3 ord_server_start.py --regtest --index-runes --server
- python3 bitcoin_start.py --regtest
- python3 bitcoin_cli.py --regtest --rpcwallet banana sendtoaddress bcrt1phaem0helwmugx3eeuem0lg7f7hj06vc9jxfvevytuxexa9pxcg8s24tjce 40
- python3 ord_server_start.py --regtest --wallet --batch batch_rune_example.yaml --fee-rate 2
- python3 ord_server_start.py --regtest --wallet --batch batch_rune_example.yaml --fee-rate 2
- python3 bitcoin_cli.py --regtest generatetoaddress 101 bcrt1phaem0helwmugx3eeuem0lg7f7hj06vc9jxfvevytuxexa9pxcg8s24tjce

# own notes 