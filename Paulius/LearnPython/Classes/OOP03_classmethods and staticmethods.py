
#python OOP 03 Corey Schafer

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


    def fullname(self):                             #method
        return f'{self.first} {self.last}'


    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)                #alternative contructor

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


str1 = "Name-Last-40000"


emp1 = Employee("Corey", "Last", "60000")
emp2 = Employee("Name", "Last2", "70000")

new_emp1 = Employee.from_string(str1)
emp1.set_raise_amt(1.05)

my_date = datetime.date(2020, 5, 10)
print(Employee.is_workday(my_date))

print(new_emp1.pay)


