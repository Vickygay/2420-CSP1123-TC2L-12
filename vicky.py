import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Screen Size
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Life Roulette')

# Video
video_clip = VideoFileClip('video.mp4')
fps = video_clip.fps

def get_frame_as_surface(frame):
    frame_bgr = np.flip(frame, axis=0)  
    frame_bgr = np.rot90(frame_bgr, k=-1) 
    return pygame.surfarray.make_surface(frame_bgr)

# Background music in Menu
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.set_volume(0.3)  # (0.0 - 1.0)
pygame.mixer.music.play(-1)  # Loop music infinity

# Sound effects when click the text
sound_play = pygame.mixer.Sound('clicksound.mp3')
sound_how_to_play = pygame.mixer.Sound('clicksound.mp3')
sound_back = pygame.mixer.Sound('clicksound.mp3')
sound_next = pygame.mixer.Sound('clicksound.mp3')
sound_clickbox = pygame.mixer.Sound("clickbox.mp3")

# Colours code in RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CHARCOAL = (54, 69, 79)
DARKRED = (139, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

# Font setting for Life Roulette
font_1_size = 85
font_1_path = 'Creepster.ttf'
font_1 = pygame.font.Font(font_1_path, font_1_size)

# Show (Life Roulette) on screen
text_1 = "Life Roulette"
text_1_surface = font_1.render(text_1, True, RED)

text_1_width, text_1_height = text_1_surface.get_size()
text_1_x = (screen_width - text_1_width) // 2
text_1_y = (screen_height - text_1_height) // 2 -150
# Font setting for Start
font_2_size = 70
font_2_path = 'Creepster.ttf'
font_2 = pygame.font.Font(font_2_path, font_2_size)

# Show (Start) on screen
text_2 = "Start"
text_2_surface = font_2.render(text_2, True, RED)

text_2_width, text_2_height = text_2_surface.get_size()
text_2_x = (screen_width - text_2_width) // 2
text_2_y = (screen_height - text_2_height) // 2 -10 

# Font setting for How to Play
font_3_size = 60
font_3_path = 'Creepster.ttf'
font_3 = pygame.font.Font(font_3_path, font_3_size)

# Show (How to Play) on screen
text_3 = "How to Play"
text_3_surface = font_3.render(text_3, True, WHITE)

# Show (How to Play) on screen
text_3_width, text_3_height = text_3_surface.get_size()
text_3_x = (screen_width - text_3_width) // 2
text_3_y = (screen_height - text_3_height) // 2 + 110

# Button areas for How to Play (Back)
button_text2_rect = pygame.Rect(text_2_x, text_2_y, text_2_width, text_2_height)
button_text3_rect = pygame.Rect(text_3_x, text_3_y, text_3_width, text_3_height)

# Load and scale the image for Gun
image_4 = pygame.image.load('Gun.png')
image_4_size = (150, 100)
image_4 = pygame.transform.scale(image_4, image_4_size)
image_4_width, image_4_height = image_4.get_size()
image_4_x = (screen_width - image_4_width) // 2
image_4_y = (screen_height - image_4_height) // 2

# Define screen states
SCREEN_MAIN = 0
SCREEN_PLAY1 = 9
current_screen = SCREEN_MAIN

# Bullet setting for round 1
num_real_bullets = 5
num_fake_bullets = 3
shoot_message = " "

def bullet():
    global num_real_bullets, num_fake_bullets, shoot_message
    mouse_pos = pygame.mouse.get_pos()

    # Handle gun click
    if image_4_x <= mouse_pos[0] <= image_4_x + image_4_width and image_4_y <= mouse_pos[1] <= image_4_y + image_4_height:
        if num_real_bullets > 0 or num_fake_bullets > 0:
            available_bullets = []
            if num_real_bullets > 0:
                available_bullets.append("real")
            if num_fake_bullets > 0:
                available_bullets.append("fake")

            bullet_type = random.choice(available_bullets)

            if bullet_type == "real":
                num_real_bullets -= 1
                shoot_message = "You shot a Real bullet!"
            else:
                num_fake_bullets -= 1
                shoot_message = "You shot a Fake bullet!"
        else:
            shoot_message = "No bullets left!"

# Main loop
running = True
while running:
    screen.fill(BLACK)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == SCREEN_PLAY1:
                bullet()

            # Handle transitions between screens
            if current_screen == SCREEN_MAIN:
                if button_text2_rect.collidepoint(event.pos):
                    sound_play.play()
                    current_screen = SCREEN_PLAY1  # Proceed to the game play screen

    # Render based on current screen
    if current_screen == SCREEN_MAIN:
        screen.blit(text_1_surface, (text_1_x, text_1_y))
        screen.blit(text_2_surface, (text_2_x, text_2_y))
        screen.blit(text_3_surface, (text_3_x, text_3_y))

    elif current_screen == SCREEN_PLAY1:
        # Show bullet count and gun
        real_bullets_text = pygame.font.SysFont(None, 36).render(f"Real Bullets: {num_real_bullets}", True, WHITE)
        fake_bullets_text = pygame.font.SysFont(None, 36).render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
        screen.blit(real_bullets_text, (10, 10))
        screen.blit(fake_bullets_text, (300, 10))
        screen.blit(image_4, (image_4_x, image_4_y))

        shoot_message_text = pygame.font.SysFont(None, 36).render(shoot_message, True, WHITE)
        screen.blit(shoot_message_text, (10, 100))

    pygame.display.flip()
    pygame.time.Clock().tick(30)
