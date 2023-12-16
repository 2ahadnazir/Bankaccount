# Using interactive menu
# from Account import *
from Bank import *
oBank = Bank('9am-5pm', 'Faisal Garder, Phase II', '+92 331 6677 911')

abdulAhadAccount = oBank.createAccount('Abdul Ahad', 1000,'123')
asmaAccount = oBank.createAccount('Asma Ahad', 750,'123')


while True:
    print()
    print('Press b to get balance')
    print('Press c to close account')
    print('Press d to make a deposit')
    print('Press o to open new account')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower()  # lowercase
    action = action[0]  # Use only first letter
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'o':
            oBank.openAccount()
        elif action == 's':
            oBank.show()
        elif action == 'q':
            break
        elif action == 'w':
            oBank.withdraw()
    except AbortTransaction as error:
        print('Sorry, Please enter any valid action')
print('Done....!')



# accountDict = {}
# nextAccountNumber = 0
#
# while True:
#     print()
#     print('Press b to get balance')
#     print('Press d to make a deposit')
#     print('Press w to make a withdrawal')
#     print('Press s to show the account')
#     print('Press n to create New Account')
#     print('Press q to quit')
#     print()
#
#     action = input('What do you want to do?')
#     action = action.lower()  # lowercase
#     action = action[0]  # Use only first letter
#     print()
#
#     if action == 'b':
#         print('Check Balance..!')
#         userAccountNumber = int(float(input('Please Enter User Account Number :')))
#         userPassword = input('Enter User Password: ')
#         oAccount = accountDict[userAccountNumber]
#         currentBalance = oAccount.getBalance(userPassword)
#         if currentBalance is not None:
#             print('Current Balance is: ', currentBalance)
#
#
#     elif action == 'd':
#         print('Deposit')
#         userAccountNumber = int(float(input('Please Enter User Account Number :')))
#         userPassword = input('Enter User Password: ')
#         userDepositAmount = int(float(input('Please enter amount to deposit: ')))
#         oAccount = accountDict[userAccountNumber]
#         newBalance = oAccount.deposit(userDepositAmount, userPassword)
#         if newBalance is not None:
#             print('New Balance is: ', newBalance)
#
#     elif action == 'n':
#         print('New Account')
#         userName = input('Enter User Name: ')
#         userAmount = int(float(input('Enter User Amount for Bank')))
#         userPassword = input('User Password')
#         oAccount = Account(userName, userAmount, userPassword)
#         accountDict[nextAccountNumber] = oAccount
#         nextAccountNumber = nextAccountNumber + 1
#         print()
#
#     elif action == 's':
#         print('Show')
#         for userAccountNumber in accountDict:
#             oAccount  =accountDict[userAccountNumber]
#             print('Account Number: ', userAccountNumber)
#             oAccount.show()
#
#     elif action == 'q':
#         break
#
#     elif action == 'w':
#         print('Withdrawl')
#         userAccountNumber = int(float(input('Please Enter User Account Number :')))
#         userWithdrawlAmount = int(float(input('Please enter amount to withdraw: ')))
#         userPassword = input('Enter Password')
#         oAccount = accountDict[userAccountNumber]
#
#         newBalance = oAccount.withdraw(userWithdrawlAmount, userPassword)
#         if newBalance is not None:
#             print('Withdrawl amount: ', userWithdrawlAmount)
#             print('New balance is: ', newBalance)
#     else:
#         print('Server Down, try again...!')
#
# print('Done')

