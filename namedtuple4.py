from collections import namedtuple
student=namedtuple("student",["name","age","marks"])
s1=student("Ravi",20,76)
print("Name:",s1.name)
print("Age:",s1.age)
print("Marks:",s1.marks)