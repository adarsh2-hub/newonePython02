from functools import reduce
l=[10,20,30,40,50]
result=reduce(lambda a,b:max(l),l)
print(result)