for i in range(1,11):
    if i%3==0:
        continue
    if i==8:
        break
    if i==5:
        pass
    print(i)