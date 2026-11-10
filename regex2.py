import re
text="I am 21 years old and I was admit in 2024 in my degree college"
result=re.findall(r"\d+",text)
print(result)