import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np
import random
from moviepy.editor import *

# Initialize Pygame
pygame.init()

# Screen Size
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Life Roulette')


# Resize Video
def resize_video(video_clip, size):
    return video_clip.resize(newsize=size)

# Video
video_clip = VideoFileClip('video.mp4')
debtorturn_video = VideoFileClip('gun 2.mp4')
playerturn_video = VideoFileClip('gun 1.mp4')
totem = VideoFileClip('totem.mp4')
handsawvideo1 = VideoFileClip('handsawvideo1.mp4')
handsawvideo2 = VideoFileClip('handsawvideo2.mp4')

# Resize videos to fit the screen
video_size = (200, 200)
debtorturn_video = resize_video(debtorturn_video, video_size)
playerturn_video = resize_video(playerturn_video, video_size)
totem = resize_video(totem, video_size)
handsawvideo1 = resize_video(handsawvideo1, video_size)
handsawvideo2 = resize_video(handsawvideo2, video_size)
=======
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
gun_sound = pygame.mixer.Sound("gunsound.mp3")
emptygun_sound = pygame.mixer.Sound("emptygun.mp3")
delete_sound = pygame.mixer.Sound("delete.mp3")
totem_sound = pygame.mixer.Sound("totem.mp3")
handsaw_sound = pygame.mixer.Sound("handsaw.mp3")

# Colours code in RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (173, 216, 230)
CHARCOAL = (54, 69, 79)
LIGHTRED = (255,0,0)
PURPLE = (160, 32, 240)
YELLOW = (255, 255, 0)
DARKRED = (139, 0, 0)
TRANSPARENT = (0, 0, 0, 0)
RICHGREY = (31,32,34)
DARKGREY = (169, 169, 169)
BISQUE2 = (238, 213, 183, 255)
LIGHTCYAN3 = (180, 205, 205, 255)
LIGHTCYAN4 = (122, 139, 139, 255)
LIGHTSKYBLUE4 = (96, 123, 139, 255)
LIGHTCYAN2 = (209, 238, 238, 255)
LIGHTGREY = (211, 211, 211)

font = pygame.font.Font("DMRegular.ttf", 18)

font_1 = pygame.font.Font('Creepster.ttf', 85)
text_1_surface = font_1.render("Life Roulette", True, RED)
text_1_x, text_1_y = (screen_width - text_1_surface.get_width()) // 2, (screen_height - text_1_surface.get_height()) // 2 - 150

font_2 = pygame.font.Font('Creepster.ttf', 70)
text_2_surface = font_2.render("Start", True, RED)
text_2_x, text_2_y = (screen_width - text_2_surface.get_width()) // 2, (screen_height - text_2_surface.get_height()) // 2 - 10 
button_text2_rect = pygame.Rect(text_2_x, text_2_y, text_2_surface.get_width(), text_2_surface.get_height())


font_3 = pygame.font.Font('Creepster.ttf', 60)
text_3_surface = font_3.render("How to Play", True, WHITE)
text_3_x, text_3_y = (screen_width - text_3_surface.get_width()) // 2, (screen_height - text_3_surface.get_height()) // 2 + 110
button_text3_rect = pygame.Rect(text_3_x, text_3_y, text_3_surface.get_width(), text_3_surface.get_height())
font3 = pygame.font.Font("Nerko.ttf", 22)

font_4 = pygame.font.Font('Matemasie.ttf', 45)
text_4_surface = font_4.render("<< Back", True, WHITE)
text_4_button_x, text_4_button_y = (screen_width - text_4_surface.get_width()) // 2 - 400, screen_height - text_4_surface.get_height() // 2 - 50
text_4_button_rect = pygame.Rect(text_4_button_x, text_4_button_y, text_4_surface.get_width(), text_4_surface.get_height())
=======
# Font setting for Life Roulette
font_1_size = 85
font_1_path = 'Creepster.ttf' 
font_1 = pygame.font.Font(font_1_path, font_1_size)

# Show (Life Roulette) on screen
text_1 = "Life Roulette"
text_1_surface = font_1.render(text_1, True, RED)

# Font setting for Start
font_2_size = 70
font_2_path = 'Creepster.ttf'  
font_2 = pygame.font.Font(font_2_path, font_2_size)

# Show (Start) on screen
text_2 = "Start"
text_2_surface = font_2.render(text_2, True, RED)

# Font setting for How to Play
font_3_size = 60
font_3_path = 'Creepster.ttf'  
font_3 = pygame.font.Font(font_3_path, font_3_size)

# Show (How to Play) on screen
text_3 = "How to Play"
text_3_surface = font_3.render(text_3, True, WHITE) 

# Show (How to Play) on screen
text_3 = "How to Play"
text_3_surface = font_3.render(text_3, True, WHITE) 

# Font setting for Back
font_4_size = 45
font_4_path = 'Matemasie.ttf'  
font_4 = pygame.font.Font(font_4_path, font_4_size)

# Show (Back) on screen
text_4 = "<< Back"
text_4_surface = font_4.render(text_4, True, WHITE)

# Font setting for Next
font_5_size = 45
font_5_path = 'Matemasie.ttf'  
font_5 = pygame.font.Font(font_5_path, font_5_size)

# Show (Next) on screen
text_5 = "Next >>"
text_5_surface = font_5.render(text_5, True, WHITE)

# Font setting for Back to Main
font_8_size = 45
font_8_path = 'Matemasie.ttf'
font_8 = pygame.font.Font(font_8_path, font_8_size)

# Show (Back to Main) on screen
text_8 = "<< Main"
text_8_surface = font_8.render(text_8, True, WHITE)

# Font setting Enter Your Name
font_11_size = 70
font_11_path = 'Nerko.ttf'
font_11 = pygame.font.Font(font_11_path, font_11_size)

# Show Enter your name
text_11 = "Enter Your Name!"
text_11_surface = font_11.render(text_11, True, WHITE)

# Fonts setting for How many bullets left
font_12_size = 36
font_12_path = "Nerko.ttf"
font_12 = pygame.font.Font(font_12_path, font_12_size)

font_13_size = 28
font_13_path = "Nerko.ttf"
font_13 = pygame.font.Font(font_13_path, font_13_size)

font_5 = pygame.font.Font('Matemasie.ttf', 45)
text_5_surface = font_5.render("Next >>", True, WHITE)
text_5_button_x, text_5_button_y = (screen_width - text_5_surface.get_width()) // 2 + 400, screen_height - text_5_surface.get_height() // 2 - 50
text_5_button_rect = pygame.Rect(text_5_button_x, text_5_button_y, text_5_surface.get_width(), text_5_surface.get_height())
# Show (Life) on screen and positioning

life_text_surface = font_5.render("Life:", True, RED)
life_x, life_y = 3, 0

font_6 = pygame.font.Font('Matemasie.ttf', 40)
lose_text_surface = font_6.render("Foolish gambler. Try again would ya?", True, RED)
lose_x, lose_y = 125, 250

# You win
font_7 = pygame.font.Font('Matemasie.ttf', 40)
win_text_surface = font_7.render("Congratulations, your humanity didn't betray you.", True, WHITE)
win_x, win_y = 50, 50

# Round Two
font_8 = pygame.font.Font('Matemasie.ttf', 40)
round_2_surface = font_8.render("Round Two", True, WHITE)
round_2_x, round_2_y = 375, 0

# Final Round
font_9 = pygame.font.Font('Matemasie.ttf', 40)
round_3_surface = font_9.render("Final Round", True, RED)
round_3_x, round_3_y = 375, 0

font_10 = pygame.font.Font("Gloria.ttf", 47)

font_11 = pygame.font.Font('Nerko.ttf', 70)
text_11_surface = font_11.render("Enter Your Name!", True, WHITE)
text_11_button_x, text_11_button_y = (screen_width - text_11_surface.get_width()) // 2, (screen_width // 2) - text_11_surface.get_height() - 200
text_11_button_rect = pygame.Rect(text_11_button_x, text_11_button_y, text_11_surface.get_width(), text_11_surface.get_height())

font_12 = pygame.font.Font('Nerko.ttf', 36)
font_13 = pygame.font.Font('Nerko.ttf', 28)

font_14 = pygame.font.Font('Matemasie.ttf', 45)
text_14_surface = font_14.render("<< Main", True, WHITE)
text_14_button_x, text_14_button_y = (screen_width - text_14_surface.get_width()) // 2 - 400, screen_height - text_14_surface.get_height() // 2 - 50
text_14_button_rect = pygame.Rect(text_14_button_x, text_14_button_y, text_14_surface.get_width(), text_14_surface.get_height())

input_font_name = pygame.font.Font("Gloria.ttf", 50)

font_turn = pygame.font.Font("Creepster.ttf", 60)
turn_message = "Player's Turn"

transparent_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 0, 0)) 
=======
life_text = "Life:"
life_text_surface = font_5.render(life_text, True, RED)
life_x = 3
life_y = 0

# Font setting for You lose
font_6_size = 40
font_6_path = 'Matemasie.ttf'
font_6 = pygame.font.Font(font_6_path, font_6_size)

# Show (You lose) on screen and positioning
lose_text = "Foolish gambler.Try again would ya?"
lose_text_surface = font_6.render(lose_text, True, RED)
lose_x = 125
lose_y = 250

# Font setting for You win 
font_7_size = 40
font_7_path = 'Matemasie.ttf'
font_7 = pygame.font.Font(font_7_path, font_7_size)

# Show (You win) on screen and positioning
win_text = "Congratulations, your humanity didn't betray you."
win_text_surface = font_7.render(win_text, True, WHITE)
win_x = 50
win_y = 50

# Font setting for Round two
font_8_size = 40
font_8_path = 'Matemasie.ttf'
font_8 = pygame.font.Font(font_8_path, font_8_size)

# Show (Round two) on screen and positioning
round_2 = "Round Two"
round_2_surface = font_8.render(round_2, True, WHITE)
round_2_x = 375
round_2_y = 0

# Font setting for Final Round)
font_9_size = 40
font_9_path = "Matemasie.ttf"
font_9 = pygame.font.Font(font_9_path, font_9_size)

