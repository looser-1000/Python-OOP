# class is created
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#         print("New Data is added into the database...")

# object is created
# s1 = Student("Salis", 97)
# print(s1.name, s1.marks)
#
# s2 = Student("Bushra", 92)
# print(s2.name, s2.marks)

# Create student class that takes name & marks of 3 subjects as an
# arguments in constructor then create a method to print the average


class Student:
    sum = 0
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.marks1 = sub1
        self.marks2 = sub2
        self.marks3 = sub3

    def avg_marks(self):
        avg = float((self.marks1 + self.marks2 + self.marks3)/3)
        return avg


s1 = Student("Bushra", 97, 87, 92)
print(s1.avg_marks())

s2 = Student("Salis", 98, 97, 92)
print(s2.avg_marks())

if s2.avg_marks() > s1.avg_marks():
    print(s2.name + " got the highest marks")
else:
    print(s1.name + " got the highest marks")

print(s2.name + " I love you")