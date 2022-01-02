# -*- coding: utf-8 -*-
"""
Created on Sun May  3 07:17:24 2020

@author: Fabrizio
"""

import importlib
import sys
import os
import random

#to unpack environ variable pointing to work folder
path = os.path.expandvars('$HOME')
sys.path.insert(1, path)


#wrap inside try block, this code must not generate error
try:
    m = importlib.import_module('bankaccount')
    ba = m.BankAccount
    mba = m.MinimumBalanceAccount
    c_score = 0
    tot_score = 0
    def check(cond):
        global c_score, tot_score
        try:	
            if eval(cond):
                c_score += 1
            else:
                print('Assert failed:', cond)
            tot_score += 1
        except Exception as e:
            print(e)
            tot_score += 1
    
    #########################
    ###### START TESTS ######
    #########################

    # gazelles
    b1 = mba(123,'Fabrizio')
    b2_mb = random.randint(20,30)
    b2 = mba(456,'Iozzi',b2_mb)

    #init
    check('isinstance(b1, ba)') 
    check('isinstance(b2, ba)') 
    check('b1.holder_name=="Fabrizio"')
    check('b1.account_number==123')
    check('b1.minimum_balance == 0')		
    check('b1.locked == False')
    check('b2.minimum_balance == b2_mb')
    b2.deposit(b2_mb)
            
    #operations
    check('b1.deposit(100) == 100')
    check('b1.get_balance() == 100')
    check('b1.deposit(10) == 10')
    check('b1.get_balance() == 110')
    check('b1.withdraw(20) == 20')
    check('b1.get_balance() == 90')
    check('b2.deposit(100 - b2_mb) == 100 - b2_mb')
    check('b2.get_balance() == 100')
    check('b2.deposit(10) == 10')
    check('b2.get_balance() == 110')
    check('b2.withdraw(20) == 20')
    check('b2.get_balance() == 90')

    # external locking
    b1.locked = True
    b2.locked = True
    check('b1.deposit(100) == None')
    check('b1.get_balance() == 90')
    check('b1.withdraw(20) == None')
    check('b1.get_balance() == 90')
    check('b2.deposit(100) == None')
    check('b2.get_balance() == 90')
    check('b2.withdraw(20) == None')
    check('b2.get_balance() == 90')

    # below minimum balance
    check('b1.unlock(100)==True')
    b1.unlock(123)
    b2.unlock(123)
    check('b1.withdraw(100)==None')
    check('b1.is_locked()==True')
    check('b1.get_balance() == 90')
    check('b1.deposit(100)==None')
    check('b1.is_locked()==True')
    check('b1.get_balance() == 90')
    check('b2.withdraw(100)==None')
    check('b2.is_locked()==True')
    check('b2.get_balance() == 90')
    check('b2.deposit(100)==None')
    check('b2.is_locked()==True')
    check('b2.get_balance() == 90')

    #########################
    ###### END TESTS ######
    #########################
            
    max_score = tot_score
    final_score = round(c_score*max_score/tot_score)
    print(f'Score: {final_score}/{max_score}')
    sys.exit(final_score)
	
except Exception as e:
	print('Test file returned early due to exception')
	print(str(e))
	sys.exit(0)


          
#need to publish scores, make sure you are matching the scoring tag in part description
#https://help.vocareum.com/article/45-scripts-and-resources
#with open('vocareum_grade.csv', 'w') as w:
#          w.write(f'test_score,{c}')

        

sys.exit(c)
