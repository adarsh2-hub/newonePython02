def total(num):
    if num==1:
        return 1
    return num+total(num-1)
result=total(7)
print(result)