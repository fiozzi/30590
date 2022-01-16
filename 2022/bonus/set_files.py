import csv
import random

random.seed()
curr_id = 1
with open('names1.txt','r') as n_in, \
    open('names2.txt','w',newline='') as n_out2, \
    open('names3.txt','w',newline='') as n_out3, \
    open('scores1.txt','w',newline='') as s_out1, \
    open('scores2.txt','w',newline='') as s_out2:

    r1 = csv.reader(n_in)
    w2 = csv.writer(n_out2)
    w3= csv.writer(n_out3)
    s1 = csv.writer(s_out1)
    s2 = csv.writer(s_out2)
    for row in r1:
        dept = random.choice(['SALES', 'IT', 'HR', 'MKTG', 'OP'])
        score = random.randint(1,100)
        curr_id += random.randint(1,5)
        w2.writerow([f'{curr_id:04}',row[0],row[1],dept])
        w3.writerow([row[0],row[1],f'{curr_id:04}',dept])
        if random.random() > .5:
            s1.writerow([f'{curr_id:04}',str(score)])
            s2.writerow([row[0],row[1],f'{curr_id:04}',str(score)])

for name in ['names1', 'names2', 'names3', 'scores1', 'scores2']:
    lines = open(name+'.txt').readlines()
    random.shuffle(lines)
    open(name+'.txt', 'w').writelines(lines)
