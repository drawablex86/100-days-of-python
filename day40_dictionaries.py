# testing it out
import os, time
while True:
    myUser = {"name":"", "age":"", "email id":""}
    print("Let's try Dictionaries of Python\n**********************\n")
    myUser["name"]= input("Enter your name: ")
    myUser["age"] = input("Enter your age: ")
    myUser["email id"] = input("Enter you email id: ")


    print(f"\n Your name is {myUser['name']} and you are {myUser['age']} years old and your email id is {myUser['email id']}.")
    time.sleep(3)
    os.system("clear")
