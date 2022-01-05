# -*- coding: utf-8 -*-

import bankaccount as ba 
import configparser
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l',"--language", help="specify language for messages")
args = parser.parse_args()
if args.language:
    language = args.language
else:
    language = None

config = configparser.ConfigParser()
config_file = os.path.join(os.getcwd(),'example_bankaccount.ini')
if os.path.exists(config_file):
    config.read(config_file)
    if not language:
        language = config['DEFAULT']['language']
    withdraw_error = config[language]['withdraw error']
else:
    print('Missing config file.')
    withdraw_error = ''

def print_transactions(self):
    with open(self.transactions_file,'r') as f:
        print(f.read())

def try_withdraw(account, amount, description):
    withdrawn_amount = account.withdraw(amount, description)
    if withdrawn_amount != amount:
        print(f'{withdraw_error}')
    print(f'Withdrawn amount: {withdrawn_amount}')

ba1 = ba.BankAccount(123,'Fabrizio')
print(ba1)
ba1.deposit(1000, "First deposit")
print_transactions(ba1)
print(ba1)
ba2 = ba.MinimumBalanceAccount(234,'Iozzi',minimum_balance=100)
print(ba2)
ba2.deposit(1000, "First deposit")
print(ba2)
try_withdraw(ba2, 500, "First withdrawal")
print(ba2)
try_withdraw(ba2, 500, "Second withdrawal")
print(ba2)
print_transactions(ba2)

