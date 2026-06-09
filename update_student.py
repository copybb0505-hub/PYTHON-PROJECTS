import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25/05/2025",
    database="collage"
)

cursor = conn.cursor()

id = int(input("Enter student id: "))
new_marks = int(input("enter new marks: "))

sql = "Update student set marks=%s where id=%s"
val = (new_marks, id)

cursor.execute(sql,val)
conn.commit()

print("Record Updated Successfully")