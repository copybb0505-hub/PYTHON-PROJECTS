import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="25/05/2025",
    database="collage"
)
cursor = conn.cursor()

name = input ("enter name:")
marks = int(input("enter marks:"))

sql = "insert into student(name,marks) values(%s,%s)"
val = (name,marks)

cursor.execute(sql,val)
conn.commit()

print("student added suceessfully")
        