# To-Do List application

# Empty list to store tasks
tasks = []

def print_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_todo_list():
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\n===== Your To-Do List =====")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

def mark_task_done():
    view_todo_list()
    if tasks:
        try:
            task_index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                print(f"Task '{tasks[task_index]}' marked as done.")
                tasks.pop(task_index)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid input! Please enter a valid task number.")
    else:
        print("No tasks to mark as done.")

def delete_task():
    view_todo_list()
    if tasks:
        try:
            task_index = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                print(f"Task '{tasks[task_index]}' deleted.")
                tasks.pop(task_index)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid input! Please enter a valid task number.")
    else:
        print("No tasks to delete.")

# Main loop
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        view_todo_list()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")