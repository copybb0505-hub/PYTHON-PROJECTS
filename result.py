name = input("Student name: ")

maths = int(input("maths marks:"))
statistics = int(input("statistics marks: "))
economics = int(input("economics marks: "))

total = maths + statistics + economics
percentage = total / 3

print("\nStudent name:" , name)
print("Total:" , total)
print("percentage:" , percentage)

if percentage >=50:
    print("Result: Pass")
else:
    print("Result: fail")