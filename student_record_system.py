def add_student():
    file = open("student.txt", "a")

    name = input("Enter name: ")
    marks = input("Enter marks: ")

    file.write(name + " - " + marks + "\n")

    file.close()

    print("Student Added Successfully")

def view_student():
    file = open("student.txt", "r")

    data = file.read()

    print("\nStudent records")
    print(data)

    file.close()

while True:

    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_student()

    elif choice == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")