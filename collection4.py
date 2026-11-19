from collections import Counter
sentence="python is easy python is powerful python"
words=sentence.split()
result=Counter(words)
print(result.most_common(2))
