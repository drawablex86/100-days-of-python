print("Guess the number challenge")
print()
print("The object of the game is for you to guess correctly my favourite number")
print()
print("You will be given hints to help you along the way")
print("Number will be between 1 and 1,000,000")
print()
print("Player with the least amount of guesses wins!")
print()
print("****Let's start****")
myNum = 10000
counter = 0
while True:
  guess = int(input("What is your guess?: "))
  if guess == 10000:
    counter += 1
    print("You have correctly guessed in", counter, "chances!")
    break
  elif guess < 10000 and guess >= 1:
    counter += 1
    print("Too low")
    continue
  elif guess > 10000 and guess <= 1000000:
    counter += 1
    print("Too high")
    continue
  elif guess > 1000000 or guess ==0:
    print("I said between 1 and 1,000,000")
    continue
  else:
    print("You are trying to be clever, I am done with you")
    exit()