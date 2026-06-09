while True:
    print("\n===== Student Managaement System =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Add Student Selected")

    elif choice == 2:
        print("View Student Selected")

    elif choice == 3:
        print("Update Student Selected")

    elif choice == 4:
        print("Delete Student Selected")

    elif choice == 5:
       print("Thank you!")
       break

    else:
        print("Invalid choice") 