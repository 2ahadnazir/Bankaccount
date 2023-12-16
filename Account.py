

class AbortTransaction(Exception):
    pass
class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(float(balance))
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(float(amount))
        except ValueError:
            raise AbortTransaction('Amount must be a integer')
        if amount <=0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def checkPassword(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect Password')


    # def deposit(self, amountToDeposit, password):
    #     if password != self.password:
    #         print('Incorrect Password...!')
    #         return None
    #     if amountToDeposit <= 0:
    #         print('ARE YOU SERIOUS...!')
    #         return None
    #     self.balance = self.balance + amountToDeposit
    #     return self.balance

    # new method to work with exceptions
    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    # def withdraw(self, amountToWithdraw, password):
    #     if password != self.password:
    #         print('Incorrect Password...!')
    #         return None
    #     if amountToWithdraw <= 0:
    #         print('ARE YOU SERIOUS...!')
    #         return None
    #     if amountToWithdraw > self.balance:
    #         print('CANNOT WITHDRAW')
    #         return None
    #     self.balance = self.balance - amountToWithdraw
    #     return self.balance

    # new method to work with exceptions
    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if  amountToWithdraw > self.balance:
            raise AbortTransaction('Can.t withdraw more than you have.')
        self.balance = self.balance - amountToWithdraw
        return self.balance

    # def getBalance(self, password):
    #     if password != self.password:
    #         print('Incorrect Password...!')
    #         return None
    #     return self.balance

    def getBalance(self):
        return self.balance


    def show(self):
        print('Show account details:')
        print('Name: {:>24}'.format(self.name))
        print('Balance: {0:>18}{1}'.format('$', self.balance))
        print('Password: {:>20}'.format(self.password))


