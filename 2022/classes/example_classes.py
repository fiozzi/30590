# -*- coding: utf-8 -*-

import datetime
import person as p
import configparser
import os

config = configparser.ConfigParser()
config_file = os.path.join(os.getcwd(),'example_classes.ini')
if os.path.exists(config_file):
    config.read(config_file)
    dateformat = config['DEFAULT']['dateformat']
else:
    dateformat = '%Y%m%d'

p1 = p.Person(
    first_name='Mickey', 
    last_name='Mouse', 
    birth_date=datetime.datetime.strptime('19300113',dateformat))
p2 = p.Person(
    first_name='Donald', 
    last_name='Duck', 
    birth_date=datetime.datetime.strptime('19380207',dateformat))
e1 = p.Employee(
    first_name='Bugs', 
    last_name='Bunny', 
    birth_date=datetime.datetime.strptime('19400727',dateformat),
    dept='Sales',
    salary=1000)

print(p1)
print(p1.age())

print(p2)
print(p2.age())
p2.first_name = 'Daffy'
p2.birth_date = datetime.datetime.strptime('19370417',dateformat)

print(e1)

persons = []
persons.append(p1)
persons.append(p2)
employees = []
employees.append(e1)

print('\n'.join(map(str,persons)))
print('\n'.join(map(str,employees)))
print(e1.age())

