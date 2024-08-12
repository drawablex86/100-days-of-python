print ("Welcome to TiCalc - The Tip Calculator")
myBill = float(input("What was the bill?: $ "))
tip = int(input("What percentage tip would you like to leave? 15/18/20:  "))
numberOfPeople = int(input("How many people are you?: "))
total = myBill * (1 + tip/100)
answer = total / numberOfPeople
answer = round (answer, 2)
print("You all owe", "$",answer)