#Show (Final Round) on screen and positioning
round_3 = "Final Round"
round_3_surface = font_9.render(round_3, True, RED)
round_3_x = 375
round_3_y = 0

transparent_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA) # Every pixel on screen is transparent
transparent_surface.fill((0, 0, 0, 128))

# All text position settings
text_1_width, text_1_height = text_1_surface.get_size()
text_1_x = (screen_width - text_1_width) // 2
text_1_y = (screen_height - text_1_height) // 2 -150

text_2_width, text_2_height = text_2_surface.get_size()
text_2_x = (screen_width - text_2_width) // 2
text_2_y = (screen_height - text_2_height) // 2 -10 

text_3_width, text_3_height = text_3_surface.get_size()
text_3_x = (screen_width - text_3_width) // 2
text_3_y = (screen_height - text_3_height) // 2 +110

# Button areas for How to Play (Back)
button_text2_rect = pygame.Rect(text_2_x, text_2_y, text_2_width, text_2_height)
button_text3_rect = pygame.Rect(text_3_x, text_3_y, text_3_width, text_3_height)

# Back button
text_4_width, text_4_height = text_4_surface.get_size()
text_4_button_x = (screen_width - text_4_width) // 2 -400
text_4_button_y = screen_height - text_4_height // 2 -50
text_4_button_rect = pygame.Rect(text_4_button_x, text_4_button_y, text_4_width, text_4_height)

# Next button 
text_5_width, text_5_height = text_5_surface.get_size()
text_5_button_x = (screen_width - text_5_width) // 2 +400
text_5_button_y = screen_height - text_5_height // 2 -50
text_5_button_rect = pygame.Rect(text_5_button_x, text_5_button_y, text_5_width, text_5_height)

# Main button 
text_8_width, text_8_height = text_8_surface.get_size()
text_8_button_x = (screen_width - text_8_width) // 2 -400
text_8_button_y = screen_height - text_8_height // 2 -50
text_8_button_rect = pygame.Rect(text_8_button_x, text_8_button_y, text_8_width, text_8_height)

# Click Shift button
text_11_width, text_11_height = text_11_surface.get_size()
text_11_button_x = (screen_width - text_11_width) // 2 
text_11_button_y = screen_width // 2- text_11_height - 200
text_11_button_rect = pygame.Rect(text_11_button_x, text_11_button_y, text_11_width, text_11_height)

# Image settings for magnifier
image_1 = pygame.image.load('magnifier.png') 
image_1_size = (200, 200)
image_1 = pygame.transform.scale(image_1, image_1_size)
image_1_width, image_1_height = image_1.get_size()
image_1_x = 70
image_1_y = (screen_height - image_1_height) // 2 + 150

# Image settings for magnifier (In game)
image_mag = pygame.image.load("magnifier.png")
image_mag_size = (100, 100)
image_mag = pygame.transform.scale(image_mag, image_mag_size)
image_mag_width, image_mag_height = image_mag.get_size()
image_mag_x = 225
image_mag_y = 200

# Tooltip settings
tooltip_font = pygame.freetype.SysFont('Edu.ttf', 20)
tooltip_text = "Magnifier: Allows you to check your current bullet's status"
tooltip_bg_color = BLACK
tooltip_text_color = WHITE
tooltip_width = 150
tooltip_height = 50

# Image with frame settings for Magnifer
frame_thickness = 10
image_with_frame_surface = pygame.Surface((image_1_width + 2 * frame_thickness, image_1_height + 2 * frame_thickness), pygame.SRCALPHA)
image_with_frame_surface.fill((DARKGREY))
pygame.draw.rect(image_with_frame_surface, BLACK, (0, 0, image_with_frame_surface.get_width(), image_with_frame_surface.get_height()), frame_thickness)
image_with_frame_surface.blit(image_1, (frame_thickness, frame_thickness))

image_2 = pygame.image.load('medicine1.png') 
image_2_size = (200, 200)
image_2 = pygame.transform.scale(image_2, image_2_size)
image_2_width, image_2_height = image_2.get_size()
image_2_x = 390
image_2_y = (screen_height - image_1_height) // 2 + 150 

tooltip_text_2 = "Expired Med Kit: 50% chance to get heal or else deduct"

frame_thickness_2 = 10
frame_color_2 = BLACK
background_color_2 = DARKGREY 

image_with_frame_surface_2 = pygame.Surface((image_2_width + 2 * frame_thickness_2, image_2_height + 2 * frame_thickness_2), pygame.SRCALPHA)
image_with_frame_surface_2.fill(background_color_2)

pygame.draw.rect(image_with_frame_surface_2, frame_color_2, (0, 0, image_with_frame_surface_2.get_width(), image_with_frame_surface_2.get_height()), frame_thickness_2)

image_with_frame_surface_2.blit(image_2, (frame_thickness_2, frame_thickness_2))

image_3 = pygame.image.load('handsaw1.png') 
image_3_size = (200, 200)
image_3 = pygame.transform.scale(image_3, image_3_size)
image_3_width, image_3_height = image_3.get_size()
image_3_x = 700
image_3_y = (screen_height - image_1_height) // 2 + 150 

tooltip_text_3 = "Handsaw: double up the damage of the guns, high rick high reward"

frame_thickness_3 = 10
frame_color_3 = BLACK
background_color_3 = DARKGREY

image_with_frame_surface_3 = pygame.Surface((image_3_width + 2 * frame_thickness_3, image_3_height + 2 * frame_thickness_3), pygame.SRCALPHA)
image_with_frame_surface_3.fill(background_color_3)

pygame.draw.rect(image_with_frame_surface_3, frame_color_3, (0, 0, image_with_frame_surface_3.get_width(), image_with_frame_surface_3.get_height()), frame_thickness_3)

image_with_frame_surface_3.blit(image_3, (frame_thickness_3, frame_thickness_3))

#Import and resize images
kidnapperimage = pygame.image.load('kidnapper.png')
kidnapper = pygame.transform.scale(kidnapperimage,(500,500))

manimage = pygame.image.load('father.png')
man = pygame.transform.scale(manimage,(500,500))

monsterimage = pygame.image.load("monster.jpeg")
monster = pygame.transform.scale(monsterimage,(700,500))

heartsimage = pygame.image.load('hearts.png')
hearts = pygame.transform.scale(heartsimage, (50,50))

broken_hearts = pygame.image.load('broken_hearts.png')
broken_hearts = pygame.transform.scale(broken_hearts, (50,50))

dealer = pygame.image.load('dealer.png')
dealer = pygame.transform.scale(dealer, (200, 200))
dealer_rect = dealer.get_rect(topleft=(750, 300))

user = pygame.image.load('player.png')
user = pygame.transform.scale(user, (200, 200))
user_rect = user.get_rect(topleft=(50, 300))

#Display positions of images
player_x = 50
player_y = 200

debtorblood = pygame.image.load('debtorblood.png')
debtorblood = pygame.transform.scale(debtorblood, (200, 250))
debtorblood_rect = debtorblood.get_rect(topleft=(740, 285))

playerblood = pygame.image.load('playerblood.png')
playerblood = pygame.transform.scale(playerblood, (200, 300))
playerblood_rect = playerblood.get_rect(topleft=(50, 230))

handsaw1 = pygame.image.load('handsaw1.png')
handsaw1 = pygame.transform.scale(handsaw1, (100, 100))
handsaw1_rect = handsaw1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2 + 100))
handsaw2 = pygame.image.load('handsaw2.png')
handsaw2 = pygame.transform.scale(handsaw2, (100, 100))
handsaw2_rect = handsaw2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2 + 100))

medicine1 = pygame.image.load('medicine1.png')
medicine1 = pygame.transform.scale(medicine1, (100, 100))
medicine1_rect = medicine1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2))
medicine2 = pygame.image.load('medicine2.png')
medicine2 = pygame.transform.scale(medicine2, (100, 100))
medicine2_rect = medicine2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2))

magnifier1 = pygame.image.load('magnifier1.png')
magnifier1 = pygame.transform.scale(magnifier1, (100, 100))
magnifier1_rect = magnifier1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2 - 100))
magnifier2 = pygame.image.load('magnifier2.png')
magnifier2 = pygame.transform.scale(magnifier2, (100, 100))
magnifier2_rect = magnifier2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2 - 100))

# Define screen states
SCREEN_MAIN = 0
SCREEN_PLAY = 1
SCREEN_HOW_TO_PLAY = 2
SCREEN_STORY1 = 3
SCREEN_STORY2 = 4
SCREEN_STORY3 = 5
SCREEN_STORY4 = 6
SCREEN_STORY5 = 7
SCREEN_STORY6 = 8
SCREEN_PLAY1 = 9
SCREENNAME = 10
SCREENDISPLAY = 11
current_screen = SCREEN_MAIN


# Function to create a rounded rectangle
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

font2 = pygame.font.Font('DMRegular.ttf', 28)

