# Test program using accounts
# Version 1, using explicti variables for each Account object
from Account import Account

abdulAhad = Account('Abdul Ahad', 100, '123')
asmaAhad = Account('Asma Ahad', 200, '321')

asmaAhad.show()
abdulAhad.show()

asmaAhad.deposit(135, '321')
asmaAhad.show()
asmaAhad.withdraw(35, '321')
asmaAhad.show()




