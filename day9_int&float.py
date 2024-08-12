print ("Find which generation you belong to!")
print("************************************")
bDay = int(input("What year were you born in? > "))
if bDay >=1925 and bDay <=1946:
  print("Woah.You are a Traditionalist!")
elif bDay >=1947 and bDay <=1964:
  print("Nice, you are Baby Boomer!")
elif bDay >= 1965 and bDay <= 1981:
  print("Damn, You are Generation X!")  
elif bDay >= 1982 and bDay <= 1995:
  print("You are a Millenial! 90s kids rule!")  
elif bDay >= 1996 and bDay <= 2015:
  print("Hey, Gen Z! TikTok much?")
else:
  print("Try again!")