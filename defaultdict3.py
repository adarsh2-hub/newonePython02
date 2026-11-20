from collections import defaultdict
subjects=defaultdict(set)
subjects["BCA"].add("Python")
subjects["BCA"].add("Java")
subjects["BCA"].add("Python")
subjects["MCA"].add("Java")
subjects["MCA"].add("C++")
print(subjects)