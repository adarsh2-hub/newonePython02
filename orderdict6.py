from collections import OrderedDict
stud=OrderedDict()
stud["name"]="Abhishek"
stud["age"]=23
stud["occupation"]="software"
stud.move_to_end("age")
print(stud)