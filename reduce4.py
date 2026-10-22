from functools import reduce
numbers=[25,10,40,5,30]
result=reduce(lambda a,b:min(a,b),numbers)
print(result)