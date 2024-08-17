
# Subroutine to create character name and type
def character():
  name = input("what is the name of your character?:")
  type = input("what is the type of your character? Human/Wizard etc: ")
  return name, type

#Subroutine that multiplies bunch of random dice rolls to generate health status
def health():
  import random
  sixDice = random.randint(1,6)
  eightDice = random.randint(1,8)
  h = ((sixDice * eightDice)/2)+10
  return h

#Subroutine that multiplies bunch of random dice rolls to generate strength status
def strength():
  import random
  sixDice = random.randint(1,6)
  eightDice = random.randint(1,8)
  s = ((sixDice * eightDice)/2)+12
  return s

#actual main function
def main():
  print()
  print("Character Builder 2.0")
  print("************************")
  print()
  name, type = character()
  h = health()
  s = strength()
  print("The character", name, "and is a", type, " with a HP", h, "& SP", s)
  print()
  condition = input("Do you want to create another character?y/n: ")
  if condition == "y":
    main()
  print()
  print("Thanks for using the generator")
  print("-------Made by Rahul--------")


main()


# Learned that you cannot use a variable used in subroutine in another subroutine without declaring it's value associtation here.
# It is best not use the same names for variables and the subroutine that returns the value to those variables.
# eg health = health() will not work.