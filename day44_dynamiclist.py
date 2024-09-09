import random, time, os

def createBingo():
    global bingo
    bingo = []
    for i in range(3):
        row = []
        for j in range(3):
            x = random.randint(0, 90)
            row.append(x)
        bingo.append(row)
    # Sort after all rows are added
    for row in bingo:
        row.sort()
    bingo[1][1] = "Bingo"

def prettyPrint():
    for row in bingo:
        for item in row:
            print(item, end="\t|\t")
        print()

createBingo()
counter = 0
while True:
    print("\nYour Card")
    prettyPrint()
    num = int(input("\nEnter a number: "))
    time.sleep(1)
    os.system("clear")
    for row in bingo:
        for i in range(len(row)):  # Use index to access elements
            if row[i] == num:      # Compare the element with num
                row[i] = "X"
    counter += 1
    if counter == 8:
        print("Bingo")
        break