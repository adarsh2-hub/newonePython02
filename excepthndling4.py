try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    result=a/b
    print("Result:",result)
except ZeroDivisionError:
    print("Cannot Divided By Zero")
else:
    print("Division Successful!")