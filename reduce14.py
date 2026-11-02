from functools import reduce
n=[1,2,3,4,5]
r=reduce(lambda x,y:x*y,n)
print(r)