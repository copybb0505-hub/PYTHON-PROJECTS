import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25/05/2025",
    database="collage"
)

cursor = conn.cursor()

cursor.execute("select * from student")

for row in cursor:
    print(row)