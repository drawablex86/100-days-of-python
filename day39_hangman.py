import os, time, random
words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "keyboard", "software", "challenge", "learning"]
word = random.choice(words)
letterpicked = []
result = []
lives = 6
while True:
    print("\nWELCOME TO HANGMAN\n***************")
    letter = input("\nEnter a letter:").lower()
      # Check if the input is a single letter
    if len(letter) != 1 or not letter.isalpha():
        print("\nPlease enter only one letter.")
        continue

    # to check if the user have already entered the letter before
    if letter in letterpicked:
            print("\nYou tried that already")
            continue
    
    # add the users' input to the letterpicked string
    letterpicked.append(letter)

    if letter in word:
        print("\nYou have found a letter")
    else:
        print("\n Try again!")
        lives -= 1
   # Simple way to do this:
   # Use a for loop to compare the letters in letterpicked with the letters in word
    allLetters = True
    for i in word: #each letter extracted from the word
        if i in letterpicked: #if letter extracted in this is cycle is among the words you have already picked
            print(i, end="") #print that letter. 
        else:
            print("_",end="")
            allLetters = False

    if allLetters:
        print(f"\nYou have won the game with {lives} lives remaining")
        break

    if lives<=0:
        print(f"\nYou ran out of lives! The answer was {word}")
        break
    else:
        print(f"\n\nOnly {lives} left")
    time.sleep(3)
    os.system("clear")