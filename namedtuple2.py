from collections import namedtuple
Student=namedtuple("Student",["name","age","marks"])
s1=Student("Naveen",22,89)
print("Name:",s1.name)
print("Age:",s1.age)
print("Marks:",s1.marks)
