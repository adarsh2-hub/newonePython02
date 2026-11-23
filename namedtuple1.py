from collections import namedtuple
Student=namedtuple("student",["name","age","course"])
s1=Student("Rahul",21,"BBA")
print(s1.name)
print(s1.age)
print(s1.course)