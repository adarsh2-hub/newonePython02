from functools import reduce
l=[2,3,4,5]
answer=reduce(lambda a,b:a*b,l)
print(answer)