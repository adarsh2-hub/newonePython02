students={
    "Adarsh":85,
    "Rahul":35,
    "Kiran":72,
    "Ravi":28,
    "Anil":90
}
result=filter(lambda item:item[1]>=40,students.items())
passed_students=dict(result)
print(passed_students)