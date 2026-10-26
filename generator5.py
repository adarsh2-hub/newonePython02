def squares():
    for num in range(1,6):
        yield num*num
for num in squares():
    print(num)