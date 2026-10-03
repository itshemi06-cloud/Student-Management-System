print("===Student Management System===")
student =[]
while True:
    print("1. add student name")
    print("2. View student details")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")

        student.append({
            "name": name,
            "age": age,
            "course": course
        })
        print("student added successfully!")

    elif choice == "2":
        if student:
                    print ("Student details")
                    for s in student:
                        print("name :",s["name"])
                        print("age :",s["age"])
                        print("course :",s["course"])
                        print()
                    else:
                     print("No student added yet.")

    elif choice == "3":
        print("Thank you! Program closed.")
        break

    else:
        print("Invalid choice")

        