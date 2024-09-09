import os
import time

taskDB = []

def addTask():
    task = input("Enter the task: ")
    dueDate = input("Enter the due date: ")
    priority = input("Select Priority - High, Medium, Low: ").lower().strip()
    row = [task, dueDate, priority]
    taskDB.append(row)

def prettyPrint(row):
    for item in row:
        print(item, end="\t:\t")
    print()

def printPriority(priority):
    found = False
    for row in taskDB:
        if row[2] == priority:
            prettyPrint(row)
            found = True
    if not found:
        print(f"\nYou have no {priority} priority tasks")

def removeTask():
    task = input("Enter the task you want to remove: ")
    for row in taskDB:
        if task == row[0]:
            taskDB.remove(row)
            print("Task removed successfully")
            return
    print("\nThis task doesn't exist")

def editTask():
    task = input("Enter the task you want to edit: ")
    for row in taskDB:
        if task == row[0]:
            whatEdit = input("Edit task(1), date(2), priority(3): ")
            if whatEdit == "1":
                row[0] = input("Edit Task: ")
            elif whatEdit == "2":
                row[1] = input("Edit Date: ")
            elif whatEdit == "3":
                row[2] = input("Edit Priority: ")
            else:
                print("\nInvalid Input")
            return
    print("\nTask does not exist")

def main():
    while True:
        os.system("clear")
        print("Task Manager")
        print("\nMenu\n--------")
        print("1. Add(1)\n2. View\n3. Edit\n4. Remove\n5. Exit")
        choice = input("Your choice(1-5): ")
        
        if choice == "1":  # Add Task
            addTask()
        elif choice == "2":  # View Tasks
            view = input("View all Tasks(a)\nView based on Priority(b): ").lower().strip()
            if view == "a":
                for row in taskDB:
                    prettyPrint(row)
            elif view == "b":
                priority = input("Select: High, Medium, or Low: ").lower().strip()
                printPriority(priority)
            else:
                print("Invalid input!")
        elif choice == "3":  # Edit task
            editTask()
        elif choice == "4":  # Remove task
            removeTask()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("\nEnter a valid choice")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()