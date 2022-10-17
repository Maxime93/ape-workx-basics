import pytest
from ape import accounts, project

@pytest.fixture
def owner(accounts):
    return accounts[0]

@pytest.fixture
def receiver(accounts):
    return accounts[1]

@pytest.fixture
def token(project, owner):
    return owner.deploy(project.Token)

def test_deploy_token(token, owner):
    # "Should set right owner"
    assert token.owner() == owner.address
    # "Should assigne owner all the funds"
    assert token.balanceOf(owner) == 1000000000

def test_transactions(token, owner, receiver):
    # Should transfer tokens
    token.transfer(receiver, 5000, sender=owner)
    assert token.balanceOf(receiver) == 5000

    # Should fail if not enough tokens
    token.transfer(owner, 7000, sender=receiver)
    assert token.balanceOf(receiver) == 5000

