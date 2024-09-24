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
fps = video_clip.fps  

def get_frame_as_surface(frame):
    frame_bgr = np.flip(frame, axis=0)  
    frame_bgr = np.rot90(frame_bgr, k=-1) 
    return pygame.surfarray.make_surface(frame_bgr)

video_playing = False
current_video_clip = None
video_start_time = 0

def render_video_frame(video_clip, current_time):
    frame_time = current_time / 1000  # Convert time to seconds
    if frame_time < video_clip.duration:
        frame = video_clip.get_frame(frame_time)
        video_surface = get_frame_as_surface(frame)

        # Calculate the position to center the video frame
        video_rect = video_surface.get_rect(center=(screen_width // 2, screen_height // 2))

        # Blit (draw) the video frame at the calculated position
        screen.blit(video_surface, video_rect.topleft)

def get_video_rect(video_clip, x=None, y=None, align="center"):
    """
    Return the rectangle (x, y, width, height) for positioning the video on screen.
    - video_clip: the VideoFileClip object
    - x, y: optional specific coordinates (if None, will align based on `align`)
    - align: alignment options: 'center', 'top-left', 'top-right', etc.
    """
    video_width, video_height = video_clip.size  # Get video dimensions
    
    if align == "center":
        if x is None:
            x = (screen_width - video_width) // 2  
        if y is None:
            y = (screen_height - video_height) // 2  

    # Return a pygame.Rect-like tuple
    return (x, y, video_width, video_height)

def center_video(video_clip, screen_width, screen_height, x=None, y=None):
    global video_start_time  # Access the global variable
    frame_time = (pygame.time.get_ticks() - video_start_time) / 1000.0  # Time in seconds
    if frame_time < video_clip.duration:
        frame = video_clip.get_frame(frame_time)
        frame_surface = get_frame_as_surface(frame)

        # If x and y are provided, use them; otherwise, center the video
        if x is None:
            video_width, video_height = frame_surface.get_size()
            x = (screen_width - video_width) // 2
            y = (screen_height - video_height) // 2

        # Blit the video at the calculated position
        screen.blit(frame_surface, (x, y))
        return True  # Video is still playing
    return False  # Video has finished

handsawvideo1_rect = get_video_rect(handsawvideo1, align="center")
handsawvideo1_x, handsawvideo1_y = handsawvideo1_rect[:2]
center_video(handsawvideo1, screen_width, screen_height, x=handsawvideo1_x, y=handsawvideo1_y)

handsawvideo2_rect = get_video_rect(handsawvideo2, align="center")
handsawvideo2_x, handsawvideo2_y = handsawvideo2_rect[:2]
center_video(handsawvideo2, screen_width, screen_height, x=handsawvideo2_x, y=handsawvideo2_y)

totem_rect = get_video_rect(totem, align="center")
totem_x, totem_y = totem_rect[:2]
center_video(totem, screen_width, screen_height, x=totem_x, y= totem_y)

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

def draw_health_bars():
    for i in range(max_hp):
        if i < player_hp:
            screen.blit(hearts, (50 + i * 60, 50))
        else:
            screen.blit(broken_hearts, (50 + i * 60, 50))

    for i in range(max_hp):
        if i < ai_hp:
            screen.blit(hearts, (900 - i * 60, 50))
        else:
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
        self.hp = 3
        self.totem_used = False
        self.game_over = False  # Define the attribute

    def check_if_game_over(self):
        if self.hp <= 0 and self.totem_used:
            self.game_over = True

    def reset(self):
        self.hp = 3
        self.game_over = False

class Player:
    def __init__(self):
        self.hp = 3  # Initial health value for the player
        self.totem_used = False  # Track if the totem has been used

    def check_if_game_over(self):
        if self.hp <= 0 and self.totem_used:
            self.game_over = True  # Set game_over to True when the player loses

    def restore_hp(self):
        if self.hp <= 0 and not self.totem_used:
            self.hp = 1
            self.totem_used = True

    def reset(self):
        self.hp = 3
        self.game_over = False  # Reset game_over when the player resets
        self.totem_used = False

def check_game_over():
    global ai_hp, player_hp, current_round, ai_totem_used

    # Check if AI's HP is 0
    if ai_hp <= 0:
        # If the AI has not used the totem yet, restore HP using the totem
        if not ai_totem_used:
            ai_hp = 1  # Restore HP
            ai_totem_used = True  # Mark the totem as used
            return  # Don't transition to Round 2 yet

        # If the AI has already used the totem and HP is 0 again, move to Round 2
        if ai_totem_used and current_round == 1:
            current_round += 1  # Increment round
            round_2()  # Call to transition to Round 2
            return

    # Player lose condition
    if player_hp <= 0:
        screen.blit(lose_text_surface, lose_x, lose_y)
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False  
        return
    
def handle_hp_restoration():
    global player_hp, player_heart, player_totem_used, video_playing, current_video_clip, video_start_time

    if player_hp <= 0 and not player_totem_used:
        player_hp = 1  # Restore player HP to 1
        player_heart = hearts  # Update heart image to full
        player_totem_used = True  # Mark as used

        # Start playing the totem video
        current_video_clip = totem
        video_playing = True
        video_start_time = pygame.time.get_ticks()
        totem_sound.play()  # Ensure this is called when the video starts
        print("Player's HP restored using totem and video should play.")

def handle_ai_hp_restoration():
    global ai_hp, ai_heart, ai_totem_used, video_playing, current_video_clip, video_start_time

    if ai_hp <= 0 and not ai_totem_used:
        ai_hp = 1  # Restore AI HP to 1
        ai_heart = hearts  # Update heart image to full
        ai_totem_used = True  # Mark as used

        # Start playing the totem video
        current_video_clip = totem
        video_playing = True
        video_start_time = pygame.time.get_ticks()
        totem_sound.play()
        print("AI's HP restored using totem and video should play.")

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
    global magnifier1_used_by_player, magnifier2_used_by_ai, ai_totem_used

    print("Starting Round 2")

    # Reset HP for both player and AI
    player_hp = 3
    ai_hp = 3  # AI's HP is fully restored in Round 2

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

    # Ensure that the AI can no longer use the totem in future rounds
    ai_totem_used = True

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

    if not video_playing and playing_totem:
        if player_hp <= 0 and not player_totem_used:
            player_hp = 1  # Restore player HP to 1
            player_heart = hearts  # Update heart image to full
            player_totem_used = True  # Mark as used
        if ai_hp <= 0 and not ai_totem_used:
            ai_hp = 1  # Restore AI HP to 1
            ai_heart = hearts  # Update heart image to full
            ai_totem_used = True  # Mark as used
        playing_totem = False  # Reset the totem flag after restoration

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

    if who_used == "player":
        # Player has 99% chance to heal, 1% chance to get damaged
        medicine_outcome = 'heal' if random.randint(1, 100) > 1 else 'damage'
        
        if medicine_outcome == 'heal':
            medicine_message = "Player healed! +1 HP"
            player_hp = min(player_hp + 1, max_hp)
        else:
            medicine_message = "Player damaged! -1 HP"
            player_hp -= 1
            if player_hp <= 0:
                handle_hp_restoration()  # Only handle restoration when HP is 0 or less

    elif who_used == "ai":
        # AI has 1% chance to heal, 99% chance to get damaged
        medicine_outcome = 'damage' if random.randint(1, 100) > 1 else 'heal'
        
        if medicine_outcome == 'heal':
            medicine_message = "AI healed! +1 HP"
            ai_hp = min(ai_hp + 1, max_hp)
        else:
            medicine_message = "AI damaged! -1 HP"
            ai_hp -= 1
            if ai_hp <= 0:
                handle_ai_hp_restoration()  # Only handle restoration when HP is 0 or less

    # Only play the totem video if health is less than or equal to 0
    if (who_used == "player" and player_hp <= 0) or (who_used == "ai" and ai_hp <= 0):
        current_video_clip = totem  # Set the totem video
        video_playing = True
        video_start_time = pygame.time.get_ticks()

    # Set the time when the medicine result should be displayed
    medicine_display_time = pygame.time.get_ticks()

def render_medicine_result():
    current_time = pygame.time.get_ticks()

    # Show the result message for 3 seconds
    if current_time - medicine_display_time <= 3000:  # Display for 3 seconds
        box_width, box_height = 500, 50
        box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2 - 150, box_width, box_height)
        pygame.draw.rect(screen, LIGHTGREY, box_rect)

        # Display the message text in white for better visibility
        medicine_surface = font_10.render(medicine_message, True, RED)
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
    global magnifier1_used_by_player, current_round

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
            return  # Player continues the turn after using magnifier

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
    global magnifier2_used_by_ai, medicine_message, medicine_display_time, current_round

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
        # AI uses magnifier if its HP is below 2 and magnifier hasn't been used yet
        if ai_hp < 2 and not magnifier2_used_by_ai:
            handle_magnifier("ai")  # AI checks bullet type using magnifier
            magnifier2_used_by_ai = True  # Mark magnifier as used
            return

        # AI uses handsaw only if the bullet is real and handsaw hasn't been used yet
        if magnifier2_used_by_ai and current_bullet() == 1 and not handsaw2_used_by_ai:
            handsaw2_used_by_ai = True  # Mark handsaw as used
            handsaw_damage_pending_ai = True  # Indicate damage will happen after target selection
            handsaw_sound.play()  # Play the handsaw sound
            video_playing = True  # Set video playing state to true
            current_video_clip = handsawvideo2  # Set the correct video for handsaw
            video_start_time = pygame.time.get_ticks()  # Track the start time of the video
            return  # Exit the function to wait for target selection after the video

    # Check the elapsed time for AI decision-making
    elapsed_time = pygame.time.get_ticks() - ai_turn_start_time
    if elapsed_time >= 3000:  # 3 seconds limit for AI shooting
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

def roundmessage(message):
    font_welcome = pygame.font.Font("Creepster.ttf", 60)
    welcome_surface = font_welcome.render(message, True, WHITE)
    welcome_rect = welcome_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(welcome_surface, welcome_rect)
    pygame.display.flip()

    # Pause for 3 seconds
    pygame.time.delay(3000)

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

    # Reset HP for both player and AI
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
    
    # Show the "Welcome to Round 2" message
    roundmessage("Welcome to Round 2")
    pygame.time.delay(3000)

def render_items_in_round_2():
    if current_round == 2:
        # Draw magnifier and handsaw for both player and AI
        if not magnifier1_used_by_player:
            screen.blit(magnifier1, magnifier1_rect)
        if not handsaw1_used_by_player:
            screen.blit(handsaw1, handsaw1_rect)
        if not magnifier2_used_by_ai:
            screen.blit(magnifier2, magnifier2_rect)
        if not handsaw2_used_by_ai:
            screen.blit(handsaw2, handsaw2_rect)

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


##########################################################################################################################################################################
# Initialize important variables
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
            # Main screen button handling
            if current_screen == SCREEN_MAIN:
                if button_text2_rect.collidepoint(event.pos):
                    sound_play.play()
                    current_screen = SCREEN_PLAY1
                    pygame.display.set_caption('Storyline')
                elif button_text3_rect.collidepoint(event.pos):
                    sound_how_to_play.play()
                    current_screen = SCREEN_HOW_TO_PLAY
                    pygame.display.set_caption('How to Play')

            # How to Play screen
            elif current_screen == SCREEN_HOW_TO_PLAY:
                if text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

            # Story screens
            elif current_screen == SCREEN_STORY1:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_next.play()
                    current_screen = SCREEN_STORY2
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_PLAY

            elif current_screen == SCREEN_STORY2:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_next.play()
                    current_screen = SCREEN_STORY3
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY1

            elif current_screen == SCREEN_STORY3:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_next.play()
                    current_screen = SCREEN_STORY4
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY2

            elif current_screen == SCREEN_STORY4:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    show_input_box = True
                    current_screen = SCREENNAME
                    pygame.display.set_caption('Enter your Name')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY3

            elif current_screen == SCREENNAME:
                name = player_name()
                SCREENDISPLAY(name)

            elif current_screen == SCREEN_PLAY1:
                if text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

                if turn == "player":
                    player_turn()

                    if player_hp <= 0:
                        handle_hp_restoration()

                if current_round == 1:
                    # Draw medicine for round 1
                    if not medicine1_used_by_player:
                        screen.blit(medicine1, medicine1_rect)
                    if not medicine2_used_by_ai:
                        screen.blit(medicine2, medicine2_rect)

    # AI turn handling with delay
    if turn == "ai" and not ai_waiting:
        ai_delay_start = pygame.time.get_ticks()  # Start delay timer
        ai_waiting = True  # Set AI as waiting

    if turn == "ai" and ai_waiting:
        current_time = pygame.time.get_ticks()
        # Check if 3 seconds have passed since AI's turn started
        if current_time - ai_delay_start >= ai_delay_duration:
            ai_turn()  # AI chooses who to shoot after delay
            ai_waiting = False  # Reset for the next turn

            if ai_hp <= 0:
                handle_ai_hp_restoration()

            # Round logic and handsaw damage application
            if current_round == 1:
                render_health_restoration()
            elif current_round == 2:
                render_health_restoration()
            elif current_round == 3:
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

    if video_playing and current_video_clip:
        if not center_video(current_video_clip, screen_width, screen_height):
            video_playing = False  
            current_video_clip = None  # Reset current video clip
            render_health_restoration()  # Restore health after video finishes
            handle_ai_hp_restoration
            handle_hp_restoration

        check_game_over()

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

        if video_playing and current_video_clip:
            totem_rect = get_video_rect(totem, align="center")
            center_video(current_video_clip, screen_width, screen_height, x=totem_rect[0], y=totem_rect[1])
            if not video_playing: 
                render_health_restoration()

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
            if not magnifier1_used_by_player:
                screen.blit(magnifier1, magnifier1_rect)
            if not handsaw1_used_by_player:
                screen.blit(handsaw1, handsaw1_rect)
            if not magnifier2_used_by_ai:
                screen.blit(magnifier2, magnifier2_rect)
            if not handsaw2_used_by_ai:
                screen.blit(handsaw2, handsaw2_rect)

            real_bullets_text = font_12.render(f"Real Bullets: {num_real_bullets}", True, WHITE)
            fake_bullets_text = font_12.render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
            screen.blit(real_bullets_text, (30, 150))
            screen.blit(fake_bullets_text, (750, 150))


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