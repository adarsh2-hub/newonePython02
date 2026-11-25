from collections import Counter
fruits=["apple","banana","apple","orange","banana","apple","mango","banana"]
result=Counter(fruits)
common=result.most_common()
print("Most common fruits is:",common)
print("Count:",result)