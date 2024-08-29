
#ANSI Codes, makes it easier to use the colours. Can also be implemented as subroutines.
RED = '\033[91m' 
RESET = '\033[37m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'


# Interface one - terminal based
title = f"{RED}={RESET}={BLUE}={RESET} Music APP {BLUE}={RESET}={RED}={RESET}" # creating the title using f-strings
print(f"{title: ^80}") # centering can only be done inside the curly brackets of fstring.
print()
print("🔥▶️\t Radio Gaga\n\t Queen")
print()
print("PREV")
print(f"\t {GREEN}NEXT{RESET}")
print(f"\t\t {RED}PAUSE{RESET}")


print()
# Interface two
x = "WELCOME TO"
print(f"{x:^30}")
arm = f"{BLUE}-- ARMBOOK --{RESET}"
print(f"{arm : ^40}")
# here i declared the strings and then used fstrings
y = "Definitely not a rip off of"
z = "a certain other social"
a = "networking site."
print(f"{YELLOW}{y:>35}\n{z:>35}\n{a:>35}{RESET}") # Alternatively I could have used the same variable to declare each of the sentence and the use seperate print statements.
h = "honest."
h = h.upper() 
print(f"\n{RED}{h:^25}{RESET}".upper())
print()




