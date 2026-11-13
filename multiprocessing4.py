import multiprocessing
def student_details(name,age):
    print("Student name:",name)
    print("Student age:",age)
if __name__=="__main__":
    p=multiprocessing.Process(target=student_details,args=("Adarsh",21))
    p.start()
    p.join()
    print("This process is completed!")