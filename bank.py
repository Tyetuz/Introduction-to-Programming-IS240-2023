#bank
class BankAccount:
    def __init__(self, customer="", balance=0):
        self._customer = customer
        self._balance = balance
        
    def __str__(self):
        return(self._customer + " $" + str(self._balance))
    
    def setCustomer(self, customer):
        self._customer = customer

    def setBalance(self, balance):
        self._balance = balance

    def getCustomer(self):
        return self._customer

    def getBalance(self):
        return self._balance

    def makeDeposit(self, amount):
        self._balance += amount

    def makeWithdrawal(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
        else:
            print("Insufficient funds")