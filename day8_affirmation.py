userName = input("Hey what is your name? >  ")
date = input("Hello " + userName + "!" + " What is the day today? >")
favThing = input("What is your favorite thing to do? > ")
monA = "Today is a fresh start. You are capable of achieving great things this week."
tueA = "You embrace new challenges and grow stronger with each experience."
wedA = "Your efforts are paying off. You are making progress towards my goals."
thurA = "You choose positivity and spread kindness in all your interactions today."
friA = "You will celebrate your accomplishments, big and small, from this week."
satA = "You deserve rest and relaxation. You will recharge yourself for the week ahead"
sunA = "You are grateful for all the blessings in your life. "
sunA += "You look forward to a new week of opportunities."

if date == "Monday" or date == "monday" or date == "MONDAY":
    print("Hey " + userName +"! " + monA)
elif date == "Tuesday" or date == "tuesday" or date == "TUESDAY":
    print("Hey " + userName +"! " + tueA)
elif date == "Wednesday" or date == "wednesday" or date == "WEDNESDAY":
    print("Hey " + userName +"! " + wedA)
elif date == "Thursday" or date == "thursday" or date == "THURSDAY":
    print("Hey " + userName +"! " + thurA)  
elif date == "Friday" or date == "friday" or date == "FRIDAY":
    print("Hey " + userName +"! " + friA)
elif date == "Saturday" or date == "saturday" or date == "SATURDAY":
    print(userName + "! " + satA)
elif date == "Sunday" or date == "sunday" or date == "SUNDAY":
    print("Hey " + userName +"! " + sunA)
else:
  print("please enter the correct day")