def getPass(): 
  user = input("Enter username: ")
  password = input ("Enter your pass:")
  return user, password #returns value as a tuple

def checkPass(user, password):
  if user == "admin" and password == "password":
    print("Login successful!")
  else:
    print("Login failed. Please try again.")
    print()
    main()

def main():
  user, password = getPass()
  checkPass(user, password)
  

print("Enter your creds to continue!")
print("*****")
main()


# i have over engineered this, just to learn how subroutines/function work in python
# you can pack a lot of functionality in to a single subroutine
# values that are collected in a subroutine needs to be returned for it to be used in the main program (see line 4)
# subroutine can call other values from outside to check for logic (see line 6)
