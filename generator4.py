def positive_numbers(numbers):
    for num in numbers:
        if num>0:
            yield num
numbers=[-5,10,-2,8,0,15]
for number in positive_numbers(numbers):
    print(number)