print ("What does the Fox say?")
print ("---")
exst = ""
while exit != "yes":
  animal = input("What animal do you like? > ")
  if animal == "cow":
    print ("A cow goes moo")
    exit = input ("do you want to exit? yes or no?: ")
  elif animal == "lemur":
    print ("A lemur goes awooga")
    exit = input ("do you want to exit? yes or no?: ")
  elif animal == "chicken":
    print ("A", animal, "goes Buck Buck!")
    exit = input ("do you want to exit? yes or no?: ")
  elif animal == "goat":
    print ("A", animal, "goes mmmmehhehehe!")
    exit = input ("do you want to exit? yes or no?: ")
  else:
    print ("I don't know that animal yet")
    exit = input("do you want to exit? yes or no?: ")