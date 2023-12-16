# USING DICT

from Account import *
accountDict = {}
nextAccountNumber = 0
oAccount = Account('Abdul Ahad', 200, '123')
ahadAccountNumber = nextAccountNumber
accountDict[ahadAccountNumber] = oAccount
print('Ahad account number is = ', ahadAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Asma', 100, '123')
asmaAccountNumber = nextAccountNumber
accountDict[asmaAccountNumber] = oAccount
print('Asma account number is = ', asmaAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Wasil', 50, '123')
wasilAccountNumber = nextAccountNumber
accountDict[wasilAccountNumber] = oAccount
print('Wasil account number is =', wasilAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountDict[asmaAccountNumber].show()
accountDict[ahadAccountNumber].show()
accountDict[wasilAccountNumber].show()

