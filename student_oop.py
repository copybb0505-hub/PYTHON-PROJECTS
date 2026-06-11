class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name =", self.name)
        print("Marks =",self.marks)

s1 = Student("Devam", 85)
s2 = Student("Charmi", 55)

s1.display()
print()

s2.display()