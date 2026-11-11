import re
sentence=int(input("Enter the sentence:"))
result=re.findall(r'[aeiouAEIOU]',sentence)
count=len(result)
print("Total Vowels:",count)