# -*- coding: utf-8 -*-
"""
@author: Fabrizio

https://github.com/MuseumofModernArt/collection
"""

# def print_file_1(filename):
#     with open(filename,'r') as f:
#         allfile = f.read()
#         print(allfile)

# def print_file_2(filename):
#     with open(filename,'r') as f:
#         for line in f:
#             print(line)


# filename = 'numbers.txt'
# print_file_2(filename)

# def print_file_3(filename, nlines=0, encoding = 'utf-8'):
#     plines = 0
#     with open(filename, 'r', encoding = encoding) as f: # DOES NOT ALWAYS WORK
#         # with open(filename,'r', encoding='utf-8') as f:
#         for line in f:
#             plines += 1
#             print(line.strip())
#             if nlines and (plines > nlines):
#                 break

# filename = 'Artists.txt'

# print_file_3(filename,nlines=10)

# # # second example with try/except

# def print_file_4(filename, nlines=0):
#     plines = 0
#     try:
#         with open(filename,'r', encoding='utf-8') as f: # DOES NOT ALWAYS WORK
#             try:
#                 for line in f:
#                     plines += 1
#                     print(line.strip())
#                     if nlines and (plines > nlines):
#                         break
#             except Exception as e:
#                 print(f'*** Error: {e}')
#     except Exception as e:
#         print(e)

# print_file_4(filename, nlines=200)

# # # third example with csv

import csv

# with open(filename, newline='', encoding='utf-8') as f:
#     linereader = csv.DictReader(f, delimiter=',', quotechar='"')
#     gender = {}
#     for row in linereader:
#         if row['Gender'] in gender.keys():
#             gender[row['Gender']] += 1
#         else:
#             gender[row['Gender']] = 1
#     print(gender)

# """
# EXERCISE: the file MSFT.csv is given with the daily data of Microsoft stock on the
# US stock market in 2019. Write a function 

# largest_variation()

# that given 
# a filename (with the same format as MSFT.csv), 
# a column to be analyzed and 
# a parameter sign = +-1, 
# returns the day when the data in the column has seen the largest variation (up or
# down, according to sign).

# """
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
