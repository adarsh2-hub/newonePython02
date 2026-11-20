from collections import defaultdict
grades=defaultdict(list)
students=[
    ("Adarsh","A"),
    ("Rahul","B"),
    ("Kiran","A"),
    ("Arjun","B"),
    ("Ravi","A")
]
for name,grade in students:
    grades[grade].append(name)
for grade,names in grades.items():
    print(f"{grade}:{names}")