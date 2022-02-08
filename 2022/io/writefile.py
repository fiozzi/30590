# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:33:06 2020

@author: Iozzi
"""

import random

def print_file_3(filename, nlines=0, encoding = 'utf-8'):
    plines = 0
    with open(filename, 'r', encoding = encoding) as f: # DOES NOT ALWAYS WORK
        # with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            plines += 1
            print(line.strip())
            if nlines and (plines > nlines):
                break

out_filename = 'numbers.txt'

with open(out_filename,'w') as file_out:
    for i in range(5):
        rn = random.randint(1,100)
        line_to_write = str(rn) + '\n'
        file_out.writelines(line_to_write)

print('Numbers')
print_file_3(out_filename)

with open(out_filename,'a') as file_out:
    for i in range(5):
        rn = random.randint(1,100)
        line_to_write = str(rn) + '\n'
        file_out.writelines(line_to_write)
 
print('More Numbers')
print_file_3(out_filename)

in_filename = 'numbers.txt'
out_filename = 'smallnumbers.txt'
threshold = 50

with open(in_filename,'r') as f_in, open(out_filename,'w') as f_out:
    for line in f_in:
        if int(line) < threshold:
            f_out.writelines(line)

print('All Numbers')
print_file_3(in_filename)
print('Small Numbers')
print_file_3(out_filename)

