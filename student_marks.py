# Student Grade System
# I built this to understand conditions, loops, and handling multiple inputs

students = []

while True:
    print("\n===== STUDENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        # deciding grade based on marks
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"

        # storing student data
        students.append([name, marks, grade])
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for i in range(len(students)):
                print("Name:", students[i][0],
                      "| Marks:", students[i][1],
                      "| Grade:", students[i][2])

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Please try again.")