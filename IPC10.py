import multiprocessing
q=multiprocessing.Queue()
q.put("Adarsh")
print("Employee Name:",q.get())
q.put("100000")
print("Employee Salary:",q.get())