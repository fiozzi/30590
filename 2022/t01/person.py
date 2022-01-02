# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:15:35 2020

@author: Iozzi
"""
import datetime

class Person:
    """
    Represents a person 
    
    >>> p1 = Person('Mickey', 'Mouse', datetime.datetime.strptime('19300113','%Y%m%d'))

    """
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        """
        Initialize a person with first/last name and birthdate

        fname, lname: String
        bdate: datetime.datetima object formatted as YYYYMMDD
        """
        
    def desc(self):
        str1 = f'{self.first_name} {self.last_name}'
        str1 = str1 + f', born on {self.birth_date}.'
        return str1
    
    def __repr__(self):
        tt = self.birth_date.timetuple()
        return (
            f'Person(first_name="{self.first_name}", '
            f'last_name="{self.last_name}", '
            f'birth_date=datetime.datetime({tt[0]}, {tt[1]}, {tt[2]})')
        
    def age(self):
        age = datetime.datetime.today() - self.birth_date
        return int(age.days // 365)
        
class Employee(Person):
    
    def __init__(self, first_name, last_name, birth_date, dept='', salary = 0):
        """
        Inizialize an employee
        """
        super().__init__(first_name, last_name, birth_date)
        self.dept = dept
        self.salary = salary

    def __repr__(self):
        tt = self.birth_date.timetuple()
        return (
            f'Employee(first_name="{self.first_name}", '
            f'last_name="{self.last_name}", '
            f'birth_date=datetime.datetime({tt[0]}, {tt[1]}, {tt[2]}), '
            f'dept="{self.dept}", '
            f'salary={self.salary})')

    def change_salary(self, delta):
        self.salary = self.salary + delta
        
if __name__ == '__main__':
    p1 = Person('Mickey', 'Mouse', datetime.datetime.strptime('19300113','%Y%m%d'))
    print(type(p1))
    print(p1)
    p2 = Person('Donald', 'Duck', datetime.datetime.strptime('19380207','%Y%m%d'))
    print(p2)
    e1 = Employee('Bugs', 'Bunny', datetime.datetime.strptime('19400727','%Y%m%d'))
    print(e1)

