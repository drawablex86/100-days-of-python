#to create pretty print subroutine 

import os, time
emaillist = []

def prettyprint():
    os.system("clear")
    print("Here is our Email Database\n--------------")
    for index in range(len(emaillist)): #using index and len to set the range for the for loop
        print(f"{index+1}. {emaillist[index]}") #index + 1 to set the counter to start from 1 when displaying results
    time.sleep(1)

def spam(): #spamming subsroutine
    for index in range(len(emaillist)):
        print(f"Dear, {emaillist[index]}")
        print("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        print("Nullam auctor, nunc id aliquam tincidunt, nisl nunc tincidunt nunc,")
        print("vitae aliquam nunc nunc vitae nunc. Sed euismod, nunc id aliquam")
        print("tincidunt, nisl nunc tincidunt nunc, vitae aliquam nunc nunc vitae nunc.")
        time.sleep(2)
        os.system("clear")



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
        print("Spamming Initiated\n")
        time.sleep(0.5)
        os.system("clear")
        spam()
    else:
        print("===Invalid Option===")
    time.sleep(1)
    os.system("clear")


