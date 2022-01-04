# -*- coding: utf-8 -*-
"""
@author: Fabrizio

https://github.com/MuseumofModernArt/collection
"""

def print_file(filename, nlines=0):
    plines = 0
    # with open(filename,'r') as f: DOES NOT ALWAYS WORK
    with open(filename,'r', encoding='utf-8') as f:
        while ((not nlines) or plines <= nlines):
            line = f.readline()
            if line:
                # line is not exmpty
                plines += 1
                print(line.strip())
            else:
                # reached the end of the file
                break

def print_file_2(filename):
    with open(filename,'r') as f:
        print(f.read())

# filename = 'numbers.txt'
filename = 'Artists.txt'

print_file(filename, nlines=4)
# print_file_2(filename)

import csv

with open(filename, newline='', encoding='utf-8') as f:
    linereader = csv.reader(f, delimiter=',', quotechar='"')
    missing_data_lines_count = 0
    data_lines_count = 0
    for row in linereader:
        data_lines_count += 1
        if not (
            row[0] and row[1] and row[2] and row[3] and 
            row[4] and row[5] and row[6] and row[7] and row[8]) :
            missing_data_lines_count += 1
    print(missing_data_lines_count, data_lines_count)

def longest_string(filename, col, refcol, delimiter=',', quotechar='"', sign=1):
    # refcol is supposed to be unique
    with open(filename,'r') as f:
        linereader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        headers = next(linereader)
        firstrow = next(linereader)
        prev_val = float(firstrow[col])
        max_variation = 0
        max_var_ref = firstrow[refcol]
        for row in linereader:
            if (float(row[col]) - prev_val) * sign > 0:
                variation = float(row[col]) - prev_val
                if variation > max_variation:
                    max_variation = variation
                    max_var_ref = row[refcol]
            prev_val = float(row[col])
    
    return max_var_ref, max_var_ref

v, vr = longest_string('MSFT.csv',5,0)
print (v, vr)