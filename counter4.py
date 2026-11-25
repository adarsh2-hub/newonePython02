from collections import Counter
text="python is easy and python is powerful"
words=text.split()
result=Counter(words)
print(result)