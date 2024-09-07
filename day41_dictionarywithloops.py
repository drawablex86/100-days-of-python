myDb = {"name":None,"url":"","desc":"","rating":""}
print()

def addData():
    for i, _ in myDb.items(): #unpacks the dictionary, i represent key. You can also use myDb.key() to only call the key into the loop
        myDb[i] = input(f"\nEnter the {i}: ")
    return myDb

def printData():
    for name, value in myDb.items():
        print(f"{name} : {value}")


def main():
    print("Website Logger\n****************")
    myDb = addData()
    printData()

while True:
    main()
    x = input("\nDo you want to exit?y/n: ").lower()
    if x == "y":
        exit()
    else:
        continue