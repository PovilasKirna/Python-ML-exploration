
#python OOP 06 Corey Schafer

class Employee:

    num_of_emps = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):           #Constructor
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1                   #constant class variable (for whole class)

    @property
    def email(self):  # method
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self): #method
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Name deleted!")
        self.first = None
        self.last = None



    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount


emp1 = Employee("Corey", "Last", "60000")
emp2 = Employee("Name", "Last2", "70000")

# emp1.fullname = "John Schafer"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
