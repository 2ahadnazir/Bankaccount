# USING LIST
from Account import *

accountList = []

abdulAhad = Account('Abdul Ahad', 100, '123')
asmaAhad = Account('Asma Ahad', 200, '321')
accountList.append(abdulAhad)
print('Ahad account number is 0')
accountList.append(asmaAhad)
print('Asma account number is 1')

accountList[0].show()
accountList[1].show()

accountList[0].deposit(213, '123')
print(accountList[0].getBalance('123'))

