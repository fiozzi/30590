# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:54:59 2019

@author: Fabrizio
"""

class BankAccount:
    def __init__(self,account_number,holder_name):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return amount

    def deposit(self, amount):
        self.balance += amount
        return amount
    
    def get_balance(self):
        return self.balance
    
    def get_account_data(self):
        return vars(self)

    def disp_account(self):
        for key, value in self.get_account_data().items():
            print(f'{key}: {value}')

class MinimumBalanceAccount(BankAccount):
     def __init__(self,account_number,holder_name,min_balance = 0,locked = False):
            super().__init__(self,account_number,holder_name)
            self.minimum_balance = min_balance
            self.locked = locked
            
     def is_locked(self):
        if self.locked == True:
            return True
        else:
            return False
        
     def lock(self):
        self.locked = True
        return None
        
     def unlock(self, code=0):
        if code == 123:
            self.locked = False
        return None
            
     def withdraw(self, amount):
        if self.locked == True:
            return None
        else:
            if self.balance - amount < self.minimun_balance:
                self.lock()
                return None
            else:
                self.balance = self.balance - amount
                return amount
     
     def deposit(self, amount):
        if self.locked == True:
            return None
        else:
            self.balance += amount
            return amount  
