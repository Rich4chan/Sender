"""
Configuration module for network settings.
"""

NETWORKS = {
    "erc20": {
        "name": "Ethereum",
        "chain_id": 1,
        "rpc_url": "https://mainnet.infura.io/v3/demo",
        "token_contract": "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    },
    "bep20": {
        "name": "Binance Smart Chain",
        "chain_id": 56,
        "rpc_url": "https://bsc-dataseed.binance.org/",
        "token_contract": "0x55d398326f99059ff775485246999027b3197955"
    },
    "trc20": {
        "name": "Tron",
        "chain_id": 1,
        "rpc_url": "https://api.trongrid.io",
        "token_contract": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
    }
}

def get_network_config(network):
    return NETWORKS.get(network.lower())