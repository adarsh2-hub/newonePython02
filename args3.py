def student_details(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
student_details(name="Adarsh",
                age=21,
                course="BCA",
                college="Government First Grade College Honnavar"
                )