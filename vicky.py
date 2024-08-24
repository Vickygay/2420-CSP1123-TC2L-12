import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np

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

# Colours code in RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (173, 216, 230)
CHARCOAL = (54, 69, 79)
PINK = (255,192,203)
PURPLE = (160, 32, 240)
YELLOW = (255, 255, 0)
DARKRED = (139, 0, 0)
TRANSPARENT = (0, 0, 0, 0)
RICHGREY = (31,32,34)
DARKGREY = (169, 169, 169)

# Font setting for Life Roulette
font_1_size = 70
font_1_path = 'Creepster.ttf' 
font_1 = pygame.font.Font(font_1_path, font_1_size)

# Show (Life Roulette) on screen
text_1 = "Life Roulette"
text_1_surface = font_1.render(text_1, True, RED)

# Font setting for Start
font_2_size = 60
font_2_path = 'Creepster.ttf'  
font_2 = pygame.font.Font(font_2_path, font_2_size)

# Show (Start) on screen
text_2 = "Start"
text_2_surface = font_2.render(text_2, True, RED)

# Font setting for How to Play
font_3_size = 50
font_3_path = 'Creepster.ttf'  
font_3 = pygame.font.Font(font_3_path, font_3_size)

# Show (How to Play) on screen
text_3 = "How to Play"
text_3_surface = font_3.render(text_3, True, WHITE) 

# Font setting for Back
font_4_size = 45
font_4_path = 'Matemasie.ttf'  
font_4 = pygame.font.Font(font_4_path, font_4_size)

# Show (Back) on screen
text_4 = "Back"
text_4_surface = font_4.render(text_4, True, WHITE)

# Font setting for Next
font_5_size = 45
font_5_path = 'Matemasie.ttf'  
font_5 = pygame.font.Font(font_5_path, font_5_size)

# Show (Next) on screen
text_5 = "Next"
text_5_surface = font_5.render(text_5, True, WHITE)

transparent_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA) # Every pixel on screen is transparent
transparent_surface.fill((0, 0, 0, 128))

# All text position settings
text_1_width, text_1_height = text_1_surface.get_size()
text_1_x = (screen_width - text_1_width) // 2
text_1_y = (screen_height - text_1_height) // 2 -150

text_2_width, text_2_height = text_2_surface.get_size()
text_2_x = (screen_width - text_2_width) // 2
text_2_y = (screen_height - text_2_height) // 2 -25  

text_3_width, text_3_height = text_3_surface.get_size()
text_3_x = (screen_width - text_3_width) // 2
text_3_y = (screen_height - text_3_height) // 2 +75 

# Button areas for How to Play (Back)
button_text2_rect = pygame.Rect(text_2_x, text_2_y, text_2_width, text_2_height)
button_text3_rect = pygame.Rect(text_3_x, text_3_y, text_3_width, text_3_height)

# Back button
text_4_width, text_4_height = text_4_surface.get_size()
text_4_button_x = (screen_width - text_4_width) // 2 +400
text_4_button_y = screen_height - text_4_height // 2 -50
text_4_button_rect = pygame.Rect(text_4_button_x, text_4_button_y, text_4_width, text_4_height)

# Next button 
text_5_width, text_5_height = text_4_surface.get_size()
text_5_button_x = (screen_width - text_5_width) // 2 +200
text_5_button_y = screen_height - text_5_height // 2 -50
text_5_button_rect = pygame.Rect(text_5_button_x, text_5_button_y, text_5_width, text_5_height)

