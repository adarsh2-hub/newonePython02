from functools import reduce
numbers=[45,12,78,34,19,2]
result=reduce(lambda x,y:min(x,y),numbers)
print(result)