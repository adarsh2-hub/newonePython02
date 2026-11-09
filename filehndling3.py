with open("student1.txt","r") as file:
    content=file.read()
    file.close()
print(content)