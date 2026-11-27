# 4-6: Bank account; money represented with Decimal, not floating point
from decimal import Decimal

class BankAccount:
    def __init__(self, number):
        digits = ''.join(number.split())
        if len(digits) != 26 or not digits.isdigit():
            raise ValueError('Account number must contain 26 digits')
        self.number = number
        self.balance = Decimal('0.00')

    def deposit(self, amount):
        amount = Decimal(str(amount))
        if amount <= 0:
            raise ValueError('Deposit must be positive')
        self.balance += amount

    def withdraw(self, amount):
        amount = Decimal(str(amount))
        if amount <= 0:
            raise ValueError('Withdrawal must be positive')
        if amount > self.balance:
            print('Insufficient funds on the account')
        else:
            self.balance -= amount

    def show_balance(self):
        print('Bank Account No:', self.number)
        print('Balance: PLN', f'{self.balance:.2f}'.replace('.', ','))

account = BankAccount('12 3456 5555 9090 1111 0000 7722')
account.show_balance()
account.deposit('25.30')
account.show_balance()
account.withdraw('31.70')
account.show_balance()
account.withdraw('14')
account.show_balance()
