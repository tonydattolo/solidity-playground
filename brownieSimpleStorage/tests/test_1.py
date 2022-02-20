from brownie import SimpleStorage, accounts

def test_deploySimpleStorage():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({'from': account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected
    
def test_updateStorageValue():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from': account})
    # Act
    simple_storage.store(666, {'from': account})
    current_value = simple_storage.retrieve()
    expected = 666
    # Assert
    assert current_value == expected
    
def test_expectingError():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from': account})
    # Act
    simple_storage.store(666, {'from': account})
    expected = 777
    # Assert
    assert expected == simple_storage.retrieve()