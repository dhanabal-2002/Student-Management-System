import json

def add_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    students.append(student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully.")
def view_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        if students:
            print("\nStudent List")

            for student in students:
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Course: {student['course']}")
                print("-------------------")

        else:
            print("No students found.")

    except FileNotFoundError:
        print("No students found.")

def search_student():
    search_name = input("Enter student name to search: ")

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\nStudent found")
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Course: {student['course']}")
                return

        print("Student not found.")

    except FileNotFoundError:
        print("No students found.")

def delete_student():
    delete_name = input("Enter student name to delete: ")

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                found = True
                break

        if found:
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No students found.")

def update_student():
    update_name = input("Enter student name to update: ")

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        found = False

        for student in students:
            if student["name"].lower() == update_name.lower():

                print("\nStudent found")

                new_name = input("Enter new name: ")
                new_age = int(input("Enter new age: "))
                new_course = input("Enter new course: ")

                student["name"] = new_name
                student["age"] = new_age
                student["course"] = new_course

                found = True
                break

        if found:
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student updated successfully.")

        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No students found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")