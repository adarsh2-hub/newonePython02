def my_decorator(func):
    def wrapper(a,b):
        print("Addition is starting..")
        result=func(a,b)
        print(result)
        print("Addition is completed..")
    return wrapper 
@my_decorator
def add(a,b):
    return a+b
add(30,40)