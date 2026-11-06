def display_info(*args,**kwargs):
    total=len(args)
    print("Total Positional Arguments:",total)
    for value in args:
        print(value)
        total=len(kwargs)
        print("Total Keyword Arguments:",total)
    for key,value in kwargs.items():
        print(key,":",value)
display_info("Python","Java","HTML","CSS",
             name="Adarsh",
             age=21,
             course="BCA")