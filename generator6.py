def vowels(word):
    for ch in word:
        if ch in "aeiou":
            yield ch
word="education"
for ch in vowels(word):
    print(ch)