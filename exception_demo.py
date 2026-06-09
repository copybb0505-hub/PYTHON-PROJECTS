try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter second Number: "))

    result = a / b

    print("Answer =",result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter number only")