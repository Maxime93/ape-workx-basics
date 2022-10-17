from lib2to3.pgen2 import token
from ape import accounts, project, networks


def deploy():
    print(dir(networks))
    print(networks.provider)
    print(networks.provider.name)
    print(networks.active_provider.name)
    print(networks.active_provider.network.name)

    # default deployer
    deployer = accounts.test_accounts[0]
    if networks.active_provider.network.name == "goerli":
        deployer = accounts.load("my_goerli_account")

    # Assume you have a contract named `MyContract` in your project's contracts folder.
    token_contract = deployer.deploy(project.Token)
    print(token_contract.receipt)

    receiver = accounts.test_accounts[2]
    receipt = token_contract.transfer(receiver, 5000, sender=deployer)
    print(receipt)

    print(token_contract.balanceOf(deployer))
    print(token_contract.balanceOf(receiver))

def main():
    deploy()


