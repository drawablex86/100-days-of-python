print("Log Defender 2024")
name = input("Enter your name > ")
passwrd = input("Enter password: ")
if name == "Jack" and passwrd == "Jack":
  print("Welcome Jack")
elif name == "Jill" and passwrd == "Jill":
  print("Welcome Jill")
else:
  print("Invalid User. Create a new id and password!")
newUser = input("Enter a new username > ")
newPass = input("Enter a new password > ")
print("Welcome", newUser)
cond = input ("Do you wish to logout? yes or no: ")
if cond == "yes":
  print("You are logged out!")
  name = input("Enter your name > ")
  passwrd = input("Enter password: ")
if name == "Jack" and passwrd == "Jack":
  print("Welcome Jack")
elif name == "Jill" and passwrd == "Jill":
  print("Welcome Jill")
elif name == newUser and passwrd == newPass:
  print("welcome", newUser)
else: 
  print(newUser, "You are still logged in!")
  
    