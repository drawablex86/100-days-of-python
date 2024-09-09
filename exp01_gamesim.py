import pygame, time, os
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Player:
    def __init__(self, x, y):
        self.health = 100
        self.x = x
        self.y = y

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 5
        if keys[pygame.K_s]:
            self.y += 5
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5

def splash_screen():
    # Set screen background color to red
    screen.fill(RED)
    
    # Limit screen update to once (splash screen duration)
    clock = pygame.time.Clock()
    clock.tick(1)

    # Wait for 2 seconds before proceeding
    time.sleep(2)
    return True

def draw_players(player1, player2):
    # Draw players on the screen
    pygame.draw.rect(screen, GREEN, (player1.x, player1.y, 50, 50))
    pygame.draw.rect(screen, GREEN, (player2.x, player2.y, 50, 50))

def game_loop():
    clock = pygame.time.Clock()
    player1 = Player(100, 100)
    player2 = Player(700, 500)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_players(player1, player2)
        
        # Update player positions
        player1.move()
        player2.move()

        # Check for collisions and update health accordingly
        if (player1.x < 50 and player1.y > 550) or (player2.x > 750 and player2.y < 50):
            player1.health -= 10
            player2.health -= 10

        # Draw the current health of each player
        font = pygame.font.Font(None, 36)
        text1 = font.render(str(player1.health), True, (255, 255, 255))
        text2 = font.render(str(player2.health), True, (255, 255, 255))

        screen.blit(text1, (50, 20))
        screen.blit(text2, (700, 20))

        # Check for game over condition
        if player1.health <= 0 or player2.health <= 0:
            # Determine the winner based on remaining health
            if player1.health > 0:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

            # End the game loop
            return

        # Draw everything to the screen
        pygame.display.flip()

def play_sound():
    # Initialize mixer module
    pygame.mixer.init()

    # Load and play the sound file
    sound = pygame.mixer.Sound("sound_file.wav")
    sound.play()

# Run the splash screen first
splash_screen()

# Run the game loop next
game_loop()

# Play the sound at the end
play_sound()
