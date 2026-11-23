from collections import namedtuple
s=namedtuple("s",["name","age","marks"])
s1=s("Adarsh",21,98)
print("Name:",s1.name)
print("Age:",s1.age)
print("Marks:",s1.marks)