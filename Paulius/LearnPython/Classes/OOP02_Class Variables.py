
#python OOP 02 Corey Schafer

class Employee:

    num_of_emps = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):           #Constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1              #constant class variable (for whole class)


    def fullname(self):                             #method
        return f'{self.first} {self.last}'


    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount


emp1 = Employee("Corey", "Last", "60000")
emp2 = Employee("Name", "Last2", "70000")

# print(Employee.__dict__)
# print(emp1.__dict__)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

print(Employee.num_of_emps)