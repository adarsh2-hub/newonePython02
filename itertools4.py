import itertools

languages = ["Python", "Java", "C++"]

cycle = itertools.cycle(languages)

for i in range(9):
    print(next(cycle))