from brownie import accounts, config, SimpleStorage, network
from dotenv import load_dotenv
load_dotenv()

def deploy_simple_storage():
    account = accounts[0]
    simpleStorage = SimpleStorage.deploy({'from': account}) # accessing SimpleStorage.sol
    # Transact
    # Call
    currentStoredValue = simpleStorage.retrieve()
    print(f'{currentStoredValue=}')
    
    storeValueTx = simpleStorage.store(666, {'from': account})
    storeValueTx.wait(1)
    
    currentStoredValue = simpleStorage.retrieve()
    
    print(f'{currentStoredValue=}')

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_2():
    account = get_account()
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
    # deploy_simple_storage()
    # script:
    # brownie run scripts/deploySimpleStorage.py --network rinkeby
    deploy_2()
