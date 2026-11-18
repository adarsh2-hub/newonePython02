import itertools
students=["A","B","C","D"]
for stud in itertools.combinations(students,2):
    print(stud)