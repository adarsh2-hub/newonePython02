try:
    with open("marks.txt","r") as file:
        contents=file.read()
except:
    FileNotFoundError
    print("File not Found!..")