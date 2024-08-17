# Health Stats Generator
# infinite dice subroutine
# 6 and 8 sided dice subroutine, multiply the two dice rolls together and return the value
#print health stats
# loop to create new stats

def main():
  print("Hand Health Stat Generator")
  while True:
    print()
    name = input("Enter the name of you character:")
    print()
    health = stats()
    print(name, "has", health, "health!")
    print("----------------------------")
    print()
    x = input("do you want to generate more? y/n: ")
    if x == "y":
      continue
    else:
      break
  print ("Thanks for using this Generator")
  print()
  condition = input("Want to try the infinite dice?: ") # just to test out the first subroutine of the task.
  if condition == "y":
    print()
    sides = int(input("How many sides?: "))
    roll = infDice(sides)
    print("You rolled", roll)
    print()
    print("Thanks for playing!")
  else:
    exit()
    


def stats():
  import random
  six = random.randint(1,6)
  eight = random.randint(1,8)
  health = six * eight
  return health

def infDice(sides):
  import random
  roll = random.randint(1,sides)
  return roll


main()