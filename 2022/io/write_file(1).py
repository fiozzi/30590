# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:33:06 2020

@author: Iozzi
"""

import random
import utility_file

out_filename = 'numbers.txt'

with open(out_filename,'w') as file_out:
    for i in range(5):
        rn = random.randint(1,100)
        line_to_write = str(rn) + '\n'
        file_out.writelines(line_to_write)
        
utility_file.print_file(out_filename)

with open(out_filename,'a') as file_out:
    for i in range(5):
        rn = random.randint(1,100)
        line_to_write = str(rn) + '\n'
        file_out.writelines(line_to_write)
 
utility_file.print_file(out_filename)

in_filename = 'numbers.txt'
out_filename = 'smallnumbers.txt'
threshold = 50

with open(in_filename,'r') as f_in, \
    open(out_filename,'w') as f_out:
    while True:
        # read one line from imput
        line = f_in.readline()
        if line:
            # if we are not at EOF
            # we remove the newline at the end
            line = line.strip()
            if line:
                # if the line is not empty
                # check for the number
                if int(line) < threshold:
                    # prepare the line to write
                    to_write = line + '\n'
                    # write line to output
                    f_out.writelines(to_write)
        else:
            break

utility_file.print_file(in_filename)
utility_file.print_file(out_filename)

