class Person:

    def show(self):
        print("I am a Person")

class student(Person):

    def show(self):
        print("I am a Student")

s1 = student()

s1.show()