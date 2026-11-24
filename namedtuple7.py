from collections import namedtuple
e=namedtuple("e",["name","salary"])
e1=e("Rahul",25000)
e2=e("Priya",35000)
e3=e("Arun",30000)
e=[e1,e2,e3]
highest=max(e,key=lambda e:e.salary)
print("Highest Paid Employee:-",highest.name)
print("Highest salary:-",highest.salary)