# Image settings for magnifier
image_1 = pygame.image.load('magnifier.png') 
image_1_size = (200, 200)  
image_1 = pygame.transform.scale(image_1, image_1_size)
image_1_width, image_1_height = image_1.get_size()
label_offset = 12
image_rect_1 = image_1.get_rect(topleft=(30, (screen_height - image_1_height) // 2 + 200)) 

# Label text with multiple lines
label_text_lines_1 = [
    "  Magnifier: ",
    "  Allows you to",
    "  check your",
    "  current bullet's",
    "  status"
]

font_10 = pygame.font.Font("Anton.ttf", 20)

label_surfaces = [font_10.render(line, True, (WHITE)) for line in label_text_lines_1]
label_rects = [surf.get_rect(topleft=(image_rect_1.left, image_rect_1.top - surf.get_height() - 10 + i * font_10.get_height())) for i, surf in enumerate(label_surfaces)]

# Frame settings
frame_thickness_1 = 10
frame_color_1 = BLACK
background_color_1 = DARKGREY  

# Image with frame surface
image_with_frame_surface_1 = pygame.Surface((image_1_width + 2 * frame_thickness_1, image_1_height + 2 * frame_thickness_1), pygame.SRCALPHA)
image_with_frame_surface_1.fill(background_color_1)  

# Draw the border around the image
pygame.draw.rect(image_with_frame_surface_1, frame_color_1, (0, 0, image_with_frame_surface_1.get_width(), image_with_frame_surface_1.get_height()), frame_thickness_1)

# Draw the image onto the surface with the frame
image_with_frame_surface_1.blit(image_1, (frame_thickness_1, frame_thickness_1))

# Image settings for Medicine
image_2 = pygame.image.load('medicine.png') 
image_2_size = (200, 200)  
image_2 = pygame.transform.scale(image_2, image_2_size)
image_2_width, image_2_height = image_2.get_size()
label_offset = 12
image_rect_2 = image_2.get_rect(topleft=(390, (screen_height - image_2_height) // 2 + 200))  

# Label text with multiple lines
label_text_lines_2 = [
    "  MED Kit: ",
    "  50% of chance",
    "  to get heal",
    "  but also 50%",
    "  of chance to",
    "  deduct a life"
]

label_surfaces_2 = [font_10.render(line, True, (WHITE)) for line in label_text_lines_2]
label_rects_2 = [surf.get_rect(topleft=(image_rect_2.left, image_rect_2.top - surf.get_height() - 10 + i * font_10.get_height())) for i, surf in enumerate(label_surfaces_2)]

# Frame settings
frame_thickness_2 = 10
frame_color_2 = BLACK
background_color_2 = DARKGREY  

# Image with frame surface
image_with_frame_surface_2 = pygame.Surface((image_2_width + 2 * frame_thickness_2, image_2_height + 2 * frame_thickness_2), pygame.SRCALPHA)
image_with_frame_surface_2.fill(background_color_2)  

# Draw the border around the image
pygame.draw.rect(image_with_frame_surface_2, frame_color_2, (0, 0, image_with_frame_surface_2.get_width(), image_with_frame_surface_2.get_height()), frame_thickness_2)

# Draw the image onto the surface with the frame
image_with_frame_surface_2.blit(image_2, (frame_thickness_2, frame_thickness_2))

# Image settings for Dice
image_3 = pygame.image.load('handsaw.png') 
image_3_size = (200, 200)  
image_3 = pygame.transform.scale(image_3, image_3_size)
image_3_width, image_3_height = image_3.get_size()
label_offset = 12
image_rect_3 = image_3.get_rect(topleft=(800, (screen_height - image_3_height) // 2 + 200))  

# Label text with multiple lines
label_text_lines_3 = [
    "  Dice: ",
    "  Choose a number",
    "  from 1 to 6",
    "  If the dice rolls",
    "  that number, you",
    "  win the prize!"
]

label_surfaces_3 = [font_10.render(line, True, (WHITE)) for line in label_text_lines_3]
label_rects_3 = [surf.get_rect(topleft=(image_rect_3.left, image_rect_3.top - surf.get_height() - 10 + i * font_10.get_height())) for i, surf in enumerate(label_surfaces_3)]

# Frame settings
frame_thickness_3 = 10
frame_color_3 = BLACK
background_color_3 = DARKGREY  

# Image with frame surface
image_with_frame_surface_3 = pygame.Surface((image_3_width + 2 * frame_thickness_3, image_3_height + 2 * frame_thickness_3), pygame.SRCALPHA)
image_with_frame_surface_3.fill(background_color_3)  

# Draw the border around the image
pygame.draw.rect(image_with_frame_surface_3, frame_color_3, (0, 0, image_with_frame_surface_3.get_width(), image_with_frame_surface_3.get_height()), frame_thickness_3)

# Draw the image onto the surface with the frame
image_with_frame_surface_3.blit(image_3, (frame_thickness_3, frame_thickness_3))

# Game Loop
running = True
while running:
    screen.fill(RICHGREY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if button_text2_rect.collidepoint(pos):
                sound_play.play()
                print("Start button clicked")
                # Transition to the next screen or handle start action
            if button_text3_rect.collidepoint(pos):
                sound_how_to_play.play()
                print("How to Play button clicked")
                # Transition to the How to Play screen or handle action
            if text_4_button_rect.collidepoint(pos):
                sound_back.play()
                print("Back button clicked")
                # Transition to the previous screen or handle back action
            if text_5_button_rect.collidepoint(pos):
                sound_next.play()
                print("Next button clicked")
                # Transition to the next page or handle next action

    # Draw the title text
    screen.blit(text_1_surface, (text_1_x, text_1_y))
    
    # Draw the Start and How to Play text
    screen.blit(text_2_surface, (text_2_x, text_2_y))
    screen.blit(text_3_surface, (text_3_x, text_3_y))
    
    # Draw the image with frame and labels for Magnifier
    screen.blit(image_with_frame_surface_1, image_rect_1)
    for surf, rect in zip(label_surfaces, label_rects):
        screen.blit(surf, rect)
        
    # Draw the image with frame and labels for Medicine
    screen.blit(image_with_frame_surface_2, image_rect_2)
    for surf, rect in zip(label_surfaces_2, label_rects_2):
        screen.blit(surf, rect)
    
    # Draw the image with frame and labels for Dice
    screen.blit(image_with_frame_surface_3, image_rect_3)
    for surf, rect in zip(label_surfaces_3, label_rects_3):
        screen.blit(surf, rect)

    # Draw the Start, Back, and Next buttons
    screen.blit(text_2_surface, button_text2_rect)
    screen.blit(text_3_surface, button_text3_rect)
    screen.blit(text_4_surface, text_4_button_rect)
    screen.blit(text_5_surface, text_5_button_rect)
    
    pygame.display.flip()


def update(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)

    # Check if the current screen is SCREEN_HOW_TO_PLAY
    if self.current_screen == SCREEN_HOW_:
        # Check collision with image_rect_1
        if image_rect_1.colliderect(mouse_rect):
            for label_surf, label_rect in zip(label_surfaces, label_rects):
                screen.blit(label_surf, label_rect)

        # Check collision with image_rect_2
        if image_rect_2.colliderect(mouse_rect):
            for label_surf, label_rect_2 in zip(label_surfaces_2, label_rects_2):
                screen.blit(label_surf, label_rect_2)

        # Check collision with image_rect_3
        if image_rect_3.colliderect(mouse_rect):
            for label_surf, label_rect_3 in zip(label_surfaces_3, label_rects_3):
                screen.blit(label_surf, label_rect_3)