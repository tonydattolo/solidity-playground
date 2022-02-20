from brownie import accounts, config
import os


def grabWallets():
    # this will grab the local brownie ganache instance accounts to use for testing
    account_0 = accounts[0]
    print(f'{account_0} sample account from local brownie instance ganache-cli')
    
    # this will prompt you for the passphrase used to encrypt the account
    sampleGanache9 = accounts.load("sampleGanache9")
    print(f'{sampleGanache9} sample account from added private key')
    
    # can programatically add accounts to brownie.accounts from env vars
    sampleGanache9fromEnv = accounts.add(os.getenv("SAMPLE_GANACHE9_PRIVATE_KEY"))
    print(f'{sampleGanache9fromEnv} sample account from private key in env')    
    
    # can add accounts using yaml settings
    sampleFromYaml = accounts.add(config["wallets"]["SAMPLE_GANACHE9_PRIVATE_KEY"])
    # sampleFromYaml = accounts.add(config["wallets"]["sampleGanache9"]["privateKey"])

def main():
    grabWallets()