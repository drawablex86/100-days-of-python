# code improved with the help of claude
import random
import os
import time

CHARACTER_TYPES = {
    "Human": {"health_multiplier": 5, "strength_multiplier": 3},
    "Orc": {"health_multiplier": 6, "strength_multiplier": 2},
    "Wizard": {"health_multiplier": 2, "strength_multiplier": 4},
    "Elf": {"health_multiplier": 2, "strength_multiplier": 4}
}

def get_character():
    while True:
        name = input("Enter character name: ")
        char_type = input("Enter character type (Human, Elf, Wizard, Orc): ").capitalize()
        if char_type in CHARACTER_TYPES:
            return name, char_type
        print("Invalid character type. Please try again.")

def roll_dice():
    return random.randint(1, 6)

def calculate_stats(char_type):
    dice_roll = roll_dice()
    stats = CHARACTER_TYPES[char_type]
    return (dice_roll * stats["health_multiplier"], 
            dice_roll * stats["strength_multiplier"])

def display_stats(name, char_type, health, strength):
    print(f"{'Player Stats':--------------------------------}")
    print(f"{char_type} - {name}")
    print(f"Health: {health}")
    print(f"Strength: {strength}")
    print("-" * 32)

def battle_round(attacker, defender, damage):
    print(f"{attacker['name']} attacks {defender['name']} with full force!")
    defender['health'] -= damage
    print(f"{defender['name']} has only {defender['health']} health left")
    return defender['health'] <= 0

def main():
    print("Welcome to Giga Battle World")
    print("*" * 30)
    print("Created by Rahul Rajeev")
    
    players = []
    for i in range(2):
        name, char_type = get_character()
        health, strength = calculate_stats(char_type)
        players.append({"name": name, "type": char_type, 
                        "health": health, "strength": strength})
        
    os.system("clear")
    for player in players:
        display_stats(**player)
    
    damage = abs(players[0]["strength"] - players[1]["strength"]) + 1
    
    input("Press any key to start the battle")
    os.system("clear")
    print("***** Battle Begins ******")
    
    round_count = 0
    while True:
        time.sleep(3)
        os.system("clear")
        round_count += 1
        print(f"\nRound {round_count}")
        
        rolls = [roll_dice() for _ in range(2)]
        if rolls[0] != rolls[1]:
            winner, loser = players if rolls[0] > rolls[1] else players[::-1]
            print(f"{winner['name']} has won this round!")
            if battle_round(winner, loser, damage):
                print(f"{winner['name']} has won the epic battle")
                print(f"Tough Luck {loser['name']}")
                break
        else:
            print("This round has been tied")
    
    print("\nThanks for playing")
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        main()

if __name__ == "__main__":
    main()