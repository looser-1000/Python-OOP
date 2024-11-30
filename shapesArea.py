class Shapes:
    def area(self):
        pass

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return .5 * self.base * self.height

import math

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

s1 = Rectangle(4,5)
print("Area of Rectangle: ",s1.area())
s1 = Triangle(1,5)
print("Area of Triangle: ",s1.area())
s1 = Circle(3)
print("Area of Circle: ",f"{s1.area():.2f}")

s2 = Triangle(3,6)
print("Area of Triangle: ", s2.area())

s3 = Circle(5)
print("Area of Circle: ", f"{s3.area():.2f}")



