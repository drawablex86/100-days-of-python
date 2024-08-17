def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)
  return dice

## first one to reach 10
p1c = 0
p2c = 0
p1 = input("Player 1, what is your name? ")
p2 = input("Player 2, what is your name? ")
while p1c < 10 and p2c < 10:
  print(p1, "press enter to roll")
  input()
  p1r = rollDice()
  p1c += p1r
  print(p1, "you are on", p1c)
  print(p2, "press enter to roll")
  input()
  p2r = rollDice()
  p2c += p2r
  print(p2, "you are on", p2c)
  if p1c >= 10:
    print(p1, "wins!")
  elif p2c >= 10:
    print(p2, "wins!")