def draw_custom_shape(surface, color, x, y, size):
    points = [
        (x, y - size // 3),              
        (x + size // 2, y - size // 3), 
        (x + size // 1.5, y),             
        (x + size // 2, y + size // 3),   
        (x, y + size // 3),              
        (x - size // 2, y + size // 3),   
        (x - size // 1.5, y),          
        (x - size // 2, y - size // 3)    
    ]
    pygame.draw.polygon(surface, color, points, 0)

# Function to wrap text
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        # Check the width of the current line with the next word added
        current_line.append(word)
        line_width, _ = font.size(' '.join(current_line))
        if line_width > max_width:
            # If it exceeds max width, add the line without the last word and start a new line
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))  # Add the last line
    return lines

def draw_multiline_text(surface, text, font2, color, x, y, max_width, line_spacing=5):
    lines = wrap_text(text, font2, max_width)
    total_height = len(lines) * font2.get_height() + (len(lines) - 1) * line_spacing
    start_y = y - total_height // 2
    
    for i, line in enumerate(lines):
        text_surface = font2.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, start_y + i * (font2.get_height() + line_spacing)))
        surface.blit(text_surface, text_rect)

# Function to create a speech bubble with multiple lines
def create_rounded_speech_bubble(text, x, y, width=200, height=100, corner_radius=10):
    # Create a surface for the speech bubble with transparency
    bubble_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    
    # Draw a rounded rectangle for the bubble
    draw_rounded_rect(bubble_surface, WHITE, bubble_surface.get_rect(), corner_radius)
    pygame.draw.rect(bubble_surface, BLACK, bubble_surface.get_rect(), 2, border_radius=corner_radius)
    
    # Wrap the text into multiple lines
    wrapped_lines = wrap_text(text, font, width - 20)  # Adjust for padding
    
    # Render each line
    for i, line in enumerate(wrapped_lines):
        line_surface = font.render(line, True, BLACK)
        line_rect = line_surface.get_rect(center=(width//2, 20 + i * 30))  # Adjust y position for each line
        bubble_surface.blit(line_surface, line_rect)

    #Draw the bubble on the screen
    screen.blit(bubble_surface, (x, y))
##########################################################################################################################################################################
# Function to create a speech bubble with multiple lines
def create_rounded_speech_bubble_2(text, x, y, width=200, height=100, corner_radius=10):
    bubble_surface_2 = pygame.Surface((width, height), pygame.SRCALPHA)

    # Draw a rounded rectangle for the bubble
    draw_rounded_rect(bubble_surface_2, DARKGREY, bubble_surface_2.get_rect(), corner_radius)
    pygame.draw.rect(bubble_surface_2, BLACK, bubble_surface_2.get_rect(), 6, border_radius=corner_radius)

    wrapped_lines_2 = wrap_text(text, font3, width - 20)  # Adjust for padding

    # Render each line
    for i, line_2 in enumerate(wrapped_lines_2):
        line_surface_2 = font3.render(line_2, True, BLACK)
        line_rect_2 = line_surface_2.get_rect(center=(width//2, 20 + i * 30)) 
        bubble_surface_2.blit(line_surface_2, line_rect_2)
    # Draw the bubble on the screen
    screen.blit(bubble_surface_2, (x, y))
##########################################################################################################################################################################
#Define initial hp
max_hp = 5
ai_hp = 3
player_hp = 3

turn = "player"
shoot_message = " "
ai_shoot_message = " "
medicine_message = ""  
medicine_display_time = 0  

# Time tracking for AI delay
ai_delay_start = 0
ai_delay_duration = 3000 
ai_waiting = False

# Time tracking for changing AI image
ai_hit_time = None
ai_blood_duration = 3000  

# Time tracking for changing player image
player_hit_time = None
player_blood_duration = 3000 

# Flags to control heart state
player_heart = hearts
ai_heart = hearts

# Flag to track if AI should continue its turn
ai_turn_ready = False

# Flag to track if the totem video is playing for heart restoration
playing_totem = False

# Flag to control if health should be restored
restore_after_video = False

# Initialize global variables for item usage flags
handsaw1_used_by_player = False
handsaw_damage_pending_player = False 
handsaw2_used_by_ai = False
handsaw_damage_pending_ai = False

global medicine1_used_by_player, medicine2_used_by_ai
medicine1_used_by_player = False
medicine2_used_by_ai = False

global magnifier1_used_by_player, magnifier2_used_by_ai
magnifier1_used_by_player = False
magnifier2_used_by_ai = False 

global magnifier_message, magnifier_display_time
magnifier_message = ""
magnifier_display_time = 0

# Function to draw health bars using hearts
def draw_health_bars():
    # Draw player hearts
    for i in range(max_hp):
        if i < player_hp:  # If the index is less than the current health, show intact heart
            screen.blit(hearts, (50 + i * 60, 50))  # Display intact hearts for player HP
        else:  # Otherwise, show broken hearts
            screen.blit(broken_hearts, (50 + i * 60, 50))  # Display broken hearts for lost HP

    # Draw AI hearts
    for i in range(max_hp):
        if i < ai_hp:  # If the index is less than the AI's health, show intact heart
            screen.blit(hearts, (900 - i * 60, 50))  # Display intact hearts for AI HP
        else:  # Otherwise, show broken hearts
            screen.blit(broken_hearts, (900 - i * 60, 50))

# Initialize global variables for health restoration and totem usage tracking
player_restored = False
ai_restored = False
player_totem_used = False  # Track if player has used the totem
ai_totem_used = False  # Track if AI has used the totem

# Initialize elimination tracking flags
player_can_be_eliminated = False  # Can player be eliminated after restoration?
ai_can_be_eliminated = False  # Can AI be eliminated after restoration?

class AI:
    def __init__(self):
        self.hp = 3  # Initial health value for AI
        self.game_over = False  # Start with game_over as False

    def check_if_game_over(self):
        if self.hp <= 0:
            self.game_over = True

    def reset(self):
        self.hp = 3
        self.game_over = False
        
class Player:
    def __init__(self):
        self.hp = 3  # Initial health value for the player
        self.game_over = False  # Start with game_over as False
        self.totem_used = False  # Track if the totem has been used
=======
        global current_screen, num_fake_bullets, num_real_bullets
        current_screen = SCREEN_MAIN
        num_real_bullets = 5
        num_fake_bullets = 3
        current_round = 1
        round_1()

#Reset hp for player
    def hp_reset(self):
        self.current_hp = max_hp

#Draw out defeated screen when player is defeated
    def draw_lose_screen(self):
        if self.game_over:
            screen.fill(BLACK)
            screen.blit(lose_text_surface, (lose_x, lose_y))
            pygame.display.update()
            pygame.time.delay(2000)
            self.reset

#AI class
class ai(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dealer
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width * 5 // 5.5, screen_height // 2)
        self.max_hp = ai_hp
        self.ai_current_hp = ai_hp
        self.ai_hp_positions = [(950, 0), (900, 0), (850, 0)]
        self.game_over = False


    def check_if_game_over(self):
        if self.hp <= 0 and self.totem_used:  # Only game over if the totem has been used
            self.game_over = True

    def restore_hp(self):
        if self.hp <= 0 and not self.totem_used:
            self.hp = 1
            self.totem_used = True

    def reset(self):
        self.hp = 3
        self.game_over = False
        self.totem_used = False

# Function to center the video on the screen
def center_video(video_clip, screen_width, screen_height):
    frame_time = (pygame.time.get_ticks() - video_start_time) / 1000.0
    if frame_time < video_clip.duration:
        frame = video_clip.get_frame(frame_time)
        frame_surface = get_frame_as_surface(frame)
        video_width, video_height = frame_surface.get_size()
        video_x = (screen_width - video_width) // 2  # Center the video horizontally
        video_y = (screen_height - video_height) // 2  # Center the video vertically
        screen.blit(frame_surface, (video_x, video_y))
        return True  # Video is still playing
    return False  # Video has finished

# Updated function to play the correct video (totem, handsaw1, handsaw2)
def play_video_in_center():
    global video_playing, current_video_clip
    if current_video_clip:
        if not center_video(current_video_clip, screen_width, screen_height):
            video_playing = False
            current_video_clip = None  # Video has finished playing

def handle_hp_restoration():
    global player_hp, player_can_be_eliminated, player_heart, playing_totem, player_restored, video_playing, current_video_clip, video_start_time, player_totem_used

    # If player's HP is zero, totem hasn't been used, and no video is playing, play totem video
    if player_hp <= 0 and not player_restored and not video_playing and not player_totem_used:
        current_video_clip = totem  # Set totem video
        video_playing = True  # Start video
        playing_totem = True  # Indicate that totem is playing
        video_start_time = pygame.time.get_ticks()  # Log the time video starts
        totem_sound.play()  # Play totem sound
    
    # After the totem video has finished, restore one health point (HP)
    if not video_playing and playing_totem:
        player_hp = 1  # Restore player HP to 1
        player_heart = hearts  # Restore one broken heart to full heart
        player_can_be_eliminated = True  # Player can now be eliminated on the next hit
        player_restored = True  # Mark the player as restored to prevent further totem use
        player_totem_used = True  # Mark the totem as used for the player
        playing_totem = False  # Stop the totem flag to prevent it from playing again
        print("Player's health restored by totem!")

    # Center the video on the screen while it's playing
    if video_playing and current_video_clip:
        frame_time = (pygame.time.get_ticks() - video_start_time) / 1000.0
        if frame_time < current_video_clip.duration:
            frame = current_video_clip.get_frame(frame_time)
            frame_surface = get_frame_as_surface(frame)
            video_width, video_height = frame_surface.get_size()
            video_x = (screen_width - video_width) // 2
            video_y = (screen_height - video_height) // 2
            screen.blit(frame_surface, (video_x, video_y))


def handle_hp_restoration():
    global player_hp, player_can_be_eliminated, player_heart, playing_totem, player_restored, video_playing, current_video_clip, video_start_time, player_totem_used

    # If player's HP is zero, totem hasn't been used, and no video is playing, play totem video
    if player_hp <= 0 and not player_restored and not video_playing and not player_totem_used:
        current_video_clip = totem  # Set totem video
        video_playing = True  # Start video
        playing_totem = True  # Indicate that totem is playing
        video_start_time = pygame.time.get_ticks()  # Log the time video starts
        totem_sound.play()  # Play totem sound
    
    # After the totem video has finished, restore one health point (HP)
    if not video_playing and playing_totem:
        player_hp = 1  # Restore player HP to 1
        player_heart = hearts  # Restore one broken heart to full heart
        player_can_be_eliminated = True  # Player can now be eliminated on the next hit
        player_restored = True  # Mark the player as restored to prevent further totem use
        player_totem_used = True  # Mark the totem as used for the player
        playing_totem = False  # Stop the totem flag to prevent it from playing again
        print("Player's health restored by totem!")

    if video_playing and current_video_clip:
        frame_time = (pygame.time.get_ticks() - video_start_time) / 1000.0
        if frame_time < current_video_clip.duration:
            frame = current_video_clip.get_frame(frame_time)
            frame_surface = get_frame_as_surface(frame)
            video_width, video_height = frame_surface.get_size()
            video_x = (screen_width - video_width) // 2
            video_y = (screen_height - video_height) // 2
            screen.blit(frame_surface, (video_x, video_y))

def handle_ai_hp_restoration():
    global ai_hp, ai_totem_used, ai_can_be_eliminated, ai_heart, playing_totem, video_playing, current_video_clip, video_start_time

    # If AI's HP is zero or below, totem hasn't been used, and no video is playing, play totem video
    if ai_hp <= 0 and not ai_totem_used and not video_playing:
        print("AI totem triggered")  # Debug message
        current_video_clip = totem  # Set totem video for AI
        video_playing = True  # Start video
        playing_totem = True  # Indicate that totem is playing
        video_start_time = pygame.time.get_ticks()  # Log the time video starts
        totem_sound.play()  # Play totem sound
        ai_totem_used = True  # Mark the totem as used for the AI
        ai_can_be_eliminated = True  # AI can now be eliminated on the next hit

    # After the totem video has finished, restore one health point (HP)
    if not video_playing and playing_totem:
        ai_hp = 1  # Restore AI HP to 1
        ai_heart = hearts  # Restore one broken heart to full heart
        ai_can_be_eliminated = True  # AI can now be eliminated on the next hit
        playing_totem = False  # Stop the totem flag to prevent it from playing again
        print("AI's health restored by totem!")

    # Center the video on the screen while it's playing
    if video_playing and current_video_clip:
        frame_time = (pygame.time.get_ticks() - video_start_time) / 1000.0
        if frame_time < current_video_clip.duration:
            frame = current_video_clip.get_frame(frame_time)
            frame_surface = get_frame_as_surface(frame)
            video_width, video_height = frame_surface.get_size()
            video_x = (screen_width - video_width) // 2
            video_y = (screen_height - video_height) // 2
            screen.blit(frame_surface, (video_x, video_y))

def handle_magnifier(who_used):
    global shoot_message, magnifier_message, magnifier_display_time
    bullet_type = current_bullet()  # Get current bullet type

    # Only check bullet type if in round 2
    if current_round == 2:
        if who_used == "player":
            if bullet_type == 1:  # Real bullet
                magnifier_message = "It's a Real Bullet!"
            else:  # Fake bullet
                magnifier_message = "It's a Fake Bullet!"
            magnifier_display_time = pygame.time.get_ticks()  # Track the time to display message

        elif who_used == "ai":
            if bullet_type == 1:  # Real bullet
                magnifier_message = "It's a Real Bullet!"
            else:  # Fake bullet
                magnifier_message = "It's a Fake Bullet!"

def render_magnifier_result():
    current_time = pygame.time.get_ticks()

    # Show the magnifier result message for 3 seconds
    if current_time - magnifier_display_time <= 3000:  # Display for 3 seconds
        box_width, box_height = 500, 50
        box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2 - 200, box_width, box_height)
        pygame.draw.rect(screen, LIGHTGREY, box_rect)

        # Change text color to WHITE for better visibility
        magnifier_surface = font_10.render(magnifier_message, True, WHITE)
        text_rect = magnifier_surface.get_rect(center=box_rect.center)
        screen.blit(magnifier_surface, text_rect.topleft)

def bullets_reset():
    global bullets, num_fake_bullets, num_real_bullets
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

def round_1():
    global turn, num_real_bullets, num_fake_bullets, bullets
    global handsaw1_used_by_player, handsaw_damage_pending_player
    global handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier2_used_by_ai, magnifier1_used_by_player

    num_real_bullets = 5
    num_fake_bullets = 3
    turn = "player"
    shoot_message = " "
    ai_shoot_message = " "
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    bullets_reset()
    
    # Ensure handsaw cannot be used in Round 1
    handsaw1_used_by_player = False
    handsaw_damage_pending_player = False
    handsaw2_used_by_ai = False
    handsaw_damage_pending_ai = False
    magnifier1_used_by_player = False
    magnifier2_used_by_ai = False


def round_2():
    global player_hp, ai_hp, num_real_bullets, num_fake_bullets, bullets, current_round
    global handsaw1_used_by_player, handsaw_damage_pending_player, handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier1_used_by_player, magnifier2_used_by_ai, totem_used

    print("Starting Round 2")

    # Restore HP for both player and AI
    player_hp = 3
    ai_hp = 3

    # Set the number of real and fake bullets for Round 2
    num_real_bullets = 3
    num_fake_bullets = 2
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

    # Reset handsaw and magnifier usage flags for Round 2
    handsaw1_used_by_player = False
    handsaw_damage_pending_player = False
    handsaw2_used_by_ai = False
    handsaw_damage_pending_ai = False
    magnifier1_used_by_player = False
    magnifier2_used_by_ai = False

    # Ensure that the totem can only be used once (either in Round 1 or Round 2)
    if totem_used:
        player_totem_used = True  # Mark as used to prevent further usage
        ai_totem_used = True  # Mark as used to prevent further usage

    # Update the current round
    current_round = 2
    turn = "player"

def round_3():
    global turn, num_real_bullets, num_fake_bullets, bullets
    global handsaw1_used_by_player, handsaw_damage_pending_player
    global handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier1_used_by_player, magnifier2_used_by_ai
    global player_totem_used, ai_totem_used

    print("Starting Round 3")
    num_real_bullets = 1
    num_fake_bullets = 1
    turn = "player"
    shoot_message = " "
    ai_shoot_message = " "
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    bullets_reset()

    # Reset all item usage flags for Round 3
    handsaw1_used_by_player = True  # Mark as used to prevent usage
    handsaw_damage_pending_player = False
    handsaw2_used_by_ai = True  # Mark as used to prevent usage
    handsaw_damage_pending_ai = False
    magnifier1_used_by_player = True  # Mark as used to prevent usage
    magnifier2_used_by_ai = True  # Mark as used to prevent usage

    # Prevent the use of the totem
    player_totem_used = True  # Mark as used to prevent usage
    ai_totem_used = True  # Mark as used to prevent usage

def check_game_over():
    global ai_hp, ai_can_be_eliminated, ai_totem_used, running, current_round

    # Lose condition: Player HP is 0 at any round and they've used the totem
    if player.hp <= 0 and player.totem_used:
        font_game_over = pygame.font.Font("Creepster.ttf", 100)
        game_over_surface = font_game_over.render("Game Over! You Lose!", True, RED)
        game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False  # Stop the game loop
        return

    # If AI HP is 0 and AI has already used the totem, progress to the next round
    if ai_hp <= 0:
        if current_round == 1 and not ai_totem_used:
            handle_ai_hp_restoration()  # AI uses the totem, if not already used
        elif current_round == 1 and ai_totem_used:
            current_round += 1
            round_2()  # Start Round 2
        elif current_round == 2 and ai_totem_used:
            current_round += 1
            round_3()  # Start Round 3
        elif current_round == 3:
            font_game_over = pygame.font.Font("Creepster.ttf", 100)
            congrats_surface = font_game_over.render("Congrats! You Win!", True, GREEN)
            congrats_rect = congrats_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(congrats_surface, congrats_rect)
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False  # Stop the game loop
            return

    # If the AI game is over after Round 1 or Round 2, proceed to the next round
    if ai.game_over:
        ai.reset()  # Reset AI for the next round
        current_round += 1  # Move to the next round
        if current_round == 2:
            round_2()  # Call the round_2 setup
        elif current_round == 3:
            round_3()  # Call the round_3 setup
        turn = "player"  # Set turn to the player
        shoot_message = None  # Reset shoot messages
        ai_shoot_message = None

    # Player's game over: Player loses if their HP is 0 at any round
    if player.game_over:
        font_game_over = pygame.font.Font("Creepster.ttf", 100)
        game_over_surface = font_game_over.render("Game Over! You Lose!", True, RED)
        game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False  # Stop the game loop
        return

def show_game_over(message):
    font_game_over = pygame.font.Font("Creepster.ttf", 100)
    game_over_surface = font_game_over.render(message, True, RED)
    game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    running = False  # Stop the game loop
    
def render_health_restoration():
    global playing_totem, player_restored, ai_restored, player_heart, ai_heart

    # After the totem video finishes, restore hearts if health was restored
    if not video_playing and playing_totem:
        if player_restored:
            player_heart = hearts  # Update to healthy heart
        if ai_restored:
            ai_heart = hearts  # Update to healthy heart
        playing_totem = False  # Reset totem flag

def render_player_image():
    current_time = pygame.time.get_ticks()
    
    # If the player has been hit recently, show playerblood for 3 seconds
    if player_hit_time and current_time - player_hit_time <= player_blood_duration:
        screen.blit(playerblood, playerblood_rect.topleft)
    else:
        screen.blit(user, user_rect.topleft)

def render_ai_image():
    current_time = pygame.time.get_ticks()
    
    # If the AI has been hit recently, show debtorblood for 3 seconds
    if ai_hit_time and current_time - ai_hit_time <= ai_blood_duration:
        screen.blit(debtorblood, debtorblood_rect.topleft)
    else:
        screen.blit(dealer, dealer_rect.topleft)

def restore_health():
    global player_hp, ai_hp, player_restored, ai_restored, player_heart, ai_heart, playing_totem

    if playing_totem:  # If the totem is currently playing
        if player_hp <= 0 and not player_restored:
            player_hp = 1  # Restore player HP to 1
            player_heart = hearts  # Update the heart to full
            player_restored = True  # Player has been restored once
        if ai_hp <= 0 and not ai_restored:
            ai_hp = 1  # Restore AI HP to 1
            ai_heart = hearts  # Update the heart to full
            ai_restored = True  # AI has been restored once
        playing_totem = False  # Reset the totem flag after restoring health

def handle_medicine(who_used):
    global current_video_clip, video_playing, video_start_time
    global player_hp, ai_hp, medicine_message, medicine_display_time
    medicine_outcome = random.choice(['heal', 'damage'])

    if who_used == "player":
        if medicine_outcome == 'heal':
            medicine_message = "Player healed! +1 HP"
            player_hp = min(player_hp + 1, max_hp)
        else:
            medicine_message = "Player damaged! -1 HP"
            player_hp -= 1
            if player_hp <= 0:
                handle_hp_restoration()

    elif who_used == "ai":
        if medicine_outcome == 'heal':
            medicine_message = "AI healed! +1 HP"
            ai_hp = min(ai_hp + 1, max_hp)
        else:
            medicine_message = "AI damaged! -1 HP"
            ai_hp -= 1
            if ai_hp <= 0:
                handle_ai_hp_restoration()

    # Set video
    current_video_clip = totem  # Replace with the correct video for medicine
    video_playing = True
    video_start_time = pygame.time.get_ticks()

    # Debug print
    print(f"Video playing: {video_playing}, Current Video Clip: {current_video_clip}")

    # Set the time when the medicine result should be displayed
    medicine_display_time = pygame.time.get_ticks()

def render_medicine_result():
    current_time = pygame.time.get_ticks()

    # Show the result message for 3 seconds
    if current_time - medicine_display_time <= 3000:  # Display for 3 seconds
        box_width, box_height = 500, 50
        box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2 - 200, box_width, box_height)
        pygame.draw.rect(screen, LIGHTGREY, box_rect)

        # Display the message text in white for better visibility
        medicine_surface = font_10.render(medicine_message, True, WHITE)
        text_rect = medicine_surface.get_rect(center=box_rect.center)
        screen.blit(medicine_surface, text_rect.topleft)

def handle_handsaw_usage(shooter, target):
    global shoot_message, player_hp, ai_hp, ai_hit_time, player_hit_time
    global num_real_bullets, num_fake_bullets
    global handsaw_damage_pending_player, handsaw_damage_pending_ai
    global magnifier2_used_by_ai, current_bullet  # Include necessary globals

    # Prevent AI from using handsaw if it revealed a fake bullet
    if shooter == "ai" and magnifier2_used_by_ai and current_bullet() == 0:
        return  # Exit without using handsaw

    # Randomly choose either a real bullet or a fake bullet, if available
    bullet_type = None
    if num_real_bullets > 0 and num_fake_bullets > 0:
        bullet_type = random.choice(['real', 'fake'])
    elif num_real_bullets > 0:
        bullet_type = 'real'
    elif num_fake_bullets > 0:
        bullet_type = 'fake'

    # Handling when a real bullet is chosen
    if bullet_type == 'real' and num_real_bullets > 0:
        num_real_bullets -= 1  # Deduct a real bullet
        gun_sound.play()

        if shooter == "player":
            if target == "ai":
                shoot_message = "Player used handsaw and shot AI with real bullets! AI -2 HP"
                ai_hp -= 2  # HP is deducted here
                ai_hit_time = pygame.time.get_ticks()  # Track AI shot time
            else:
                shoot_message = "Player used handsaw and shot themselves with real bullets! Player -2 HP"
                player_hp -= 2  # HP is deducted here
                player_hit_time = pygame.time.get_ticks()  # Track player shot time
                handsaw_damage_pending_player = False  # Reset the flag to prevent further damage
                return  # Exit after player shoots themselves

        elif shooter == "ai":
            if target == "player":
                shoot_message = "AI used handsaw and shot Player with real bullets! Player -2 HP"
                player_hp -= 2  # HP is deducted here
                player_hit_time = pygame.time.get_ticks()  # Track player shot time
            else:
                shoot_message = "AI used handsaw and shot itself with real bullets! AI -2 HP"
                ai_hp -= 2  # HP is deducted here

    # Handling when a fake bullet is chosen (No HP deduction)
    elif bullet_type == 'fake' and num_fake_bullets > 0:
        num_fake_bullets -= 1  # Deduct a fake bullet
        emptygun_sound.play()

        if shooter == "player":
            if target == "ai":
                shoot_message = "Player used handsaw and shot AI with fake bullets! Nothing happened."
            else:
                shoot_message = "Player used handsaw and shot themselves with fake bullets! Nothing happened."
                handsaw_damage_pending_player = False  # Reset the flag to prevent further actions
                return  # Exit after player shoots themselves

        elif shooter == "ai":
            if target == "player":
                shoot_message = "AI used handsaw and shot Player with fake bullets! Nothing happened."
            else:
                shoot_message = "AI used handsaw and shot itself with fake bullets! Nothing happened."

    # After any shot, check if the player or AI needs to be restored or eliminated
    handle_hp_restoration()
    handle_ai_hp_restoration()
    check_game_over()

    # Reset the handsaw damage flags after usage to avoid multiple damage
    handsaw_damage_pending_player = False
    handsaw_damage_pending_ai = False

def player_turn():
    global turn, handsaw1_used_by_player, handsaw_damage_pending_player, num_real_bullets, num_fake_bullets
    global player_hp, ai_hp, player_hit_time, ai_hit_time, player_heart, ai_heart
    global medicine1_used_by_player, medicine_display_time, gun_sound, emptygun_sound, shoot_message
    global ai_waiting, ai_delay_start, video_playing, current_video_clip, video_start_time
    global magnifier1_used_by_player, current_round  # Track if magnifier has been used

    mouse_pos = pygame.mouse.get_pos()

    # Prevent rapid shooting by adding a cooldown
    current_time = pygame.time.get_ticks()

    # Medicine can only be used in Round 1
    if current_round == 1 and medicine1_rect.collidepoint(mouse_pos) and not medicine1_used_by_player:
        handle_medicine("player")  # Apply medicine effects
        medicine1_used_by_player = True
        medicine_display_time = pygame.time.get_ticks()
        return  # Player continues the turn after using medicine

    # Magnifier and handsaw can only be used in Round 2
    if current_round == 2:
        # Player uses the magnifier
        if magnifier1_rect.collidepoint(mouse_pos) and not magnifier1_used_by_player:
            handle_magnifier("player")  
            magnifier1_used_by_player = True 

        # Player uses the handsaw
        if handsaw1_rect.collidepoint(mouse_pos) and not handsaw1_used_by_player:
            handsaw1_used_by_player = True
            handsaw_damage_pending_player = True
            handsaw_sound.play()
            video_playing = True
            current_video_clip = handsawvideo1
            video_start_time = pygame.time.get_ticks()
            return  # Exit to wait for video

    # If handsaw video finished, player chooses target
    if handsaw_damage_pending_player:
        if user_rect.collidepoint(mouse_pos):  # Player shoots themselves
            handle_handsaw_usage("player", "player")
        elif dealer_rect.collidepoint(mouse_pos):  # Player shoots AI
            handle_handsaw_usage("player", "ai")
            handsaw_damage_pending_player = False
            turn = "ai"
            return

    # Cooldown between shooting actions
    if player_hit_time and current_time - player_hit_time < 500:  # Add a 0.5 second cooldown
        return  # Skip the rest of the logic during cooldown

    # Player shoots themselves or the AI
    if user_rect.collidepoint(mouse_pos):  # Player shoots themselves
        bullet_type = random.choice(['real', 'fake'])
        if bullet_type == 'real' and num_real_bullets > 0:
            num_real_bullets -= 1
            gun_sound.play()
            shoot_message = "You shot yourself with a real bullet!"
            player_hp -= 1
            player_hit_time = pygame.time.get_ticks()
            player_heart = broken_hearts
            if player_hp <= 0:
                handle_hp_restoration()
            check_game_over()
        elif bullet_type == 'fake' and num_fake_bullets > 0:
            num_fake_bullets -= 1
            emptygun_sound.play()
            shoot_message = "You shot yourself with a fake bullet!"
        return  # Player keeps the turn

    elif dealer_rect.collidepoint(mouse_pos):  # Player shoots the AI
        bullet_type = 'real' if num_real_bullets > 0 else 'fake'
        if bullet_type == 'real':
            num_real_bullets -= 1
            gun_sound.play()
            shoot_message = "You shot the AI with a real bullet!"
            ai_hp -= 1
            ai_hit_time = pygame.time.get_ticks()
            ai_heart = broken_hearts
            if ai_hp <= 0:
                handle_ai_hp_restoration()
            check_game_over()
        elif bullet_type == 'fake':
            num_fake_bullets -= 1
            emptygun_sound.play()
            shoot_message = "You shot the AI with a fake bullet!"

        turn = "ai"
        ai_delay_start = pygame.time.get_ticks()
        ai_waiting = True

def ai_turn():
    global turn, num_real_bullets, num_fake_bullets, ai_shoot_message, player_hp, ai_hp
    global handsaw2_used_by_ai, handsaw_damage_pending_ai, video_playing, current_video_clip, video_start_time
    global ai_hit_time, player_hit_time, ai_heart, player_heart, ai_waiting, medicine2_used_by_ai
    global magnifier2_used_by_ai, medicine_message, medicine_display_time, current_round  # Include necessary globals

    ai_shoot_message = ""  # Reset AI shoot message
    ai_turn_start_time = pygame.time.get_ticks()  # Start the timer for the AI's turn

    # Medicine can only be used in Round 1
    if current_round == 1 and ai_hp < 2 and not medicine2_used_by_ai:
        handle_medicine("ai")  
        medicine2_used_by_ai = True  
        medicine_display_time = pygame.time.get_ticks()  
        return  # AI continues its turn after using medicine

    # Magnifier and handsaw can only be used in Round 2
    if current_round == 2:
        if ai_hp < 2 and not magnifier2_used_by_ai:
            handle_magnifier("ai")  # AI checks bullet type
            magnifier2_used_by_ai = True  # Mark magnifier as used

        if magnifier2_used_by_ai and current_bullet() == 1 and not handsaw2_used_by_ai:  # Only use handsaw if the bullet is real
            handsaw2_used_by_ai = True  # Mark handsaw as used
            handsaw_damage_pending_ai = True  # Indicate damage will happen after target selection
            handsaw_sound.play()  # Play the handsaw sound
            video_playing = True  # Set video playing state to true
            current_video_clip = handsawvideo2  # Set the correct video for handsaw
            video_start_time = pygame.time.get_ticks()  # Track the start time of the video
            return  # Exit the function to wait for target selection after the video

    # Check the elapsed time for AI decision-making
    elapsed_time = pygame.time.get_ticks() - ai_turn_start_time
    if elapsed_time >= 3000:  # 3 seconds limit for shooting
        # AI proceeds with the shooting logic
        bullet_type = random.choice(['real', 'fake'])  # AI randomly selects real or fake bullet

        if bullet_type == 'real' and num_real_bullets > 0:  # AI shoots player with real bullet
            num_real_bullets -= 1
            player_hp -= 2  # Apply -2 HP to Player
            player_hit_time = pygame.time.get_ticks()  # Track player shot time
            player_heart = broken_hearts  # Update player's heart to broken
            gun_sound.play()  # Play gun sound for real bullet
            ai_shoot_message = "AI shot Player with a real bullet! Player -2 HP"
            if player_hp <= 0:
                handle_hp_restoration()  # Handle player health restoration if necessary
            check_game_over()  # Check if game is over

        elif bullet_type == 'fake' and num_fake_bullets > 0:  # AI shoots player with fake bullet
            num_fake_bullets -= 1
            emptygun_sound.play()  # Play empty gun sound for fake bullet
            ai_shoot_message = "AI shot Player with a fake bullet! Nothing happened."

        handsaw_damage_pending_ai = False  # Reset the handsaw flag
        turn = "player"  # Return to player's turn
        return

    # If no items are used, AI will decide to shoot
    available_bullet_types = []
    if num_real_bullets > 0:
        available_bullet_types.append('real')
    if num_fake_bullets > 0:
        available_bullet_types.append('fake')

    if not available_bullet_types:
        ai_shoot_message = "AI has no bullets left!"
        turn = "player"
        return

    bullet_type = random.choice(available_bullet_types)

    if bullet_type == 'real':
        num_real_bullets -= 1
        gun_sound.play()
        ai_shoot_message = "AI shot you with a real bullet!"
        player_hp -= 1
        player_hit_time = pygame.time.get_ticks()
        player_heart = broken_hearts  # Player heart becomes broken
        if player_hp <= 0:
            handle_hp_restoration()  # Use player's totem if available
        check_game_over()  # Check if game is over
        turn = "player"  # Change turn to the player
    elif bullet_type == 'fake':
        num_fake_bullets -= 1
        emptygun_sound.play()
        ai_shoot_message = "AI shot you with a fake bullet!"
        turn = "player"  # Change turn to the player

    ai_waiting = False  # Reset AI waiting flag

#Create player and AI objects
player = Player()
ai = AI()

#Group the sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ai)

##########################################################################################################################################################################
font_10 = pygame.font.Font("Gloria.ttf", 47)
input_font_name = pygame.font.Font("Gloria.ttf", 50)

def player_name():
    input_box = pygame.Rect(screen_width // 2 - 300, screen_height // 2 - 75, 600, 120)
    color_inactive = pygame.Color(WHITE)
    color_active = pygame.Color(LIGHTRED)
    color = color_inactive
    active = False
    text = ' '
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    sound_clickbox.play()
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        delete_sound.play()
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        sound_clickbox.play()
                        return text
                    else:
                        text += event.unicode
                        delete_sound.play()

        screen.fill(BLACK)
        txt_surface = input_font_name.render(text, True, color)
        width = max(600, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 10)
        screen.blit(text_11_surface,(text_11_button_x, text_11_button_y))

        pygame.display.flip()
        clock.tick(30)

def SCREENDISPLAY(name):
    clock = pygame.time.Clock()
    global current_screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Check if the mouse click is on the "Next" button
                if text_5_button_rect.collidepoint(mouse_pos):
                    sound_next.play()
                    current_screen = SCREEN_PLAY1 
                    pygame.display.set_caption('Storyline')
                    return

        screen.fill(BLACK)
        name_surface = font_10.render(f'Hello{name}, Welcome to Life Roulette', True, RED)
        screen.blit(name_surface, (screen_width // 2 - name_surface.get_width() // 2, screen_height // 2 - name_surface.get_height() // 2))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))

        pygame.display.flip()
        clock.tick(30)
##########################################################################################################################################################################
# Bullet setting for round 1
bullets = []
num_real_bullets = 5
num_fake_bullets = 3

#Define the array for bullets
bullets = [1] * num_real_bullets + [0] * num_fake_bullets

#Define the turn
turn = "player"

#Message given by system
shoot_message = " "
ai_shoot_message = " "
shoot_message_time = 0  
ai_shoot_message_time = 0  

#Define the rounds
current_round = 1

#Define for reset bullets for every round
def bullets_reset():
    global bullets, num_fake_bullets, num_real_bullets
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

#Showcase for round 1
def round_1():
    print("Starting Round 1")
    global turn, num_real_bullets, num_fake_bullets, bullets
    num_real_bullets = 5
    num_fake_bullets = 3
    turn = "player"
    shoot_message = " "
    ai_shoot_message = " "
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    bullets_reset()
    
 
def round_2():
    global turn, num_real_bullets, num_fake_bullets, bullets, current_round
    global handsaw1_used_by_player, handsaw_damage_pending_player, handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier1_used_by_player, magnifier2_used_by_ai

    print("Starting Round 2")

    # Restore HP for both player and AI
    player_hp = 3
    ai_hp = 3

    # Set the number of real and fake bullets for Round 2
    num_real_bullets = 3
    num_fake_bullets = 2
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

    # Reset handsaw and magnifier usage flags for Round 2
    handsaw1_used_by_player = False
    handsaw_damage_pending_player = False
    handsaw2_used_by_ai = False
    handsaw_damage_pending_ai = False
    magnifier1_used_by_player = False
    magnifier2_used_by_ai = False

    # Update the current round
    current_round = 2
    turn = "player"

def round_3():
    global turn, num_real_bullets, num_fake_bullets, bullets
    global handsaw1_used_by_player, handsaw_damage_pending_player
    global handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier1_used_by_player, magnifier2_used_by_ai
    global player_totem_used, ai_totem_used

    print("Starting Round 3")
    num_real_bullets = 1
    num_fake_bullets = 1
    turn = "player"
    shoot_message = " "
    ai_shoot_message = " "
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    bullets_reset()

    # Reset all item usage flags for Round 3
    handsaw1_used_by_player = True  # Mark as used to prevent usage
    handsaw_damage_pending_player = False
    handsaw2_used_by_ai = True  # Mark as used to prevent usage
    handsaw_damage_pending_ai = False
    magnifier1_used_by_player = True  # Mark as used to prevent usage
    magnifier2_used_by_ai = True  # Mark as used to prevent usage

    # Prevent the use of the totem
    player_totem_used = True  # Mark as used to prevent usage
    ai_totem_used = True  # Mark as used to prevent usage
    current_round = 3
    turn = "player"

#To track the current bullet that player is holding
next_bullet_type = None

# Define the function of what is the current bullet that player is handling
def current_bullet():
    global bullets

    if bullets:
        return bullets[0]  # Return the type of the current bullet (1 for real, 0 for fake)
    else:
        return None  # Return None if there are no bullets left

=======
    global turn, num_real_bullets, num_fake_bullets, bullets
    num_real_bullets = 5
    num_fake_bullets = 3
    turn = "player"
    shoot_message = " "
    ai_shoot_message = " "
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    bullets_reset()
 
#Showcase for round 2
def round_2():
    screen.blit(round_2_surface, (round_2_x,round_2_y))
    pygame.display.update()
    pygame.time.delay(2000)
    global turn, num_real_bullets, num_fake_bullets, bullets
    num_real_bullets = 3
    num_fake_bullets = 2
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    turn = "player"
    shoot_message = " "
    ai_shoot_message = " "
    if current_round == 2:
        magnifier_button()
    bullets_reset()

#Showcase for round 3 (Final Round)
def round_3():
    screen.blit(round_3_surface, (round_3_x, round_3_y))
    pygame.display.update()
    pygame.time.delay(2000)
    global turn, num_real_bullets, num_fake_bullets, bullets
    #Define the new max hp for player and ai in the last round
    player.max_hp = 1
    player.current_hp = player.max_hp
    ai.max_hp = 1
    ai.ai_current_hp = ai.max_hp
    num_real_bullets = 1
    num_fake_bullets = 1
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    turn = "player"
    shoot_message = " "
    ai_shoot_message = " "
    bullets_reset()

#To track the current bullet that player is holding
next_bullet_type = None

#Define the function of what is the current bullet that player is handling
def current_bullet():
    global bullets, next_bullet_type, shoot_message

    if bullets:
        next_bullet_type = bullets[0]
        if next_bullet_type == 1:
            shoot_message = "This is a real bullet."

        else:
            shoot_message = "This is a fake bullet."
    else:
        return "No bullet left."


#Define the function of bullet
def bullet():
    global num_real_bullets, num_fake_bullets, shoot_message, turn, bullets, next_bullet_type
    mouse_pos = pygame.mouse.get_pos()


    # Click on Image
    if image_4_x <= mouse_pos[0] <= image_4_x + image_4_width and image_4_y <= mouse_pos[1] <= image_4_y + image_4_height:

        if bullets:
            bullet_type = bullets.pop(0)

            if bullet_type == 1:
                num_real_bullets -= 1
                gun_sound.play()
                shoot_message = (f"{name} shot a real bullet!")
                ai.ai_current_hp -= 1

            else:
                num_fake_bullets -= 1
                emptygun_sound.play()
                shoot_message = (f"{name} shot a fake bullet!")

            turn = "ai"

        else:
            shoot_message = "No bullets left!"

    return shoot_message

#Define for AI to fire 
def ai_fire():

    global num_real_bullets, num_fake_bullets, ai_shoot_message, turn, bullets

#Make the turn to player once ai is defeated
    if ai.ai_current_hp <= 0:
        turn = "player"
        return

    if bullets:
        bullet_type = bullets.pop(0)
        if bullet_type == 1:
            num_real_bullets -= 1
            gun_sound.play()
            ai_shoot_message = "Debtor shot a Real bullet!"
            player.current_hp -= 1

        else:
            num_fake_bullets -= 1
            emptygun_sound.play()
            ai_shoot_message = "Debtor shot a Fake bullet!"
                
    else:
        ai_shoot_message = "Debtor has no bullets left!"    
        turn = "player"
    return shoot_message

def draw_game_state():
    screen.blit(text_8_surface, (text_8_button_x, text_8_button_y))
    real_bullets_text = font_12.render(f"Real Bullets: {num_real_bullets}", True, WHITE)
    fake_bullets_text = font_12.render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
    screen.blit(real_bullets_text, (10, 50))
    screen.blit(fake_bullets_text, (300, 50))
    screen.blit(image_with_frame_surface_4, (image_4_x, image_4_y))
    shoot_message_text = font_12.render(shoot_message, True, WHITE)
    screen.blit(shoot_message_text, (10, 100))
    ai_shoot_message_text =font_12.render(ai_shoot_message, True, WHITE)
    screen.blit(ai_shoot_message_text, (625, 100))
    pygame.display.update()


##########################################################################################################################################################################
# IMPORTANT!!!
video_playing = False
current_video_clip = None
video_start_time = 0

show_input_box = False
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Settings for click on Play and move to storyline
            if current_screen == SCREEN_MAIN:
                if button_text2_rect.collidepoint(event.pos):
                    sound_play.play()
                    current_screen = SCREEN_PLAY1
                    pygame.display.set_caption('Storyline')

                # Settings for How to Play and How to Play Back
                elif button_text3_rect.collidepoint(event.pos):
                    sound_how_to_play.play()
                    current_screen = SCREEN_HOW_TO_PLAY
                    pygame.display.set_caption('How to Play')
            elif current_screen == SCREEN_HOW_TO_PLAY:
                if text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

                # Setting for Play and move to Story 1 and Screen Play back to Main
            elif current_screen == SCREEN_PLAY:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_next.play()
                    current_screen = SCREEN_STORY1
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

                # Setting for Story 1 and move to Story 2 and Story 1 back to Play
            elif current_screen == SCREEN_STORY1:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_next.play()
                    current_screen = SCREEN_STORY2
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_PLAY
                    pygame.display.set_caption('Storyline')

            elif current_screen == SCREEN_STORY2:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY3
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY1
                    pygame.display.set_caption('Storyline')
            
            elif current_screen == SCREEN_STORY3:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY4
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY2
                    pygame.display.set_caption('Storyline')

            elif current_screen == SCREEN_STORY4:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    show_input_box = True
                    current_screen = SCREENNAME
                    pygame.display.set_caption('Enter your Name')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY3
                    pygame.display.set_caption('Storyline')

            elif current_screen == SCREENNAME:
                name = player_name()
                SCREENDISPLAY(name)
            
            elif current_screen == SCREEN_PLAY1:
                if text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')
                if current_screen == SCREEN_PLAY1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if turn == "player":
                            player_turn()
                            
                        if current_round == 1:
                        # Draw medicine for round 1
                            if not medicine1_used_by_player:
                                screen.blit(medicine1, medicine1_rect)
                            if not medicine2_used_by_ai:
                                screen.blit(medicine2, medicine2_rect)

        if turn == "ai" and not ai_waiting:
            ai_delay_start = pygame.time.get_ticks()  # Start delay timer
            ai_waiting = True  # Set AI as waiting for delay

        if turn == "ai" and ai_waiting:
            current_time = pygame.time.get_ticks()
            # Check if 3 seconds have passed since AI's turn started
            if current_time - ai_delay_start >= ai_delay_duration:
                ai_turn()  # AI chooses who to shoot again after 3-second delay
                ai_waiting = False  # Reset waiting for the next turn

            if current_screen == SCREEN_PLAY1:

                if video_playing:
                    play_video_in_center()  # Render the video in the center
                else:
                    if current_round == 1:
                    # Logic for round 1
                        render_health_restoration()
                    elif current_round == 2:
                        # Logic for round 2
                        render_health_restoration()
                    elif current_round == 3:
                    # Logic for final round
                        render_health_restoration()

                # Apply handsaw damage after video finishes, based on player's and AI's target
                if handsaw_damage_pending_player:
                    if user_rect.collidepoint(pygame.mouse.get_pos()):  # Player shoots themselves
                        if num_real_bullets > 0:
                            num_real_bullets -= 1
                            player_hp -= 2  # Apply -2 HP to Player
                            player_hit_time = pygame.time.get_ticks()
                            player_heart = broken_hearts
                            gun_sound.play()
                        else:
                            emptygun_sound.play()  # If no real bullets, play empty sound
                        if player_hp <= 0:
                            handle_hp_restoration()  # Handle player health restoration if necessary
                        check_game_over()  # Check if game over
                    elif dealer_rect.collidepoint(pygame.mouse.get_pos()):  # Player shoots AI
                        if num_real_bullets > 0:
                            num_real_bullets -= 1
                            ai_hp -= 2  # Apply -2 HP to AI
                            ai_hit_time = pygame.time.get_ticks()
                            ai_heart = broken_hearts
                            gun_sound.play()
                        else:
                            emptygun_sound.play()  # If no real bullets, play empty sound
                        if ai_hp <= 0:
                            handle_ai_hp_restoration()  # Handle AI health restoration if necessary
                    check_game_over()  # Check if game over

                    handsaw_damage_pending_player = False  # Reset the flag
                    turn = "ai"  # Change turn to AI after player finishes

                elif handsaw_damage_pending_ai:
                    # AI chooses target (player) and applies -2 HP after handsaw video
                    if num_fake_bullets <= 0 or random.choice([True, False]):  # AI shoots player when fake bullets are gone or randomly
                        if num_real_bullets > 0:
                            num_real_bullets -= 1
                            player_hp -= 2  # Apply -2 HP to Player
                            player_hit_time = pygame.time.get_ticks()
                            player_heart = broken_hearts
                            gun_sound.play()
                        else:
                            emptygun_sound.play()  # If no real bullets, play empty sound
                        if player_hp <= 0:
                            handle_hp_restoration()  # Handle player health restoration if necessary
                    check_game_over()  # Check if game over

                    handsaw_damage_pending_ai = False  # Reset the flag
                    turn = "player"  # Return to player's turn after AI shoots

                        # If playing the totem, restore health after video finishes
                if playing_totem:
                    handle_hp_restoration()  # Handle player's totem-based restoration
                    handle_ai_hp_restoration()  

        render_health_restoration()
        restore_health()

        # After the video finishes, check if the game is over
        check_game_over() 
    
        if video_playing:
            print("Playing video...")
            screen.fill((0, 0, 0))
                            
    if current_screen == SCREEN_HOW_TO_PLAY:
        image_rect = pygame.Rect(image_1_x, image_1_y, image_1_width + 2 * frame_thickness, image_1_height + 2 * frame_thickness)
        if image_rect.collidepoint(mouse_x, mouse_y):
            tooltip_surface, tooltip_rect = tooltip_font.render(tooltip_text, fgcolor=tooltip_text_color, bgcolor=tooltip_bg_color)
            tooltip_rect.topleft = (mouse_x + 10, mouse_y + 10)  
            tooltip_x = mouse_x - tooltip_width // 2
            screen.blit(tooltip_surface, tooltip_rect)
    
        image_rect_2 = pygame.Rect(image_2_x, image_2_y, image_2_width + 2 * frame_thickness_2, image_2_height + 2 * frame_thickness_2)
        if image_rect_2.collidepoint(mouse_x, mouse_y):
            tooltip_surface_2, tooltip_rect_2 = tooltip_font.render(tooltip_text_2, fgcolor=tooltip_text_color, bgcolor=tooltip_bg_color)
            tooltip_rect_2.topright = (mouse_x -10, mouse_y - 10)

        image_rect_3 = pygame.Rect(image_3_x, image_3_y, image_3_width + 2 * frame_thickness_3, image_3_height + 2 * frame_thickness_3)
        if image_rect_3.collidepoint(mouse_x, mouse_y):
            tooltip_surface_3, tooltip_rect_3 = tooltip_font.render(tooltip_text_3, fgcolor=tooltip_text_color, bgcolor=tooltip_bg_color)
            tooltip_rect_3.topright = (mouse_x -10, mouse_y - 10)
            screen.blit(tooltip_surface_3, tooltip_rect_3)

    # Current screen update
    screen.fill(BLACK)
    if current_screen == SCREEN_MAIN:
        screen.fill(BLACK)
        screen.blit(text_1_surface, (text_1_x, text_1_y)) 
        screen.blit(text_2_surface, (text_2_x, text_2_y)) 
        screen.blit(text_3_surface, (text_3_x, text_3_y))  
        
        # Get the current frame
        current_time = pygame.time.get_ticks() / 1000.0  # Convert milliseconds to seconds
        frame_time = current_time % video_clip.duration  # Loop video
        frame = video_clip.get_frame(frame_time)
        
        # Convert frame to Pygame surface
        frame_surface = get_frame_as_surface(frame)
        
        # Clear the screen
        screen.fill(TRANSPARENT)
        
        # Draw the video frame
        screen.blit(frame_surface, (0, 0))
        screen.blit(transparent_surface, (0, 0))
        
        # Draw both text surfaces
        screen.blit(text_1_surface, (text_1_x, text_1_y))  
        screen.blit(text_2_surface, (text_2_x, text_2_y))  
        screen.blit(text_3_surface, (text_3_x, text_3_y))  

    elif current_screen == SCREEN_PLAY:
        # Render the Play screen
        screen.fill(BLACK)
        play_1_text = ""
        play_1_text_surface = font_2.render(play_1_text, True, GREEN)
        play_1_text_width, play_text_height = play_1_text_surface.get_size()
        play_1_text_x = (screen_width - play_1_text_width) // 2
        play_1_text_y = (screen_height - play_text_height) // 2
        screen.blit(play_1_text_surface, (play_1_text_x, play_1_text_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))  
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(kidnapper, (player_x, player_y))
        create_rounded_speech_bubble("Well, well, look who's finally answering his phone. Your little girl is with me now. You know why, don't you? You owe me RM10,000,000. And with that juicy 20% interest, it's now over RM12,000,000. You've been dodging me for months, wasting your money at the tables. But guess what? Your luck just ran out.",
        player_x + 400, player_y - 150, width=400, height=230)
        draw_custom_shape(screen, WHITE, 700, 490, 200)
        draw_multiline_text(screen, "Dad, please! Help me!", font2, RED, 700, 500, max_width=140)
        
    elif current_screen == SCREEN_HOW_TO_PLAY:
        # Show on How to Play screen 
        screen.fill(CHARCOAL)
        how_text1_ = "Game Introduction"
        how_text1_surface = font_3.render(how_text1_, True, WHITE)
        how_text1_width, how_to_play_1_height = how_text1_surface.get_size()
        how_text1_x = (screen_width - how_text1_width) // 2
        how_text1_y = (screen_height - how_to_play_1_height) // 2 -350
        how_text2_ = "Items Introduction"
        how_text2_surface = font_3.render(how_text2_, True, WHITE)
        how_text2_width, how_to_play_2_height = how_text2_surface.get_size()
        how_text2_x = (screen_width - how_text2_width) // 2
        how_text2_y = (screen_height - how_to_play_2_height) // 2 
        how_text3_ = "Notes: There will be hidden objects; grab them if you see them. GOOD LUCK"
        how_text3_surface = font_13.render(how_text3_, True, BLACK)
        how_text3_width, how_to_play_3_height = how_text3_surface.get_size()
        how_text3_x = (screen_width - how_text3_width) // 2
        how_text3_y = (screen_height - how_to_play_3_height) // 2 - 60
        screen.blit(how_text1_surface, (how_text1_x, how_text1_y))
        screen.blit(how_text2_surface, (how_text2_x, how_text2_y))
        screen.blit(how_text3_surface, (how_text3_x,how_text3_y))
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y)) 
        screen.blit(image_with_frame_surface, (image_1_x, image_1_y))
        screen.blit(image_with_frame_surface_2, (image_2_x, image_2_y))
        screen.blit(image_with_frame_surface_3, (image_3_x, image_3_y))
        create_rounded_speech_bubble_2("The game consists of three rounds. At the start of the round, the dealer loads the shotgun with a certain amount of real bullets and fake bullets in random order. Players then ask to choose either to shoot the dealer or themselves. Depending on whether the player chooses to shoot themselves or the dealer, if the bullet is real, then either the dealer or the player will lose a life. Each player has a certain amount of life depending on the round. Starting on round 2, a set of items will be distributed to you and the dealer. Every item will give you a different advantage.",
        player_x +6 , player_y -100 , width=900, height=200)

        # Tooltip logic
        image_1_rect = pygame.Rect(image_1_x, image_1_y, image_1_width + 2 * frame_thickness, image_1_height + 2 * frame_thickness)
        if image_1_rect.collidepoint(mouse_x, mouse_y):
            tooltip_surface, tooltip_rect = tooltip_font.render(tooltip_text, fgcolor=tooltip_text_color, bgcolor=tooltip_bg_color)
            tooltip_rect.topleft = (mouse_x + 10, mouse_y + 10)  
            screen.blit(tooltip_surface, tooltip_rect)
        
        image_2_rect = pygame.Rect(image_2_x, image_2_y, image_2_width + 2 * frame_thickness_2, image_2_height + 2 * frame_thickness_2)
        if image_2_rect.collidepoint(mouse_x, mouse_y):
            tooltip_surface_2, tooltip_rect_2 = tooltip_font.render(tooltip_text_2, fgcolor=tooltip_text_color, bgcolor=tooltip_bg_color)
            tooltip_rect_2.topleft = (mouse_x -10, mouse_y -10)
            screen.blit(tooltip_surface_2, tooltip_rect_2)

        image_rect_3 = pygame.Rect(image_3_x, image_3_y, image_3_width + 2 * frame_thickness_3, image_3_height + 2 * frame_thickness_3)
        if image_rect_3.collidepoint(mouse_x, mouse_y):
            tooltip_surface_3, tooltip_rect_3 = tooltip_font.render(tooltip_text_3, fgcolor=tooltip_text_color, bgcolor=tooltip_bg_color)
            tooltip_rect_3.topright = (mouse_x -10, mouse_y - 10)
            screen.blit(tooltip_surface_3, tooltip_rect_3)

    elif current_screen == SCREEN_STORY1:
        # Show on Play Screen
        screen.fill(BLACK)
        how_to_play_text = "Storyline"
        how_to_play_surface = font_3.render(how_to_play_text, True, WHITE)
        how_to_play_width, how_to_play_height = how_to_play_surface.get_size()
        how_to_play_x = (screen_width - how_to_play_width) // 2
        how_to_play_y = (screen_height - how_to_play_height) // 2 -350
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(man, (player_x, player_y))
        create_rounded_speech_bubble("Please, I... I don't have that kind of money right now. Just let her go! I need more time—ten days! Just ten days, and I’ll get you your money!",
        player_x + 400, player_y - 90, width=400, height=130)
          
    elif current_screen == SCREEN_STORY2:
        # Show on Story 2 Screen
        screen.fill(BLACK)
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(kidnapper, (player_x, player_y))
        create_rounded_speech_bubble("Time? Do you think you can bargain with me? Here's the deal—you don't have a choice. If you want your daughter back, you'll play a little game with me. A game of life and death. Win, and I'll give you 20 days to raise the money. Lose... and your daughter won't live to see tomorrow.",
        player_x + 400, player_y - 150, width=410, height=200)

    elif current_screen == SCREEN_STORY3:
        # Show on Story 3 Screen
        screen.fill(BLACK) 
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(man, (player_x, player_y))
        create_rounded_speech_bubble("I’ll do it. I’ll play your game. Just don’t hurt her, please!!",
        player_x + 400, player_y - 90, width=400, height=100)

    elif current_screen == SCREEN_STORY4:
        # Show on Story 4 Screen
        screen.fill(BLACK) 
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))
        screen.blit(monster, (player_x, player_y)) 
        draw_custom_shape(screen, WHITE, 700, 300, 200)
        draw_multiline_text(screen, "Good. Then let's begin.", font2, RED, 700, 300, max_width=140)

    elif current_screen == SCREENNAME:
        # Show on Enter your name Screen
        screen.fill(BLACK)
        name = player_name()  
        SCREENDISPLAY(name)
        current_screen = SCREEN_PLAY1

    elif current_screen == SCREEN_PLAY1:
        # Show on Screen Play
        screen.fill(BLACK) 
        turn_message = f"{'Player' if turn == 'player' else 'AI'}'s Turn"
        turn_surface = font_turn.render(turn_message, True, WHITE)
        screen.blit(turn_surface, (350, 50))

        if video_playing:
            if current_video_clip is not None:  # Check if current_video_clip is set
                elapsed_time = pygame.time.get_ticks() - video_start_time
                frame_time = elapsed_time / 1000.0  # Convert milliseconds to seconds

                if frame_time < current_video_clip.duration:
                    frame = get_frame_as_surface(current_video_clip.get_frame(frame_time))
                    frame_rect = frame.get_rect(center=(screen_width // 2, screen_height // 2))
                    screen.blit(frame, (0, 0))  # Display the video frame
            else:
                video_playing = False  # Stop playing video once it's done
                current_video_clip = None  # Reset current_video_clip to avoid further errors

        render_player_image()
        render_ai_image()
        draw_health_bars()

         # Display AI image or debtorblood depending on the timing
        if ai_hit_time and current_time - ai_hit_time <= ai_blood_duration:
            # Show the debtorblood image for 3 seconds
            screen.blit(debtorblood, debtorblood_rect.topleft)
        else:
            # After 3 seconds, show the normal AI image again
            screen.blit(dealer, dealer_rect.topleft)

        # Show medicine result if it was used
        render_medicine_result()
        render_magnifier_result()

        shoot_surface = font.render(shoot_message, True, WHITE)
        screen.blit(shoot_surface, (50, 600))

        ai_shoot_surface = font.render(ai_shoot_message, True, WHITE)
        screen.blit(ai_shoot_surface, (50, 700))

        real_bullets_text = font_12.render(f"Real Bullets: {num_real_bullets}", True, WHITE)
        fake_bullets_text = font_12.render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
        screen.blit(real_bullets_text, (30, 150))
        screen.blit(fake_bullets_text, (750, 150))

        # Display items based on the current round for Player and AI
        if current_round == 1:
            # Draw medicine for round 1
            if not medicine1_used_by_player:
                screen.blit(medicine1, medicine1_rect)
            if not medicine2_used_by_ai:
                screen.blit(medicine2, medicine2_rect)

        elif current_round == round_2:
            real_bullets_text = font_12.render(f"Real Bullets: {num_real_bullets}", True, WHITE)
            fake_bullets_text = font_12.render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
            screen.blit(real_bullets_text, (30, 150))
            screen.blit(fake_bullets_text, (750, 150))

            # Draw magnifier and handsaw for round 2
            if not magnifier1_used_by_player:
                screen.blit(magnifier1, magnifier1_rect)
            if not handsaw1_used_by_player:
                screen.blit(handsaw1, handsaw1_rect)
            if not magnifier2_used_by_ai:
                screen.blit(magnifier2, magnifier2_rect)
            if not handsaw2_used_by_ai:
                screen.blit(handsaw2, handsaw2_rect)

        if ai.game_over:
            if current_round == 1:
                ai.reset()
                current_round += 1
                round_2()
                turn = "player"
                shoot_message = None
                ai_shoot_message = None

            elif current_round == 2:
                ai.reset()
                current_round += 1
                round_3()
                turn = "player"
                shoot_message = None
                ai_shoot_message = None
        else:
            pass

        all_sprites.draw(screen)
        player.draw_hp(screen)
        ai.draw_hp(screen)
        player.player_check_hp()
        ai.ai_check_hp()
        if turn == "ai":
            ai_fire()
            turn = "player"

        if current_round == 2:
            magnifier_button()

        if ai.game_over:
            if current_round == 1:
                ai.reset()
                current_round += 1
                round_2()
                turn = "player"
                shoot_message = None
                ai_shoot_message = None

            elif current_round == 2:
                ai.reset()
                current_round += 1
                round_3()
                turn = "player"
                shoot_message = None
                ai_shoot_message = None
        else:
            pass
        draw_game_state()
  
        if player.game_over:
            player.draw_lose_screen()
            shoot_message = None
            ai_shoot_message = None

            if current_round == 2:
                current_screen = SCREEN_PLAY1
                current_round = 1
                player.reset()
                ai.ai_hp_reset()
                round_1()
            else:
                player.reset()
                ai.ai_hp_reset()
        else:
            pass
            
    pygame.display.flip()   
    pygame.time.Clock().tick(30)

