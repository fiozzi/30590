# -*- coding: utf-8 -*-
"""

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

def anonymize2(f_in, k, sep = ',', header = 'ID', f_out = 'out.txt', t_out = 'table.txt'):
    with open(f_in, 'r') as infile, open(f_out, 'w') as outfile, open(t_out, 'w') as outfile2:
        line_in = infile.readline()
        line_in = line_in.strip()
        s = split_at(line_in,sep,k)
        to_write = header + sep + s[1] + '\n'         
        outfile.writelines(to_write)
        to_write2 = header + sep + s[0] + '\n'
        outfile2.writelines(to_write2)
        nlines = 0
        
        while True:
            line_in = infile.readline()
            if line_in:
                line_in =line_in.strip()
                if line_in:
                    nlines = nlines + 1
                    s = split_at(line_in,sep,k)
                    to_write = str(nlines) + sep + s[1] + '\n'
                    to_write2 = str(nlines) + sep + s[0] + '\n'
                    outfile.writelines(to_write)
                    outfile2.writelines(to_write2)
            else:
                break


if __name__ == '__main__':
    anonymize('midterm.txt',2)
    anonymize2('midterm.txt', k=2)
