from brownie import SimpleStorage, accounts, config

def read_contract():
    # print(SimpleStorage[1])
    # print(SimpleStorage[-1]) # most recent deployment use -1 index
    # ABI
    # Address
    simple_storage_last = SimpleStorage[-1]
    print(simple_storage_last.retrieve()) # retrieves the 666 we stored

def main():
    read_contract()