from functools import reduce
numbers=[12,45,23,67,34,89,56]
result=reduce(lambda x,y:max(x,y),numbers)
print(result)