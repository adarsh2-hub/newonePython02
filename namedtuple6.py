from collections import namedtuple
Student=namedtuple("Student",["name","marks1","marks2","marks3"])
s=Student("Arun",80,90,70)
average_marks=(s.marks1+s.marks2+s.marks3)/3
print("Name:",s.name)
print("Average:",average_marks)