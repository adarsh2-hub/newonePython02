def calculate(*args,**kwargs):
    total=sum(args)
    print("Sum:",total)
    print("Personal Details:")
    for key,value in kwargs.items():
        print(key,":",value)
calculate(10,20,30,40,
          name="Adarsh",
          course="BCA",
          city="Kumta")