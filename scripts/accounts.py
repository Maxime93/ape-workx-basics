from ape import accounts

sender = accounts.test_accounts[0]

def main():
    # Test accounts
    sender = accounts.test_accounts[0]
    print(sender)
    print(sender.balance)

    my_account = accounts.load("max_goerli")
    print(my_account)
    print(my_account.balance)


