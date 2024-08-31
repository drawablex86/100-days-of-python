import os, time
while True:
  print("=== Star Wars Name Generator ===\n")
  menu = input("1: Play the game\n2: Exit\n\n> ")
  if menu == "1":
    fn = input("Enter your first name: ").strip().lower()
    sn = input("Enter your surname: ").strip().lower()
    fname = f"{fn[:3]}{sn[:3]}".capitalize()
    maiden = input("\nEnter your mother's maiden name: ")
    city = input("\nEnter the city where your mom was born: ")
    lname = f"{maiden[:2]}{city[-3:]}".capitalize()
    print(f"{fname} {lname}")
    time.sleep(5)
    os.system("clear")
  else:
    exit()
