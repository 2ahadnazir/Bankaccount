#Without OOP
#Bank Version 1
# Single Account

accName = 'Abdul Ahad'
accBalance = 100
accPwd = 'ahad123'

while True:
    print('Press b to get balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower() #lowercase
    action = action[0] # Use only first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userPwd = input('Please enter password: ')
        if userPwd != accPwd:
            print('Incorrect Password')
        else:
            print('Your balance is ${}'.format(accBalance))

    elif action == 'd':
        print('Deposit')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(float(userDepositAmount))
        userPwd = input('Please enter password: ')

        if userDepositAmount <= 0:
            print("Can't Enter nothing and a negative value!")

        elif userPwd != accPwd:
            print('Incorrect Password')
        else:
            accBalance = accBalance + userDepositAmount
            print('Your new balance is : ${}'.format(accBalance))

    elif action == 's':
        print('Show account details:')
        print('Name: {:>24}'.format(accName))
        print('Balance: {0:>18}{1}'.format('$',accBalance))
        print('Password: {:>20}'.format(accPwd))

    elif action == 'q':
        print('Good Bye')
        break

    elif action == 'w':
        print('Withdrawl')

        userWithdrawalAmount = int(float(input('Enter amount to withdraw: ')))
        userPwd = input('Please enter password: ')
        if userWithdrawalAmount <= 0:
            print('Cannot withdraw $0 and negative amount!')
        elif userPwd != accPwd:
            print('Incorrect Password')
        elif userWithdrawalAmount > accBalance:
            print('Cannot withdraw amount greater than current balance')
        else:
            accBalance = accBalance - userWithdrawalAmount
            print('Your new balance is: {}'.format(accBalance))

print('Done')
