from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development"]


def get_account(index=None):
    if index:
        account = accounts[index]
    elif network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        account = accounts[0]
    else:
        account = accounts.add(config["wallets"]["from_key"])
    return account
