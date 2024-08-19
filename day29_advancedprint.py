#Creating a subroutine for colour

def red(x):
  print("\033[31m",x ,"\033[0m",sep="",end="")


def main ():
  import os
  os.system("clear")
  print("Let's print in colour!")
  print()
  x = input ("Type word you want to see in colour: ")
  print()
  red(x)
  print()
  y = input("Play again? y/n:")
  if y == "y":
    main()


main()