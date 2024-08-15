from getpass import getpass as input
print ("WELCOME TO ROCK PAPER SCISSORS - BATTLE ULTIMATUM")
print ("----")
p1score = 0
p2score = 0
while True:
  print()
  print ("Select your move (R, P or S)")
  print("******")
  p1 = input("Player 1 > ")
  p2 = input ("Player 2 > " )
  if (p1 == "R" or p1 == "P" or p1 == "S") and (p2 == "R" or p2 == "P" or p2 == "S"):
    
    if p1 == "R" and p2 == "R":
      print ("You rock heads have tied!")
    elif p1 == "P" and p2 == "P":
      print ("Paper fans have tied!")
    elif p1 == "S" and p2 == "S":
        print ("Scissoring only gets you a tie")
    elif p1 == "R" and p2 == "P":
      print ("Paper covers rock, player 2 wins!")
      p2score += 1
    elif p1 == "R" and p2 == "S":
      print ("Rock smashes scissors, player 1 wins")
      p1score += 1
    elif p1 == "P" and p2 == "R":
      print ("Paper covers rock, player 1 wins!")
      p1score += 1
    elif p1 == "P" and p2 == "S":
      print ("Scissors cuts paper, player 2 wins!")
      p2score += 1
    elif p1 == "S" and p2 == "R":
      print ("Rock smashes scissors, player 2 wins!")
      p2score += 1
    elif p1 == "S" and p2 == "P":
      print ("Scissors cuts paper, player 1 wins!")
      p1score += 1
    print ("Player 1:", p1score, "and Player 2:", p2score,)
    if p1score == 3:
      print ("Player 1 has won the tournament. Thanks for playing!")
      exit()
    elif p2score == 3:
      print ("Player 2 has won the tournament. Thanks for playing!")
      break
  else: 
    print ("Please enter a valid move")

  
    
  