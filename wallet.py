from server_wallet import ServerWallet
from client_wallet import ClientWallet
from plain_wallet import PlainWallet
from memory_wallet import MemoryWallet


# This is a factory method to instantiate a wallet. The wallet constructor handles the logic
# of determining whether a wallet needs to be created from scratch.
def create_wallet(wallet_type, key, logger):
    if wallet_type == 'ServerWallet':
        wallet = ServerWallet(key, logger)
    elif wallet_type == 'ClientWallet':
        wallet = ClientWallet(key)
    elif wallet_type == 'MemoryWallet':
        wallet = MemoryWallet(key)  # Used for file encryption
    else:
        wallet = PlainWallet()
    wallet.instance()
    return wallet
