#student marks analyzer project
stud1={"name":"Adarsh"}
stud1_marks=[98,99,97,88,90]
stud2={"name":"Abhishek"}
stud2_marks=[99,98,97,96,95]
stud1_total_marks=sum(stud1_marks)
stud2_total_marks=sum(stud2_marks)
average_marks1=len(stud1_marks)/sum(stud1_marks)
average_marks2=len(stud2_marks)/sum(stud2_marks)
print(f"student1 total marks is:{stud1_total_marks} \nand student2 total marks is:{stud2_total_marks}\nstudent1 average marks is:{average_marks1} \nand student2 average marks is:{average_marks2}")
print(f"maximum marks is: {max(stud1_marks)} and {max(stud2_marks)}")
print(f"minimum marks is: {min(stud1_marks)} and {min(stud2_marks)}")