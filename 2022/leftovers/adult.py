# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:14:50 2020

@author: Iozzi
"""

threshold = 10
lines_counter = 0
over_counter = 0

with open('adult.data','r') as input_file:
    while True:
        line = input_file.readline()
        if line:
            lines_counter = lines_counter + 1
            data = line.split(',')
            schooling_years = int(data[4])
            if schooling_years >= threshold:
                over_counter = over_counter + 1
        else:
            break
        
print(f'Lines read: {lines_counter}.')
print(f'Threshold: {threshold}.')
print(f'Lines over threshold: {over_counter}.')
perc_over = over_counter / lines_counter
print(f'Percentage over threshold: {perc_over}.')