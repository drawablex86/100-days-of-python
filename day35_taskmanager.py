import os, time
tasks =[]
#Colour variables
red = "\033[91m"
green = "\033[92m"
default = "\033[0m"
yellow = "\033[93m"


# #Introduce the program
def intro():
    border = "---------------------"
    print(f"\n{border}\nUltimate Task Manager\n{border}\n")

  
#Give menu options for the user
def menubar():
    menu = input(f"== {yellow}Menu{default} ==\n\n0: Add Task\n1: Remove Task\n2: Replace Task\n3: Erase all Tasks\n4: Display all Tasks\n5: Exit\n{yellow}Enter your choice:{default} \n")
    return menu

# Print all tasks - Subroutine
def myTasks():
    os.system("clear")
    print(f"\n{green}Your Task List:\n---------------{default}")
    for index in range(len(tasks)):
        print(f"{index+1}: {tasks[index].capitalize()}")

#Add, Remove, Erase, Exit implementation with duplicate checker and double confirmatin from the user
def main():
    os.system("clear")
    global tasks
    while True:
        intro()
        menu = menubar()
        if menu == "5": #Exit
            print("Thank you for using the Ultimate Task Manager")
            time.sleep(0.5)
            print(f"Developed by {green}Rahul Rajeev{default}")
            time.sleep(3)
            os.system("clear")
            exit()
        elif menu == "4": #View All Tasks
            myTasks() #call the print subroutine
            time.sleep(3) #to keep the tasks visible
        elif menu == "3": # Erase all Tasks
            confirm = input(f"\n{red}Confirm you want to clear all tasks?{default}y/n: ").lower().strip()
            if confirm == "y":
                tasks = []
                print(f"\n{green}You have cleared all the tasks!{default}")
                time.sleep(0.5)
            elif confirm == "n":
                print(f"{green}Erase cancelled{default}")
                time.sleep(0.5)
            else:
                print("Please choose y or n")
        elif menu == "2": # Replace Task
            task = input("\nWhat is the task that you want to replace: \n").lower().strip() #converts the input to small case and strips away empty spaces in the left and right)
            if task in tasks:
                new_task = input("\nEnter the task you want to add:\t")
                # find where the task is stored
                for index in range(len(tasks)): #for loop to check each elements of lists with the task that is to be replaced
                    if tasks[index]== task: 
                        tasks[index]= new_task #replaces the task with new task
                print(f"\n{green}Task replaced{default}")
                time.sleep(0.5)
            else:
                print(f"\n{red}There is no such task!{default}") #Invalid task
        elif menu == "1": #Remove task
            task = input("\nEnter the task that you want to remove:\n").lower().strip()
            if task in tasks:
                confirm = input(f"\n{red}Confirm you want to remove {green}{task}{default}?y/n: ").lower().strip()
                if confirm == "y" :
                    tasks.remove(task)
                    print(f"\n{green}You have successfully removed the {red}{task}{default}")
                    time.sleep(0.5)
                elif confirm == "n":
                    print("\nThere is no such task!") #Invalid task
                else:
                    print("Please select y or n!")
            else:
                print("\nThere is not  such task") #invalid task
        elif menu == "0": #add task
            task = input("\nEnter the task that you want to add:\n").lower().strip()
            if task in tasks: #check for duplicity of task
                break
            else:
                tasks.append(task)
                print(f"\n{green}Task Added!{default}")
                time.sleep(0.5)
        time.sleep(0.5)
        os.system("clear")




main()


        

