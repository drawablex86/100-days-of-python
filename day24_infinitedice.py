# Infinitiy dice - player choses the number of sides the dice has

def main():
    print("Welcome to the Infinity Dice")
    x = int(input("How many sides for the dice?: "))
    y = rollDice(x) # value extraction
    print("You rolled", y)
    condition = input("Roll again?y/n ")
    if condition == "y)":
      main()
    else:
      exit()

def rollDice(x): 
#takes the user input x and pass it on to random function to generates a roll.
    import random
    y = random.randint(1,x)
    return y #returns the value of y to main function
      
      
main()
