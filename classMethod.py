# class Person:
#     name = "anonymous"
#     # def __init__(self, name):
#     #      self.__class__.name = name
#     #     Person.name = name
#
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
#
# p1 = Person()
# p1.changeName("Rayhan Ahmed Khan Subir")
# print(p1.name)
# print(Person.name)
#
#
#
#
#


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def calculation(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(97, 95, 85)
print(s1.calculation())


