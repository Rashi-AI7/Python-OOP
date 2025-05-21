class bankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def inc_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        self.__balance -= amount

    def deduc_balance(self):
        return self.__balance
    
account = bankAccount(4000)
account.deposit(500)
print(account.inc_balance())  #4500
account.withdraw(1000)
print(account.deduc_balance()) #3500

# print(account.__balance) will raise en error