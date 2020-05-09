import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = 2 * self.radius
        self.circumference = 2 * math.pi * self.radius

    def parameters(self):
        return (self.radius, self.diameter, self.circumference, self.area)

a = Circle(3)

print(a.parameters())
