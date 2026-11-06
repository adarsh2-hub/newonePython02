def my_decorator(func):
    def wrapper(a,b):
        print("Addition is starting..")
        result=func(a,b)
        print("Addition is completed..")
        return result
    return wrapper
@my_decorator
def add(a,b):
    return a+b
result=add(15,25)
print(result)