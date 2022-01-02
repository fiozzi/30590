# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:47:01 2020

@author: Iozzi
"""

def print_file(filename):
    with open(filename,'r') as fp:
        # prints the filename
        print(f'File: {filename}')
        while True:
            # read a line from input
            line = fp.readline()
            if line:
                # if we are not at EOF, print line
                # stripped of its trailing
                # newline
                print(line.strip())
            else:
                break
        print('--EOF--')

def split_at(s, sep, n):
    # separates s into two substrings before and
    # after the n-th occurrence of separator
    if s.count(sep) < n:
        return None
    else:
        parts = s.split(sep,n)
        r = parts[n]
        return s[0:-len(r)-len(sep)] , r
    
def anonymize(f_in, k, sep = ',', header = 'ID', f_out = 'out.txt'):
    with open(f_in,'r') as infile, open(f_out,'w') as outfile:
        line_in = infile.readline()
        line_in = line_in.strip()
        s = split_at(line_in,sep,k)
        to_write = header + sep + s[1] + '\n'
        outfile.writelines(to_write)
        nlines = 0
        while True:
            line_in = infile.readline()
            if line_in:
                line_in = line_in.strip()
                if line_in:
                    nlines = nlines + 1
                    s = split_at(line_in,sep,k)
                    to_write = str(nlines) + sep + s[1] + '\n'
                    outfile.writelines(to_write)
            else:
                break
            