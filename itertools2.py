import itertools
student1=["Adarsh","Rahul","Kiran"]
student2=["Arun","Manoj","Ravi"]
result=itertools.chain(student1,student2)
print(list(result))