# Writing a piece of code to test out creating a program inside the terminal

import os
import random
print()
print("Welcome to Dice game")
while True:
    print() 
    x = input("Press any key to roll the dice")
    print()
    ds = random.randint(1,6)
    print("You rolled {ds}." .format(ds=ds))
    print()
    x = input("Thanks for playing, do you want to exit?y/n: \n")
    if x=="y":
        exit()
    else:
        continue

