print ("Guess the lyrics")
print ("-----")
print("see if you can find the missing word in the lyrics")
word = input("Never going to ____ you up!   > ")
while True:
  if word == "give":
    print("correct!")
    break
  else:
    print()
    print("wrong! try again")
    print()
    word = input("Never going to ____ you up!   >")
    print()