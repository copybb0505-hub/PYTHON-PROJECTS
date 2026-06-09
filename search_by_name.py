import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25/05/2025",
    database="collage"
)

cursor = conn.cursor()

name = input("Enter Student name: ")

sql = "Select * from student where name=%s"
val = (name,)

cursor.execute(sql, val)

record = cursor.fetchone()

if record:
    print("Student Found ")
    print("ID:",record[0])
    print("name:",record[1])
    print("Marks:",record[2])

else:
    print("Student Not Found")