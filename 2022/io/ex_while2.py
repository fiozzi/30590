# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:33:16 2020

@author: Iozzi
"""

import random
random.seed()

# fix n
n = 20

numbers_list = list(range(n))
print(numbers_list)
random.shuffle(numbers_list)
print(numbers_list)

i = 0
while numbers_list[i] != 0:
    i = i + 1
print(f'The number 0 is in position {i}.')

for i in range(n):
    if numbers_list[i] == 0:
        print(f'The number 0 is in position {i}.')
        # we exit the loop, since we are done
        break
