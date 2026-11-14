import multiprocessing
def parents():
    print("Parents are:-")
    parents1="Appa"
    parents2="Amma"
    print(parents1)
    print(parents2)
if __name__=="__main__":
    p=multiprocessing.Process(target=parents)
    p.start()
    p.join()