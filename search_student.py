import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25/05/2025",
    database="collage"
)
cursor = conn.cursor()

id = int(input("Enter Student Id: "))

sql = "select * from student where id=%s"
val = (id,)

cursor.execute(sql, val)

record = cursor.fetchone()

if record:
 print("Student found")
 print("Id:", record[0])
 print("Name:",record[1])
 print("Marks:",record[2])

else:
 print("Student Not Found")