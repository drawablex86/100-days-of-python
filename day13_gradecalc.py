print("HANDY GRADE CALCULATOR V0.1")
print("---------------------------")
name = input ("Enter the name of your test: ")
max = int(input("Enter the maximum you can score: "))
mark = float(input("Enter your score: "))
percent = (mark/max)*100
percent = round(percent,2)
print ()
if percent >= 90 and percent < 101:
  print ("You have worked hard and scored",percent,"%")
  print ("Awesome! That's an A+")
elif percent > 100 or percent < 0:
  print ("Oops! You have entered an invalid score")
elif percent >= 80 and percent < 90:
  print ("You have worked hard and scored",percent,"%")
  print ("Good Going on Scoring an A")
elif percent >=70 and percent < 80:
  print ("You have worked hard and scored",percent,"%")
  print ("Congrats! Your grade is B")
elif percent >=60 and percent < 70:
  print ("You have worked hard and scored",percent,"%")
  print ("Sadly your grade C. Keep studying.")
elif percent >= 50 and percent < 60:
  print ("You have worked hard and scored",percent,"%")
  print("Tough Luck! You have scored a D")
else:
  print ("You have worked hard and scored",percent,"%")
  print ("Damn! You have scored a U. Study hard son.")