
#python OOP 01 Corey Schafer

class Employee:

    def __init__(self, first, last, pay):           #Constructor

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):                             #method
        return f'{self.first} {self.last}'


emp1 = Employee("Corey", "Last", "60000")
emp2 = Employee("Name", "Last2", "70000")


print(Employee.fullname(emp2))

print(emp1.fullname())