import multiprocessing
q=multiprocessing.Queue()
q.put("Python")
q.put("Java")
print(q.get())
print(q.get())