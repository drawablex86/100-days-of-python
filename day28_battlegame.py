#Day 28 Challenge
# h= orc x6, human x5, wizard x2, elf x2
# s = orc x2, human x3, wizard x4, elf x4

def getChara():
  import random
  print("Let's create your champion!")
  c1Name = input("Player 1: ")
  c1Type = input("Type (Human, Elf, Wizard, Orc): ")
  print()
  c2Name = input("Player 2: ")
  c2Type = input("Type (Human, Elf, Wizard, Orc): ")
  print()
  if (c1Type != "Human" and c1Type != "Elf" and c1Type != "Wizard" and c1Type != "Orc")\
  or (c2Type != "Human" and c2Type != "Elf" and \
    c2Type != "Wizard") and c2Type != "Orc":
    print("Invalid character type. Please try again. Check case")
    print()
    getChara() 
  return c1Name, c1Type, c2Name, c2Type

def rollDice():
  import random
  dice = random.randint(1,6)
  return dice

def main():
  import os
  import time
  print ("Welcome to Giga Battle World")
  print("******************************")
  print("Created by Rahul Rajeev")
  print()
  c1Name, c1Type, c2Name, c2Type = getChara()
  print()
  os.system("clear") # clear the stage so far
  x = input("Press any key set the battle stats for your characters")
  # Setting Stats
  h1 = 0
  h2 = 0
  s1 = 0
  s2 = 0
  # character 1
  d1 = rollDice()
  if c1Type == "Human":
    h1 = d1*5
    s1 = d1*3
  elif c1Type == "Orc":
    h1 = d1*6
    s1 = d1*2
  elif c1Type == "Wizard": 
    h1 = d1*2
    s1 = d1*4
  elif c1Type == "Elf":
    h1 = d1*2
    s1 = d1*4
  print()
  # Character 2
  d2 = rollDice()
  if c2Type == "Human":
    h2 = d2*5
    s2 = d2*3
  elif c2Type == "Orc":
    h2 = d2*6
    s2 = d2*2
  elif c2Type == "Wizard":
    h2 = d2*2
    s2 = d2*4
  elif c2Type == "Elf":
    h2 = d2*2
    s2 = d2*4
  # Print Player stats
  print()
  print("--------------------------------")
  print("Player 1 Stats")
  print(c1Type," - ",c1Name)
  print("Health: ",h1)
  print("Strength:",s1)
  print("--------------------------------")
  print("--------------------------------")
  print("Player 2 Stats")
  print(c2Type," - ",c2Name)
  print("Health: ",h2)
  print("Strength:",s2)
  print("--------------------------------")
  print ()
  # Damage Algorithm
  diff = abs(s1-s2)
  dmg = diff+1
  x = input("Press any key to start the battle")
  os.system("clear")
  print("***** Battle Begins ******")
  counter = 0
  while True:
    time.sleep(3)
    os.system("clear")
    print()
    counter += 1
    print("Round", counter)
    # Roll Dice - highest wins the round
    dc1 = rollDice()
    dc2 = rollDice()
    if dc1 > dc2:
      print (c1Name, "has won this round!")
      print (c1Name,"attacks" ,c2Name, "with full force!")
      # Apply the damage to player 2
      print()
      h2 = h2 - dmg
      print (c2Name, "has only", h2, "health left")
      if h2 <= 0:
        print(c1Name,"has won the epic battle")
        print()
        print("Tough Luck",c2Name)
        break
    elif dc2 > dc1:
      print (c2Name, "has won this round!")
      print (c2Name,"attacks" ,c1Name, "with full force!")
      # Apply the damage to player 1
      h1 = h1 - dmg
      print()
      print (c1Name, "has only", h1, "health left")
      if h1 <= 0:
        print(c2Name,"has won the epic battle")
        print()
        print("Tough Luck",c1Name)
        break
    else:
      print ("This round has been tied")
      continue
  print()
  print("Thanks for playing")
  condition = input("Do you want to play again? (y/n): ")
  if condition == "y":
    main()
  else:
    exit()




main()
  
  
  