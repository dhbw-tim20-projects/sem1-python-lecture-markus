"""Snack automat application
"""
import os
import random
from subprocess import call
from product import Product, ProductNotAvailibleException


class Main:
    """Represents the whole application state
    """

    def __init__(self):
        self.create_depot()
        self.balance = 100
        self.operations = ['Exit', 'Show Balance',
                           'Show Depot', 'Deposit', 'Buy a Product']

    def run(self):
        """Run the base application lifecycle
        """
        self.print_menu()
        operation = self.ask_for_operation()
        if operation == 0:
            exit()
        elif operation == 1:
            self.print_balance()
        elif operation == 2:
            print('asdasdasdasdasdasdasdasdad')
            self.print_depot()
        elif operation == 3:
            self.deposit()
        elif operation == 4:
            self.buy_product()

    def create_depot(self):
        """Initialse the depot
        """
        self.depot = [
            Product('Apple', random.randint(1, 9), 2),
            Product('Banna', random.randint(1, 9), 2),
            Product('Orange', random.randint(1, 9), 2),
            Product('Kiwi', random.randint(1, 9), 2),
            Product('Avocado', random.randint(1, 9), 2),
            Product('Grape', random.randint(1, 9), 2),
            Product('Lime', random.randint(1, 9), 2),
            Product('Cranberry', random.randint(1, 9), 2),
            Product('Cherry', random.randint(1, 9), 2),
            Product('Cucumber', random.randint(1, 9), 2),
        ]

    def clear_console(self):
        """Run clear/cls command
        """
        call('clear' if os.name == 'posix' else 'cls')

    def print_balance(self):
        """Print the current balance of the user
        """
        self.clear_console()
        print(f'Balance: {self.balance}')
        input('Press any key to continue...')

    def print_menu(self):
        """Print main menu
        """
        self.clear_console()
        for index, operation in enumerate(self.operations):
            print(f'[{index}] {operation}')

    def is_index_available(self, value: int, lst: list) -> bool:
        """Check if a number is a valid index in a list

        Args:
            value (int): Number to check
            list (list): List to check

        Returns:
            bool: True if index is valid
        """
        return value >= 0 and value < len(lst)

    def ask_for_operation(self):
        """Ask the user for an operation to exceute

        Returns:
            int: Operation given by the user
        """
        try:
            operation = int(input('Please select a operation: '))
            if self.is_index_available(operation, self.operations):
                return operation
            raise ValueError
        except ValueError:
            print('Please enter a valid operation. Try again')
            self.ask_for_operation()

    def print_depot(self):
        """Print the current depot as table
        """
        self.clear_console()
        print('{:<15} {:<8} {:<8}'.format('Name', 'Price', 'Amount'))
        for product in self.depot:
            print('{:<15} {:<8} {:<8}'.format(
                product.name, product.price, product.amount))
        input('Press any key to continue...')

    def deposit(self):
        """Deposit credits to the balance
        """
        self.clear_console()
        try:
            amount = int(input('Enter an amount: '))
            if amount > 0:
                self.balance += amount
                self.print_balance()
                return
            raise ValueError
        except ValueError:
            input('Amount must be a valid number and > 0. Press any key to try again...')
            self.deposit()

    def buy_product(self):
        """Buy a product
        """
        self.clear_console()
        print('{:<3} {:<15} {:<8} {:<8}'.format(
            '', 'Name', 'Price', 'Amount'))
        for index, product in enumerate(self.depot):
            print('[{:}] {:<15} {:<8} {:<8}'.format(
                index, product.name, product.price, product.amount))
        try:
            product = int(input('Please select a Product: '))
            if self.is_index_available(product, self.depot):
                try:
                    self.clear_console()
                    selected_product = self.depot[product]
                    if selected_product.price > self.balance:
                        print('Sorry! You dont have enough credits')
                        input('Press any key to countinue')
                        return
                    selected_product.reduce(1)
                    self.balance -= selected_product.price
                    print(
                        f'Success! You are now the owner of a/an new {selected_product.name}.')
                    input('Press any key to continue...')
                except ProductNotAvailibleException as exception:
                    print(str(exception))
                    input('Press any key to countinue')
                return
            raise ValueError
        except ValueError:
            self.clear_console()
            input('Input must be a product number and > 0. Press any key to try again...')
            self.buy_product()


if __name__ == '__main__':
    instance = Main()
    while True:
        instance.run()
