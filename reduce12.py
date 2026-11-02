from functools import reduce
words=["Python","is","very","interesting.."]
result=reduce(lambda x,y:x+" "+y,words)
print(result)