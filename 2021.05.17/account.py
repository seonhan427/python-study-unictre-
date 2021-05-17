class Account:
    def __init__(self, account='', balance=0, interestRate=0):
        self.__account = account
        self.__balance = balance
        self.__interestRate = interestRate
    def setAccount(self, account):
        self.__account = account
    def getAccount(self):
        # print(self.__account)
        return self.__account
    def getBalance(self):
        # print(self.__balance)
        return self.__balance
    def calculateInterest(self):
        return self.__balance*self.__interestRate
    def deposit(self, money):
        self.__balance += money
    def withdraw(self, money):
        self.__balance -= money
    # def __str__(self):
    #     return "account:{}, balance{}, interestRate:{}".format(self.__account, self.__balance,self.__interestRate)    

# Account 객체생성

account = Account("441-0290-1203",500000,0.073)
print(account.getBalance())





# print()

# account = Account()
# print(account)
