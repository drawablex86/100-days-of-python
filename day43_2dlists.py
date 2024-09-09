#2D Lists
import random
bingo =[]
number =[]

for i in range(8):
    x=random.randint(0,90)
    number.append(x)
    

bingo = [[number[0],number[1],number[2]],
         [number[3],"Bingo",number[4]],
         [number[5],number[6],number[7]],
         ]

for row in bingo:
    print(f"{row}\n-----------")