file = open("student.txt", "a")

name = input("student name: ")
marks = input("marks : ")
file.write(name + " - " +marks + " \n")

file.close()

print("Data Saved Successfully!")