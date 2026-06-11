class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name =", self.name)
        print("Marks =",self.marks)
        print()

s1 = Student("Devam", 85)
s2 = Student("Charmi", 55)
s3 = Student("Subhdra", 86)

s1.display()
s2.display()
s3.display()