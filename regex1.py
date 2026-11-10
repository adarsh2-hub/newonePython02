import re
text="My name is Adarsh and I am 21 years old."
result=re.findall(r"\d+",text)
print(result)