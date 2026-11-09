with open("student1.txt","r")as file:
    content=file.read()
print(content)
file.close()
if "BCA" in content:
    print("BCA Course Found!")
else:
    print("BCA Course Not Found!")