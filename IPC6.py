import multiprocessing

def send_students(q):
    student1 = {
        "name": "Adarsh",
        "age": 21,
        "course": "BCA"
    }

    student2 = {
        "name": "Rahul",
        "age": 22,
        "course": "BCA"
    }

    student3 = {
        "name": "Kiran",
        "age": 20,
        "course": "BCA"
    }

    students = [student1, student2, student3]

    for student in students:
        q.put(student)

if __name__ == "__main__":
    q = multiprocessing.Queue()

    p = multiprocessing.Process(
        target=send_students,
        args=(q,)
    )

    p.start()

    print("Student Details:\n")

    for i in range(3):
        student = q.get()

        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print()

    p.join()