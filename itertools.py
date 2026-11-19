import itertools
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[11,12,13,14,15,16,17,18,19,20]
result=itertools.chain(l1,l2)
print(list(result))