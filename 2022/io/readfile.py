# -*- coding: utf-8 -*-
"""
@author: Fabrizio

https://github.com/MuseumofModernArt/collection
"""

def print_file_1(filename):
    with open(filename,'r') as f:
        allfile = f.read()
        print(allfile)

filename = 'numbers.txt'
print_file_1(filename)

def print_file_2(filename, nlines=0, encoding = 'utf-8'):
    plines = 0
    with open(filename, 'r', encoding = encoding) as f: # DOES NOT ALWAYS WORK
        # with open(filename,'r', encoding='utf-8') as f:
        while ((not nlines) or plines <= nlines):
            line = f.readline()
            if line:
                # line is not exmpty
                plines += 1
                print(line.strip())
            else:
                # reached the end of the file
                break

print_file_2(filename)
filename = 'Artists.txt'
# print_file_2(filename)
# throws error for encoding
print_file_2(filename, encoding = 'utf-8')

# second example with try/except

def print_file_3(filename, nlines=0):
    plines = 0
    try:
        with open(filename,'r') as f: # DOES NOT ALWAYS WORK
            while ((not nlines) or plines <= nlines):
                try:
                    line = f.readline()
                    if line:
                        # line is not exmpty
                        plines += 1
                        print(line.strip())
                    else:
                        # reached the end of the file
                        break
                except Exception as e:
                    print(f'*** Error: {e}')
    except Exception as e:
        print(e)

print_file_3(filename, nlines=200)

# third example with csv

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

"""
EXERCISE: the file MSFT.csv is given with the daily data of Microsoft stock on the
US stock market in 2019. Write a function 

longest_string()

that given 
a filename (with the same format as MSFT.csv), 
a column to be analyzed and 
a parameter sign = +-1, 
returns the day when the data in the column has seen the largest variation (up or
down, according to sign).

"""
def largest_variation(filename, col, refcol, delimiter=',', quotechar='"', sign=1):
    # refcol is supposed to be unique
    try:
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
        return max_var_ref, max_variation
    except Exception as e:
        print(e)
        return None, None

v, vr = largest_variation('MSFT.csv',5,0)
print (v, vr)
