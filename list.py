students = []

for i in range (5):
    name = input("student name: " )
    marks = int(input("marks:"))

    students.append([name,marks])

    print("\nStudent list")

    for student in students:
        print(student[0],"-",student[1] )

