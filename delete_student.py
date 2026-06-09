import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25/05/2025",
    database="collage"
)

cursor = conn.cursor()

id = int(input("Enter student id to delete: "))

sql = "delete from student where id=%s"
val = (id,)

cursor.execute(sql, val)
conn.commit()

print("Record deleted successfully")