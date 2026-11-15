import multiprocessing

def send_student_data(conn):

    student = conn.recv()

    print("Student Name:", student["name"])
    print("Student Age:", student["age"])
    print("Student Course:", student["course"])

    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=send_student_data,
        args=(child_conn,)
    )

    process.start()

    student = {
        "name": "Adarsh",
        "age": 21,
        "course": "BCA"
    }

    parent_conn.send(student)

    parent_conn.close()

    process.join()