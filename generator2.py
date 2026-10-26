def count():
    yield 1
    yield 2
    yield 3
result=count()
print(next(result))
print(next(result))
print(next(result))