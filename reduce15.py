from functools import reduce
numbers=[55,66,77,88,99]
result=reduce(lambda x,y:x*y,numbers)
print(result)