from functools import reduce
list=[12,45,23,67,34]
result=reduce(lambda a,b:max(a,b),list)
print(result)