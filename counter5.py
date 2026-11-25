from collections import Counter
numbers=[10,20,10,30,20,10,40,20,30,50]
count=Counter(numbers)
common=count.most_common(3)
print(common)