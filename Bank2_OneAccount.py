accName = ''
accBalance = 0
accPwd = ''

def newAccount(name, balance, password):
    global accName, accBalance, accPwd
    accName = name
    accBalance = balance
    accPwd = password

def show():
    global accName, accBalance, accPwd
    print('Show account details:')
    print('Name: {:>24}'.format(accName))
    print('Balance: {0:>18}{1}'.format('$', accBalance))
    print('Password: {:>20}'.format(accPwd))
    print()

def getBalance(password):
    global accName, accBalance, accPwd
    if password != accPwd:
        print('Incorrect Password!')
        return None
    return accBalance

def deposit(amountToDeposit, password):
    global accName, accBalance, accPwd
    if amountToDeposit <= 0:
        print('Not possible to deposit a negative amount!')
        return None
    elif password != accPwd:
        print('Incorrect Password!')
        return None
    else:
        accBalance = accBalance + amountToDeposit
        return accBalance

def withdraw(amountToWithdraw, password):
    global accName, accBalance, accPwd

    if amountToWithdraw <= 0:
        print('Cannot withdraw $0 and negative amount!')
        return None
    elif password != accPwd:
        print('Incorrect Password')
        return None
    elif amountToWithdraw > accBalance:
        print('Cannot withdraw amount greater than current balance')
        return None
    else:
        accBalance = accBalance - amountToWithdraw
        return accBalance

#newAccount('Asma', 150, 'asma123')

while True:
    print('Press b to get balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower()  # lowercase
    action = action[0]  # Use only first letter
    print()

    if action == 'b':
        print('Get Balance')
        userPwd = input('Please enter password: ')
        currentBalance = getBalance(userPwd)
        if currentBalance is not None:
            print('Your Balance is: ${}'.format(currentBalance))

    elif action == 'd':
        print('Deposit')
        userDepositAmount = int(float(input('Please enter amount to deposit: ')))
        userPwd = input('Please enter password: ')
        newBalance = deposit(userDepositAmount, userPwd)
        if newBalance is not None:
            print('Your new balance is : ${}'.format(newBalance))

    elif action == 'w':
        print('Withdrawl')
        userWithdrawlAmount = int(float(input('Please enter amount to deposit: ')))
        userPwd = input('Please enter password: ')
        newBalance = withdraw(userWithdrawlAmount, userPwd)
        if newBalance is not None:
            print('Your new balance is : ${}'.format(newBalance))

    elif action == 's':
        show()

    elif action == 'q':
        break




