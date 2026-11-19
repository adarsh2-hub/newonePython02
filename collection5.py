from collections import Counter
marks=[85,90,75,85,90,85,70,75,90,85]
count=Counter(marks)
print(count)
result=count.most_common(1)
print(result)
print(count.most_common(3))