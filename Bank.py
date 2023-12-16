from Account import *

class Bank():
    def __init__(self, hours, address, phone):
        self.accountDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        try:
             userAccountNumber = int(float(input('Please Enter User Account Number :')))
        except ValueError:
            raise AbortTransaction('Account number must be an integer')
        if userAccountNumber not in self.accountDict:
            raise AbortTransaction('There.s no account' + str(userAccountNumber))
        return userAccountNumber

    def getUserAccount(self):
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        return oAccount

    def askForValidPassword(self, oAccount):
        userPassword = input('User Password')
        oAccount.checkPassword(userPassword)


    # def createAccount(self, name, amount, password):
    #     oAccount = Account(name, amount, password)
    #     self.nextAccountNumber = self.nextAccountNumber + 1
    #     self.accountDict[self.nextAccountNumber] = oAccount
    #     return self.nextAccountNumber

    def createAccount(self, name, amount, password):
        oAccount = Account(name, amount, password)
        newAccountNumber = self.nextAccountNumber
        self.accountDict[newAccountNumber] = oAccount
        #increment for the next account
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print('..Open Account')
        userName = input('Enter User Name: ')
        userAmount = int(float(input('Enter User Amount for Bank')))
        userPassword = input('User Password')
        userAccountNumber = self.createAccount(userName, userAmount, userPassword)
        print('New Account Number is: ', userAccountNumber)
        print()

    # def closeAccount(self):
    #     print('--Close Account--')
    #     userAccountNumber = int(float(input('Please Enter User Account Number :')))
    #     userPassword = input('User Password')
    #     oAccount = self.accountDict[userAccountNumber]
    #     currentBalance = oAccount.getBalance(userPassword)
    #     if currentBalance is not None:
    #         print('Amount: ', currentBalance, ' is returned..')
    #         del self.accountDict[userAccountNumber]
    #         print("Your account is been closed.")

    def closeAccount(self):
        print(' Close account ')
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        currentBalance = oAccount.getBalance()
        print('Amount: ', currentBalance, ' is returned..')
        del self.accountDict[userAccountNumber]
        print("Your account is been closed.")

    # def balance(self):
    #     print('... Get Balance...')
    #     userAccountNumber = int(float(input('Please Enter User Account Number :')))
    #     userPassword = input('User Password')
    #     oAccount = self.accountDict[userAccountNumber]
    #     currentBalance = oAccount.getBalance(userPassword)
    #     if currentBalance is not None:
    #         print('Your current balance is: ', currentBalance)

    def balance(self):
        print('Get Balance')
        oAccount = self.getUserAccount()
        currentBalance = oAccount.getBalance()
        print('Your current balance is: ', currentBalance)


    # def deposit(self):
    #     print('...Deposit..')
    #     userAccountNumber = int(float(input('Please Enter User Account Number :')))
    #     userDepositAmount = int(float(input('Please enter amount to deposit: ')))
    #     userPassword = input('User Password')
    #     oAccount = self.accountDict[userAccountNumber]
    #     currentBalance = oAccount.deposit(userDepositAmount, userPassword)
    #     if currentBalance is not None:
    #         print('Your new balance is: ', currentBalance)

    def deposit(self):
        print('Deposit')
        oAccount = self.getUserAccount()
        userDepositAmount = input('Please enter amount to deposit: ')
        currentBalance = oAccount.deposit(userDepositAmount)
        print('You have deposited: $ ' + userDepositAmount)
        print('Your new balance is: ', currentBalance)




    def show(self):
        print('Show')
        for userAccountNumber in self.accountDict:
            oAccount  = self.accountDict[userAccountNumber]
            print('Account Number: ', userAccountNumber)
            oAccount.show()

    # def withdraw(self):
    #     print('Withdraw')
    #     userAccountNumber = int(float(input('Please Enter User Account Number :')))
    #     userWithdrawlAmount = int(float(input('Please enter amount to deposit: ')))
    #     userPassword = input('User Password')
    #     oAccount = self.accountDict[userAccountNumber]
    #     currentBalance = oAccount.withdraw(userWithdrawlAmount, userPassword)
    #     if currentBalance is not None:
    #         print('Your new balance is: ', currentBalance)

    def withdraw(self):
        print('Deposit')
        oAccount = self.getUserAccount()
        userWithdrawAmount = input('Please enter amount to deposit: ')
        currentBalance = oAccount.withdraw(userWithdrawAmount)
        print('You have deposited: $ ' + userWithdrawAmount)
        print('Your new balance is: ', currentBalance)

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountsDict), 'account(s) open.')


















