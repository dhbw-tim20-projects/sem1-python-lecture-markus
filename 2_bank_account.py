import os
from subprocess import call


def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')


class Account:
    def __init__(self, initialBalance=0):
        self.balance = initialBalance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(amount > self.balance):
            input('Not enough funds available! Press any key to continue')
            return
        self.balance -= amount

    def printBalance(self):
        print(f'Balance: {self.balance}')


operations = ['Deposit', 'Whitedraw', 'Exit']
accountInstance = Account()

clear()

while(True):
    accountInstance.printBalance()

    for index, operation in enumerate(operations):
        print(f'  [{index}] {operation}')

    operation = int(input('Choose an Operation: '))

    if operation == 0:
        amount = float(input('Amount: '))
        accountInstance.deposit(amount)
    elif operation == 1:
        amount = float(input('Amount: '))
        accountInstance.withdraw(amount)
    elif operation == 2:
        clear()
        break
    else:
        input("Unkown operation. Press any key to countinue")

    clear()
