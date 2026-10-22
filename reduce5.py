from functools import reduce
list=["Python","is","easy"]
result=reduce(lambda a,b:len(list),list)
print(result)