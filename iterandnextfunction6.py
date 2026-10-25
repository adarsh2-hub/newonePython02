numbers=[12,24,36,48]
num=iter(numbers)
while True:
    try:
        numbers=next(num)
        print(numbers)
    except StopIteration:
        break
