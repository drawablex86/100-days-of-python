import time #for using the time function
print("How many seconds are there in a year")
print("----")
logic = input("do you wanna know the answer? y/n >  ")
print("----")
if logic == "n":
  print("Suit yourself!")
elif logic == "y":
  print("Calculating...!")
  time.sleep(2)  # Pause for 2 seconds
  days = 365
  hours = 24
  minutes = 60
  seconds = 60
  answer = days * hours * minutes * seconds
  print("There are", answer, "seconds in a year.")
  answer = answer + (24*60*60)
  print("But, if it is a leap year, then there are", answer, "seconds")
else :
  print("Choose y or n")