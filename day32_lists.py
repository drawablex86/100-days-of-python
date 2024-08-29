# Random multi-lingual greeting generator
import random
x = ["Hello There", "Hola", "Bonjour", "Hallo", "Ciao", "こんにちは (Konnichiwa)", "你好 (Nǐ hǎo)", "Привет (Privet)", "مرحبا (Marhaban)", "Olá", "नमस्ते (Namaste)"]
while True:
    y = random.randint(0,10)
    greeting = x[y]
    print("\n\t---", greeting,"---\n")
    check =input("do you want to continue?y/n\n")
    if check == "n":
        break




#while loop is broken and i have no idea why this is so. I tried a lot of stuff.