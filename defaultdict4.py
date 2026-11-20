from collections import defaultdict
word_count=defaultdict(int)
sentence="python java python c++ java python"
words=sentence.split()
for word in words:
    word_count[word]+=1
for word,count in word_count.items():
    print(f"{word}:{count}")