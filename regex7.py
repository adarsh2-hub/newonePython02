import re
text="I love 2 books, 5 pens and 10 pencils."
result=re.findall(r"\d+",text)
print(result)