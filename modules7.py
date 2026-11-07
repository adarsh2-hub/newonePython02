import os
print("Current Directory:",os.getcwd())
print("Files and Folders:",os.listdir())
if os.path.exists("Python"):
    print("Folder exists")
else:
    print("Folder does not exist")