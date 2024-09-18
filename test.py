import pygame
import tkinter as tk
from tkinter import messagebox

# Initialize pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Play or Quit?")

# Function to create a Tkinter pop-up
def play_or_quit():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    result = messagebox.askquestion("Play or Quit?", "Do you want to play or quit?")
    root.destroy()
    return result

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Trigger the Tkinter pop-up when 'p' is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                result = play_or_quit()
                if result == 'yes':
                    print("Player wants to play!")
                else:
                    print("Player chose to quit.")
                    running = False

    # Fill screen with white (for example)
    screen.fill((255, 255, 255))

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
