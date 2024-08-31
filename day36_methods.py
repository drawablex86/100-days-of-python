import os, time
namedb = []
def getName():
  fn = input("\nFirst Name: ").strip().lower()
  ln = input("Last Name: ").strip().lower()
  name = f"{fn} {ln}"
  return name

def printList():
  print()
  for name in namedb:
    print(name.upper())

while True:
  name = getName()
  if name not in namedb:
    namedb.append(name)
  else:
    print("\nERROR: Duplicate name")
  printList()
  time.sleep(3)
  os.system("clear")
