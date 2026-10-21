words=["madam","hello","level","python","radar"]
result=list(filter(lambda words:words[::-1]==words,words))
print(result)