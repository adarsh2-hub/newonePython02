def num():
    yield 11
    yield 22
    yield 33
    yield 44
    yield 55
result=num()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))