students=["Gajanana","Gagan","Acharya","Priya"]
marks=[85,92,78,96]
highest=0
highest_index=0
for index,mark in (enumerate(marks)):
    if mark>highest:
        highest=mark
        highest_index=index
print(f"{students[highest_index]} scored {highest} at index {highest_index}.")