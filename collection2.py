from collections import Counter
colors=["Red","Blue","Red","Green","Blue","Red","Yellow","Blue"]
result=Counter(colors)
result.most_common(2)
print(result)