import random 

x = ["Hello There", "Hola", "Bonjour", "Hallo", "Ciao", "こんにちは (Konnichiwa)", "你好 (Nǐ hǎo)", "Привет (Privet)", "مرحبا (Marhaban)", "Olá", "नमस्ते (Namaste)"] 

while True:     
    y = random.randint(0, len(x) - 1)     
    greeting = x[y]     
    print("\n\t---", greeting,"---\n")     
    check = input("do you want to continue?y/n\n").strip().lower()     
    if check == "n":         
        break 

print("Thank you for using the random greeting generator!")