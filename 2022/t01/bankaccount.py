# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:54:59 2019

@author: Fabrizio
"""
from datetime import datetime as dt

class BankAccount:
    def __init__(self,iban,holder_name):
        self.iban = iban
        self.holder_name = holder_name
        self.balance = 0
        self.last_modified = dt.now()
        self.transactions_file = f'{self.iban}.log'
        with open(self.transactions_file,'w') as f:
            f.write(f'Created: {dt.now()}\n')

    def operation(self, amount, description):
        self.write_transaction(dt.now(), amount, description)
        self.balance += amount
        self.last_modified = dt.now()
        return amount

    def write_transaction(self, date, amount, description):
        with open(self.transactions_file,'a') as f:
            f.write(f'{dt.now()}, {amount}, "{description}"\n')

    def withdraw(self, amount, description=''):
        if self.balance >= amount:
            return -self.operation(-amount, description)
        else:
            return None

    def deposit(self, amount, description=''):
        return self.operation(amount, description)
    
    def status(self):
        displayed_properties = ['iban', 'holder_name', 'balance']
        status_data = { key: vars(self)[key] for key in displayed_properties }
        return status_data

    def __repr__(self):
        tt = self.last_modified.timetuple()
        return (
            f'BankAccount(iban="{self.iban}", '
            f'holder_name="{self.holder_name}", '
            f'last_modified=datetime.datetime({tt[0]}, {tt[1]}, {tt[2]}, {tt[3]}, {tt[4]}), '
            f'balance={self.balance})')

class MinimumBalanceAccount(BankAccount):
    def __init__(self, account_number, holder_name, minimum_balance = 0):
        super().__init__(account_number, holder_name)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount, description=''):
        # check for enough money on the account
        if self.balance - amount < self.minimum_balance:
            amount = self.balance - self.minimum_balance
        return -self.operation(-amount, description)

if __name__=='__main__':

    def print_transactions(self):
        with open(self.transactions_file,'r') as f:
            return f.read()

    ba1 = BankAccount(123,'Fabrizio')
    print(ba1)
    ba1.deposit(1000, "First deposit")
    print_transactions(ba1)
    print(ba1)
    ba2 = MinimumBalanceAccount(234,'Iozzi',minimum_balance=100)
    print(ba2)
    ba2.deposit(1000, "First deposit")
    ba2.withdraw(500, "First withdrawal")
    ba2.withdraw(500, "Second withdrawal")
    print_transactions(ba2)
    print(ba2)
    

