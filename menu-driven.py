import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25/05/2025",
    database="collage"
)

cursor = conn.cursor()

while True:
    print("\n===== Student Managaement System =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
       name = input("Enter name: ")
       marks = int(input("Enter marks: "))

       sql = "insert into student(name, marks) values (%s, %s)"
       val = (name, marks)

       cursor.execute(sql, val)
       conn.commit()

       print("Student Added Sucessfully")

    elif choice == 2:
        cursor.execute("SELECT * from student")
        records = cursor.fetchall()

        for row in records:
            print(row)

    elif choice == 3:
        id = int(input("Enter Student id: "))
        new_marks = int(input("Enter new marks: "))

        sql = "update student set marks=%s where id=%s"
        val = (new_marks, id)

        cursor.execute(sql, val)
        conn.commit()

        print("Record Updated successfully")

    elif choice == 4:
        id = int(input("Enter Student id to delete: "))

        sql = "DELETE FROM student where id=%s"
        val = (id,)

        cursor.execute(sql, val)
        conn.commit()

        print("Record Deleted Suceesfully")

    elif choice == 5:
       print("Thank you!")
       break

    else:
        print("Invalid choice")   