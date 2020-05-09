
#python OOP 05 Corey Schafer

import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):           #Constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1                   #constant class variable (for whole class)


    def fullname(self): #method
        return f'{self.first} {self.last}'


    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount

    def __repr__(self):                             #for developer
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)


    def __str__(self):                              #for users
        return '{} - {}'.format(self.first, self.email)

    def __add__(self, other):
        return int(self.pay) + int(other.pay)

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("Corey", "Last", "60000")
emp2 = Employee("Name", "Last2", "70000")

print(emp1 + emp2)
print(len(emp1))
# print(repr(emp1))
# print(str(emp1))

# print(emp1.__repr__())      #same shit as ahead
# print(emp1.__str__())       #same shit as ahead
#
#
# print(1 + 3)
#
# print(int.__add__(1, 3))
# print(str.__add__('a','b'))

