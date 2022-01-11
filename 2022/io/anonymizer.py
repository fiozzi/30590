# -*- coding: utf-8 -*-
"""

@author: Iozzi
"""
import utility_file
import csv

def split_at(s, sep, n):
    # separates s into two substrings before and
    # after the n-th occurrence of separator
    if s.count(sep) < n:
        return None
    else:
        parts = s.split(sep,n)
        r = parts[n]
        return s[0:-len(r)-len(sep)] , r

def anonymize(
    csv_file,                       
    cols_to_remove = [],
    fields_to_remove = [],
    has_header = True,
    sep = ',',        
    quotechar = None,     
    anonymized_file = 'out.txt',   
    new_header = 'ID',             
    build_table = False,           
    table_file = 'table.txt'):
    """
    csv_file : name of csv file
    cols_to_remove : list of zero-based numbers or field names
    fields_to_remove : list of zero-based numbers or field names
    has_header : bool, True if the first row is the header
    sep : fields separator
    quotechar : quote symbol
    anonymized_file : name of anonymized file
    new_header : field name for id in anonymized file (if has_header)
    build_table : bool True if reference table must be created
    table_file : name of reference table (each line is "ID, removed columns")
    """
    try:
        with open(csv_file, encoding='utf-8') as f_in, open(anonymized_file, 'w', newline='') as f_out:
            line_reader = csv.reader(f_in)
            line_writer = csv.writer(f_out, dialect='excel')
            cols_to_keep = []
            if has_header:
                # reads header in list and puts indexes in cols_to_remove.
                # Will use cols_to_remove from here on
                headers = next(line_reader)
                for col in headers:
                    if col in fields_to_remove:
                        cols_to_remove.append(headers.index(col))
                    else:
                        cols_to_keep.append(headers.index(col))
                # write new header to file
                anon_header = [new_header]
                [anon_header.append(headers[col]) for col in cols_to_keep]
                line_writer.writerow(anon_header)
                # print(anon_header)
            if build_table:
                try:
                    with open(table_file, 'w', newline='') as f_table:
                        table_writer = csv.writer(f_table, dialect='excel')
                        table_header = [new_header]
                        [table_header.append(headers[col]) for col in cols_to_remove]
                        table_writer.writerow(table_header)
                        write_anonymized(line_reader,cols_to_keep, line_writer, table_writer, cols_to_remove)
                except Exception as e:
                    print(f'Error in opening table file for writing: {e}')
            else:
                write_anonymized(line_reader,cols_to_keep,line_writer)
                    
    except Exception as e:
        print('Error in opening cvs and/or anon file: {e.errno}, {e.strerror}, {e.filename}')

def write_anonymized(linereader, cols_to_keep, line_writer, table_writer=None, cols_to_remove=[] ):
    row_counter = 0
    for row in linereader:
        row_counter += 1
        anonymized_row = [str(row_counter)]
        [anonymized_row.append(row[col]) for col in cols_to_keep]
        line_writer.writerow(anonymized_row)
        if table_writer:
            table_row = [str(row_counter)]
            [table_row.append(row[col]) for col in cols_to_remove]
            table_writer.writerow(table_row)

def anonymize_nocsv(f_in, k, sep = ',', header = 'ID', f_out = 'out.txt'):
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
    anonymize(csv_file = 'shortmidterm.txt', fields_to_remove=['STUDENTID','FIRSTNAME'], quotechar='"', build_table=True)
    # anonymize2('midterm.txt', k=2)
