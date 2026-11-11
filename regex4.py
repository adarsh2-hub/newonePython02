import re
text="I am learning Python Programming"
result=re.search("Python",text)
if result:
    print("Python found!")
else:
    print("Python not found!")