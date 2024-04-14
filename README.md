# Intro
- This is set of scripts that help with running a bitcoin node, bitcoin-cli and the ord server. Each script has environment variables that should be changed to match your environment.  please update these in order for scripts to run successfully.  they are marked with comments in the code.
- ord_server_start.py is the original script to run the ord server but i have condensed it down in ord_server_start2.py.  please use ord_server_start2.py if you want to start the ord_server. 
# sample commands
- These are some sample commands that have helped me during my journey of learning ord:

- python3 bitcoin_cli.py --regtest --getbalance
- python3 bitcoin_cli.py --regtest createwallet banana
- python3 ord_server_start.py --regtest --index-runes --server
- python3 bitcoin_start.py --regtest
- python3 bitcoin_cli.py --regtest --rpcwallet banana sendtoaddress bcrt1phaem0helwmugx3eeuem0lg7f7hj06vc9jxfvevytuxexa9pxcg8s24tjce 40
- python3 ord_server_start.py --regtest --wallet --batch batch_rune_example.yaml --fee-rate 2
- python3 ord_server_start.py --regtest --wallet --batch batch_rune_example.yaml --fee-rate 2
- python3 bitcoin_cli.py --regtest generatetoaddress 101 bcrt1phaem0helwmugx3eeuem0lg7f7hj06vc9jxfvevytuxexa9pxcg8s24tjce