import re
text="I     am     learning     something        new"
result=re.sub(r'\s+',' ',text)
print("Cleaned Text is:",result)