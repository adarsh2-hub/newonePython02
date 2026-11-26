from collections import OrderedDict
student=OrderedDict()
student["name"]="Adarsh"
student["age"]=21
student["course"]="BCA"
student.move_to_end("name")
print(student)