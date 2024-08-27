import pygame
import pygame.freetype  # For rendering text
import sys  # For sys.exit()

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Image with Tooltip')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load and scale image
image_1 = pygame.image.load('magnifier.png')
original_image_size = (200, 200)  # Original size for the image
image_1 = pygame.transform.scale(image_1, original_image_size)
image_1_width, image_1_height = image_1.get_size()
image_1_x = 70
image_1_y = (screen_height - image_1_height) // 2 + 150

# Tooltip settings
tooltip_font = pygame.freetype.SysFont('Arial', 24)
tooltip_text = "This is a magnifier."
tooltip_bg_color = BLACK
tooltip_text_color = WHITE

# Create a surface for the image with frame
frame_thickness = 10
image_with_frame_surface = pygame.Surface((image_1_width + 2 * frame_thickness, image_1_height + 2 * frame_thickness), pygame.SRCALPHA)
image_with_frame_surface.fill((0, 0, 0, 0))
pygame.draw.rect(image_with_frame_surface, WHITE, (0, 0, image_with_frame_surface.get_width(), image_with_frame_surface.get_height()), frame_thickness)
image_with_frame_surface.blit(image_1, (frame_thickness, frame_thickness))

# Create MAIN_SCREEN surface
SCREEN_HOW_TO_PLAY_surface = pygame.Surface((screen_width, screen_height))
SCREEN_HOW_TO_PLAY_surface.fill(BLACK)
SCREEN_HOW_TO_PLAY_surface.blit(image_with_frame_surface, (image_1_x, image_1_y))

# State management
current_screen = 'SCREEN_HOW_TO_PLAY'

# Main loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                current_screen = 'MAIN_SCREEN'
            elif event.key == pygame.K_s:
                # Implement logic for another screen if needed
                pass

    screen.fill(BLACK)  # Clear the screen
    if current_screen == "SCREEN_HOW_TO_PLAY":
        screen.blit(SCREEN_HOW_TO_PLAY_surface, (0, 0))

        # Check if mouse is over the image
        image_rect = pygame.Rect(image_1_x, image_1_y, image_1_width + 2 * frame_thickness, image_1_height + 2 * frame_thickness)
        if image_rect.collidepoint(mouse_x, mouse_y):
            # Render tooltip
            tooltip_surface, tooltip_rect = tooltip_font.render(tooltip_text, fgcolor=tooltip_text_color, bgcolor=tooltip_bg_color)
            tooltip_rect.topleft = (mouse_x + 10, mouse_y + 10)  # Position the tooltip
            screen.blit(tooltip_surface, tooltip_rect)
            
    pygame.display.flip()
    pygame.time.Clock().tick(60)
