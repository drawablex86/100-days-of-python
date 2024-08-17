def playDice():
  import random
  random.randint(1,6)
  return random.randint(1,6)
  
def main():
  # Dice game 2.0: First person to land the same number in a row wins.
  print()
  print("*************************************************")
  print("Welcome to Awesome Dice Game 2.0")
  print("*************************************************")
  print("Author: Rahul Rajeev")
  print("---")
  print("Instructions: First person to land the same number in a row wins.")
  print("---")
  counter = 0
  p1 = input("Player 1, enter your name: ")
  p2 = input("Player 2, enter your name: ")
  print()
  print("--Let's Start the Game--")
  while True:
    print()
    counter += 1
    print("Turn", counter )
    print()
    enter = input(p1+ " Press enter to roll the dice")
    x = playDice()
    y = playDice()
    print(p1,",you rolled" ,x, "and" ,y)
    print()
    enter = input(p2+ " Press enter to roll the dice")
    x1 = playDice()
    y1 = playDice()
    print(p2,"you have rolled" ,x1, "and" ,y1)
    if x != y and x1 !=y1:
      continue
    elif x == y:
      print()
      print(p1," has won the game")
      break
    elif x1 == y1:
        print()
        print(p2," has won the game")
        print()
        break
    else:
      print("It's a tie between" ,p1, "and" ,p2)
  print()
  condition = input("Do you want to play again? y/n: ")
  if condition == "y":
    main()

  
    
      
    

  

def author(x):
  print("Created by",x)


main()
