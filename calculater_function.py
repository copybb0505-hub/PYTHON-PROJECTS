def add(a, b):
    return a + b

def subtract(a, b):
    return a -b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Addition =", add(a, b))
print("Subtracation =",subtract(a, b))
print("Multiplication =",multiply(a, b))
print("division =",divide(a, b))