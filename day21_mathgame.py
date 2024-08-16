# builing a math game challenge
# requritements:
    # get a number from the user
    # ask the user to solve each multiple of the chosen number till 10
    # if the user gets it right, they get a point
    # if the user gets it wrrong, shows the correct answer and proceeds to next question
    # at the end of the game, show the user their final score.

print ()
print("\033[32m" + "Welcome to the Math Game!" + "\033[0m") ## tried adding colour to the h1
print("---------------------------------")
print("Solve the multiples of your chosen number to score points")
print()
while True:
    score = 0
    x = int(input("Enter a number: "))
    for i in range(1, 11):
        print()
        print("What is", x,"x",i,"=") # learned that input function cannot handle more than one argument (variable) at a time, so had to split the question and answer collection into two steps.
        ans = int(input())
        if ans == x * i:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The right answer is", x * i)
    print("Congrats!, Your final score is", score)
    print()
    y = input("Do you want to play again? (y/n): ")
    if y == "y":
        continue
    else:
        print()
        print("Thanks for playing!")
        exit()