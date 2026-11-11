import re
sentece=input("Enter the sentence:")
cleaned=re.sub(r'\s+',' ',sentece)
print("Cleaned Sentences:",cleaned)