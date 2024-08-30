# Agenda Manager using Dynamic Lists
agenda = [] #declare the list first to use it everywhere

# Ask the user what they want to do? Add/Remove or Exit
def ask():
    userCheck =input("Would you like to add or remove something?Add/Remove/Exit\n").strip().lower()
    return userCheck

#into section code
def intro():
    print()
    border = "---------------"
    print(f"{border: ^30}")
    greet = "Welcome to My Tasks v1.0" #we are using a variable so that fstring can be used to align the print in next line
    print(f"{greet: ^30}\n{border: ^30}") #combined greeting and border end to a single line
# Based on user input, get the corresponding action done
def check():
    print()
    userCheck = ask()
    if userCheck == "add":
        userInput = input("Enter the task you would like to add: ").lower()
        agenda.append(userInput)
    elif userCheck == "remove":
        userInput = input("Enter the task you would like to remove: ").lower()
        if userInput in agenda: # Condition to check whether the removal request item is actually in the agenda list
            agenda.remove(userInput)
        else:
            print(f"{userInput}is not on your agenda")
    elif userCheck == "exit":
        exit()
    return agenda

def calendar(): #to print the final agenda to the user
    print("\nYour Agenda for the Day is:")
    print("-----------------------------")
    for i in agenda:
        print(i.title())


def main():
    import os, time
    while True:
        
        check()
        time.sleep(1)
        os.system("clear")
        calendar()

intro()
main()