from brownie import accounts, config, SimpleStorage

def deploy_simple_storage():
    account = accounts[0]
    simpleStorage = SimpleStorage.deploy({'from': account})
    # Transact
    # Call
    currentStoredValue = simpleStorage.retrieve()
    print(f'{currentStoredValue=}')
    
    storeValueTx = simpleStorage.store(666, {'from': account})
    storeValueTx.wait(1)
    
    currentStoredValue = simpleStorage.retrieve()
    
    print(f'{currentStoredValue=}')
    
def main():
    deploy_simple_storage()