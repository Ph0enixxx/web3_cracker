from web3 import Web3
INFURA_SECRET_KEY = "a53b6ae7acb1409e9a261e1d53b55df1"

def get_w3_by_network(network='mainnet'):
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}' # 接入 Infura
    w3 = Web3(Web3.HTTPProvider(infura_url))
    return w3

a = get_w3_by_network()
print(a.eth.get_balance(Web3.toChecksumAddress("0x220866b1a2219f40e72f5c628b65d54268ca3a9d")))