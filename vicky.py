import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tooltip Example')

# Define tooltip properties
tooltip_width = 150
tooltip_height = 50
tooltip_color = (255, 255, 255)  # White color for the tooltip

# Create tooltip surface and rect
tooltip_surface = pygame.Surface((tooltip_width, tooltip_height))
tooltip_surface.fill(tooltip_color)
tooltip_rect = tooltip_surface.get_rect()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate tooltip position
    tooltip_x = mouse_x - tooltip_width // 2
    tooltip_y = mouse_y - tooltip_height - 10  # 10 pixels above the mouse

    # Update tooltip rect position
    tooltip_rect.topleft = (tooltip_x, tooltip_y)

    # Clear screen
    screen.fill((0, 0, 0))  # Black background

    # Draw tooltip
    screen.blit(tooltip_surface, tooltip_rect)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(30)
