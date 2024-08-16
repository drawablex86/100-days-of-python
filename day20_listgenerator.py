print ("Awesome List Generator")
print()
while True: #to keep playing the game
  start = int(input("Start at: "))
  end = int(input("End before: "))
  plus = int(input("Increment value: "))
  print()
  print("Here we go:")
  for i in range(start, end, plus):
    print (i)
  print ()
  print("Thank you for playing!")
  x= input("Do you want to play again? y/n: ") #conditional logic to stop or repeat the game based on user input
  if x == "y":
    continue
  else:
    exit()
