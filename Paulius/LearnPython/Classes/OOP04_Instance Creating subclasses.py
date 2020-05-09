
#python OOP 04 Corey Schafer

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



class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #inheriting parent instances
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) #inheriting parent instances
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'--{emp.fullname()}')


    raise_amount = 1.1

emp1 = Developer("Corey", "Last", "60000", "Python")
emp2 = Developer("Name", "Last2", "70000", "Java")

print(help(Developer))

man1 = Manager("name", "last", "30000", [emp1])
man1.add_emp(emp2)

# man1.print_emps()


print(isinstance(man1, Manager))
print(isinstance(man1, Developer))

print(issubclass(Manager, Employee))
print(isinstance(Employee, Developer))