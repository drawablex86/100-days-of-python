#to create pretty print subroutine 

import os, time
emaillist = []

def prettyprint():
    os.system("clear")
    print("Here is our Email Database\n--------------")
    counter = 1
    for email in emaillist:
        print(f"{counter}. {email}")
        counter += 1
    time.sleep(1)


while True:
    print("\nWelcome to Ultimate Spammer\n")
    menu = input("Menu Options\n---------\n| 1: Add Email\n| 2: Remove Email\n| 3: Show Emails\n| 4: Start Spamming\n| 5: Exit\n")
    if menu == "5":
        exit()
    elif menu =="1":
        email = input("Enter the email id:")
        emaillist.append(email)
    elif menu =="2":
        if email in emaillist:
            emaillist.append(email)
        else:
            print(f"{email} is not in th list now!")
    elif menu =="3":
        prettyprint()
    elif menu == "4":
        print("Spamming Initiated")
    else:
        print("===Invalid Option===")
    time.sleep(1)
    os.system("clear")


