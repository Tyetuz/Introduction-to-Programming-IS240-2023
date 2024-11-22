import bank

def main():
    account = bank.BankAccount("Fred Chopin", 5000)
    print(account)
    account.makeDeposit(250)
    print(account)
    account.makeWithdrawal(2750)
    print(account)
    
    
main()