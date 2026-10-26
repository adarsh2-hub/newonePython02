def numbers():
    yield 10
    yield 20
    yield 30
    yield 40
result=numbers()
print(next(result))
print(next(result))
print(next(result))
print(next(result))