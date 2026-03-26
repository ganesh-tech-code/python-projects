# Simple To-Do List App
# Built to practice lists, loops, and user interaction

tasks = []

print("Welcome to your To-Do List App! 📝")

while True:
    print("\n===== MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found. Enjoy your free time! 😎")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"❌ Task '{removed_task}' removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Exiting To-Do List App... 👋")
        break

    else:
        print("Invalid choice! Please select 1-4.")