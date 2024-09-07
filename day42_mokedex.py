# A simple pokedex clone to learn more about dictionaries

myDB = {"name":None, "type":"None", "special move":None, "hp":None, "mp":None}
red = "\033[91m"      # ASCII color for red
blue = "\033[94m"     # ASCII color for blue
brown = "\033[33m"    # ASCII color for brown
default = "\033[0m"   # ASCII color for default

def getChar():
    for i in myDB.keys():
        myDB[i]=input(f"Enter the {i} of your character: ")
    return myDB

def printChar():
    for key, value in myDB.items():
        print(f"{key: <15}:{value}").title()



print("\nElemental MokeDex\n*****************\n\nChoose you champion of FIRE, WATER, EARTH AND AIR!!!!\n")
myDB=getChar()
print()
if myDB['type'].lower() == "earth":
    print(brown)
    printChar()
    print(default)
elif myDB['type'].lower() == "water":
    print(blue)
    printChar()
    print(default)
elif myDB['type'].lower() == "fire":
    print(red)
    printChar()
    print(default)  
else:
    printChar()