accountList = []


def newAccount(name, password, balance):
    global accountList
    newAccountDict = {'name': name, 'password': password, 'balance': balance}
    accountList.append(newAccountDict)


def show(accountNumber):
    global accountList
    print('Account: ', accountNumber)
    currentAccountDict = accountList[accountNumber]
    print('Name: {:>24}'.format(currentAccountDict['name']))
    print('Balance: {0:>18}{1}'.format('$', currentAccountDict['balance']))
    print('Password: {:>20}'.format(currentAccountDict['password']))
    print()

def getBalance(accountNumber, password):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']

def deposit(accountNumber,amountToDeposit, password):
    global accountList
    currentAccountDict = accountList[accountNumber]
    if password != currentAccountDict['password']:
        return None
    elif amountToDeposit <= 0:
        return None

    currentAccountDict['balance'] = currentAccountDict['balance'] + amountToDeposit
    return currentAccountDict['balance']

def withdraw(accountNumber,amountToWithdraw, password):
    global accountList
    currentAccountDict = accountList[accountNumber]
    if password != currentAccountDict['password']:
        return None
    elif amountToWithdraw <= 0:
        return None
    elif amountToWithdraw > currentAccountDict['balance']:
        return None

    currentAccountDict['balance'] = currentAccountDict['balance'] - amountToWithdraw
    return currentAccountDict['balance']

print("Abdul's Account Number", len(accountList))
newAccount('Abdul Ahad', 123, 2000)

print("Asma's Account Number:", len(accountList))
newAccount('Asma Afzal', 123, 1500)

while True:
    print()
    print('Press b to get balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press n to create New Account')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower()  # lowercase
    action = action[0]  # Use only first letter
    print()

    if action == 'b':
        print('Check Balance..!')
        userAccountNumber = int(float(input('Please Enter User Account Number :')))
        userPassword = input('Enter User Password: ')
        currentBalance = getBalance(userAccountNumber, userPassword)
        if currentBalance is not None:
            print('Current Balance is: ', currentBalance)

    elif action == 'd':
        print('Deposit')
        userAccountNumber = int(float(input('Please Enter User Account Number :')))
        userPassword = input('Enter User Password: ')
        userDepositAmount = int(float(input('Please enter amount to deposit: ')))

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('New Balance is: ', newBalance)

    elif action == 'n':
        print('New Account')
        userName = input('Enter User Name: ')
        userAmount = int(float(input('Enter User Amount for Bank')))
        userPassword = input('User Password')

        userAccountNumber = len(accountList)
        newAccount(userName, userPassword, userAmount)
        print("Your new account number: ", userAccountNumber)

    elif action == 's':
        print('Show')
        totalAccounts = len(accountList)
        for accountNumber in range(0, totalAccounts):
            show(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdrawl')
        userAccountNumber = int(float(input('Please Enter User Account Number :')))
        userWithdrawlAmount = int(float(input('Please enter amount to withdraw: ')))
        userPassword = input('Enter Password')

        newBalance = withdraw(userAccountNumber, userWithdrawlAmount, userPassword)
        if newBalance is not None:
            print('New balance is: ', newBalance)




