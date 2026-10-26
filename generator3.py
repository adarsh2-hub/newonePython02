def even_numbers():
    for n in range(2,11,2):
        yield n
for n in even_numbers():
    print(n)