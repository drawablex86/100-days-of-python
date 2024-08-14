from getpass import getpass as input
print ("WELCOME TO ROCK PAPER SCISSORS - BATTLE ULTIMATUM")
print ("----")
condition = "no"
while condition == "no": # to keep the game running if the user gives an invalid input
  print()
  print ("Select your move (R, P or S)")
  print("******")
  p1 = input("Player 1 > ")
  p2 = input ("Player 2 > " )
  if (p1 == "R" or p1 == "P" or p1 == "S") and (p2 == "R" or p2 == "P" or p2 == "S"):
    condition = "yes"
    if p1 == "R" and p2 == "R":
      print ("You rock heads have tied!")
    elif p1 == "P" and p2 == "P":
      print ("Paper fans have tied!")
    elif p1 == "S" and p2 == "S":
        print ("Scissoring only gets you a tie")
    elif p1 == "R" and p2 == "P":
      print ("Paper covers rock, player 2 wins!")
    elif p1 == "R" and p2 == "S":
      print ("Rock smashes scissors, player 1 wins")
    elif p1 == "P" and p2 == "R":
      print ("Paper covers rock, player 1 wins!")
    elif p1 == "P" and p2 == "S":
      print ("Scissors cuts paper, player 2 wins!")
    elif p1 == "S" and p2 == "R":
      print ("Rock smashes scissors, player 2 wins!")
    elif p1 == "S" and p2 == "P":
      print ("Scissors cuts paper, player 1 wins!")
  else:
    print ("Invalid move, try again")  
    condition = "no"
 