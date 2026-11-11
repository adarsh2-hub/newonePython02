import re
text="My name is Adarsh and I love Python"
result=re.search("Adarsh",text)
if result:
    print("Name Found!")
else:
    print("Name Not Found!")