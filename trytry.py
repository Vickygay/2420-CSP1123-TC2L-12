import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np
import random
from moviepy.editor import *
import math
import time

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

# Resize videos 
video_size = (150, 150)
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
    frame_time = current_time / 1000 
    if frame_time < video_clip.duration:
        frame = video_clip.get_frame(frame_time)
        video_surface = get_frame_as_surface(frame)

        video_rect = video_surface.get_rect(center=(screen_width // 2, screen_height // 2))

        screen.blit(video_surface, video_rect.topleft)

def get_video_rect(video_clip, x=None, y=None, align="center"):
    video_width, video_height = video_clip.size  # Get video dimensions
    
    if align == "center":
        if x is None:
            x = (screen_width - video_width) // 2  
        if y is None:
            y = (screen_height - video_height) // 2 + 50

    return (x, y, video_width, video_height)

def center_video(video_clip, screen_width, screen_height, x=None, y=None):
    global video_start_time  
    frame_time = (pygame.time.get_ticks() - video_start_time) / 1000.0 
    if frame_time < video_clip.duration:
        frame = video_clip.get_frame(frame_time)
        frame_surface = get_frame_as_surface(frame)

        if x is None:
            video_width, video_height = frame_surface.get_size()
            x = (screen_width - video_width) // 2
            y = (screen_height - video_height) // 2 + 50

        screen.blit(frame_surface, (x, y))
        return True 
    return False 

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
pygame.mixer.music.set_volume(0.0)  # (0.0 - 1.0)
pygame.mixer.music.play(-1)  # Loop music infinity

# Sound effects when click the text
soundclick = pygame.mixer.Sound('clicksound.mp3')
sound_clickbox = pygame.mixer.Sound("clickbox.mp3")
gun_sound = pygame.mixer.Sound("gunsound.mp3")
emptygun_sound = pygame.mixer.Sound("emptygun.mp3")
delete_sound = pygame.mixer.Sound("delete.mp3")
totem_sound = pygame.mixer.Sound("totem.mp3")
handsaw_sound = pygame.mixer.Sound("handsaw.mp3")
dealerlaugh = pygame.mixer.Sound("muhaha.mp3")

# Colours code in RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (173, 216, 230)
CHARCOAL = (54, 69, 79)
LIGHTRED = (255,0,0)
DARKRED = (139, 0, 0)
TRANSPARENT = (0, 0, 0, 0)
DARKGREY = (169, 169, 169)
LIGHTGREY = (211, 211, 211)

font = pygame.font.Font("gennaro.ttf", 25)

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

text_5_surface = font_4.render("Next >>", True, WHITE)
text_5_button_x, text_5_button_y = (screen_width - text_5_surface.get_width()) // 2 + 400, screen_height - text_5_surface.get_height() // 2 - 50
text_5_button_rect = pygame.Rect(text_5_button_x, text_5_button_y, text_5_surface.get_width(), text_5_surface.get_height())

font_6 = pygame.font.Font('Matemasie.ttf', 40)
lose_text_surface = font_6.render("Foolish gambler. Try again would ya?", True, RED)
lose_x, lose_y = 125, 250

font_7 = pygame.font.Font('Creepster.ttf', 3)

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

font_11 = pygame.font.Font('Nerko.ttf', 62)
text_11_surface = font_11.render("Click shift first then enter your name!", True, WHITE)
text_11_button_x, text_11_button_y = (screen_width - text_11_surface.get_width()) // 2, (screen_width // 2) - text_11_surface.get_height() - 200
text_11_button_rect = pygame.Rect(text_11_button_x, text_11_button_y, text_11_surface.get_width(), text_11_surface.get_height())

font_12 = pygame.font.Font('Nerko.ttf', 36)
font_13 = pygame.font.Font('Nerko.ttf', 28)

font_14 = pygame.font.Font('Matemasie.ttf', 45)
text_14_surface = font_14.render("<< Main", True, WHITE)
text_14_button_x, text_14_button_y = (screen_width - text_14_surface.get_width()) // 2 - 400, screen_height - text_14_surface.get_height() // 2 - 50
text_14_button_rect = pygame.Rect(text_14_button_x, text_14_button_y, text_14_surface.get_width(), text_14_surface.get_height())

text_15_surface = font_2.render("Do you want to play maze?", True, WHITE)
text_15_button_x, text_15_button_y = (screen_width - text_15_surface.get_width()) // 2, (screen_width // 2 + 50) - text_15_surface.get_height() // 2 - 250
text_15_button_rect = pygame.Rect(text_15_button_x, text_15_button_y, text_15_surface.get_width(), text_15_surface.get_height())

text_16_surface = font_3.render("YES", True, WHITE)
text_16_button_x, text_16_button_y = (screen_width - text_16_surface.get_width()) // 2 -100 , (screen_width // 2 - 50) - text_16_surface.get_height() // 2 - 50
text_16_button_rect = pygame.Rect(text_16_button_x, text_16_button_y, text_16_surface.get_width(), text_16_surface.get_height())

text_17_surface = font_3.render("NO", True, WHITE)
text_17_button_x, text_17_button_y = (screen_width - text_17_surface.get_width()) // 2 + 100 , (screen_width // 2 - 50) - text_17_surface.get_height() // 2 - 50
text_17_button_rect = pygame.Rect(text_17_button_x, text_17_button_y, text_17_surface.get_width(), text_17_surface.get_height())

lines = [
    "Debtor : Welp  ,  guess  thats  all  for  your  end" ,
    "of  your  life  .  Poor  girl  with  her  poor  father",
    "-->Bad End"
]


lines_1 = [
    "--After  defeat  the  debtor--",
    "Daughter  :  *SCREMING*  ",
    "WHO  ARE  YOU?  I  WANT  MY  FATHER  BACK!!!",
    "--A  piece  of  shattered  glass  reflect  and  so  who"
    "had  you  become?--"
    "-->End 1"
]

lines_2 = [
    "Daughter  :  DAD!!",
    "'Alright  sweetie,  lets  go  back  home'",
    "--At  least  your  determination  find  you  back--",
    "--The End--"
]


input_font_name = pygame.font.Font("Gloria.ttf", 50)

font_turn = pygame.font.Font("Creepster.ttf", 50)
turn_message = "Player's Turn"
fontshoot = pygame.font.Font("Gloria.ttf", 28)
fontbulletbig = pygame.font.Font('Nerko.ttf', 45)
fontbulletsmall = pygame.font.Font('Nerko.ttf', 40)

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

fatherimage = pygame.image.load('father.png')
father = pygame.transform.scale(fatherimage,(500,500))

monsterimage = pygame.image.load("monster.jpeg")
monster = pygame.transform.scale(monsterimage,(700,500))

heartsimage = pygame.image.load('hearts.png')
hearts = pygame.transform.scale(heartsimage, (50,50))

witchimage = pygame.image.load('witch.png')
witch = pygame.transform.scale(witchimage, (500,500))

broken_hearts = pygame.image.load('broken_hearts.png')
broken_hearts = pygame.transform.scale(broken_hearts, (50,50))

dealer = pygame.image.load('dealer.png')
dealer = pygame.transform.scale(dealer, (200, 200))
dealer_rect = dealer.get_rect(topleft=(750, 400))

debtor = pygame.image.load('dealer.png')
debtor = pygame.transform.scale(dealer, (300, 300))
debtor_rect = dealer.get_rect()
debtor_rect.x = 350
debtor_rect.y = 50

crying = pygame.image.load('crying.png')
crying = pygame.transform.scale(crying, (300, 300))
crying_rect = crying.get_rect()
crying_rect.x = 350
crying_rect.y = 50

hug = pygame.image.load('crying.png')
hug = pygame.transform.scale(hug, (300, 300))
hug_rect = hug.get_rect()
hug_rect.x = 350
hug_rect.y = 50

user = pygame.image.load('player.png')
user = pygame.transform.scale(user, (200, 200))
user_rect = user.get_rect(topleft=(50, 400))

#Display positions of images
player_x = 50
player_y = 200

debtorblood = pygame.image.load('debtorblood.png')
debtorblood = pygame.transform.scale(debtorblood, (200, 250))
debtorblood_rect = debtorblood.get_rect(topleft=(740, 385))

playerblood = pygame.image.load('playerblood.png')
playerblood = pygame.transform.scale(playerblood, (200, 300))
playerblood_rect = playerblood.get_rect(topleft=(50, 330))

handsaw1 = pygame.image.load('handsaw1.png')
handsaw1 = pygame.transform.scale(handsaw1, (70, 70))
handsaw1_rect = handsaw1.get_rect(topleft=(screen_width // 2 - 250, screen_height // 2 + 90))
handsaw2 = pygame.image.load('handsaw2.png')
handsaw2 = pygame.transform.scale(handsaw2, (70, 70))
handsaw2_rect = handsaw2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2 + 90))

medicine1 = pygame.image.load('medicine1.png')
medicine1 = pygame.transform.scale(medicine1, (70, 70))
medicine1_rect = medicine1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2 + 50))
medicine2 = pygame.image.load('medicine2.png')
medicine2 = pygame.transform.scale(medicine2, (70, 70))
medicine2_rect = medicine2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2 + 50))

magnifier1 = pygame.image.load('magnifier1.png')
magnifier1 = pygame.transform.scale(magnifier1, (70, 70))
magnifier1_rect = magnifier1.get_rect(topleft=(screen_width // 2 - 250, screen_height // 2 - 20))
magnifier2 = pygame.image.load('magnifier2.png')
magnifier2 = pygame.transform.scale(magnifier2, (70, 70))
magnifier2_rect = magnifier2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2 - 20))

# Define screen states
SCREEN_MAIN = 0
SCREEN_PLAY = 1
SCREEN_HOW_TO_PLAY = 2
SCREEN_STORY1 = 3
SCREEN_STORY2 = 4
SCREEN_STORY3 = 5
SCREEN_STORY4 = 6
SCREEN_STORY5 = 7
SCREEN_PLAYMAZE = 8
SCREEN_MAZE = 9
SCREEN_PLAY1 = 10
SCREENNAME = 11
SCREENDISPLAY = 12
SCREEN_ENDING1 = 13
SCREEN_ENDING2 = 14
SCREEN_ENDING3 = 15
SCREEN_ENDING4 = 16
SCREEN_ENDING5 = 17
SCREEN_ENDING6 = 18
SCREEN_ENDING7 = 19
SCREEN_ENDING8 = 20

current_screen = SCREEN_MAIN

font = pygame.font.Font("gennaro.ttf", 25)


def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

fonttext1 = pygame.font.Font('gennaro.ttf', 40)
fonttext2 = pygame.font.Font('scary3.ttf', 40)

def draw_custom_shape(surface, color, x, y, width, height):
    points = [
        (x, y - height // 3),               # Top center
        (x + width // 2, y - height // 3),  # Top right
        (x + width // 1.5, y),              # Right
        (x + width // 2, y + height // 3),  # Bottom right
        (x, y + height // 3),               # Bottom center
        (x - width // 2, y + height // 3),  # Bottom left
        (x - width // 1.5, y),              # Left
        (x - width // 2, y - height // 3)   # Top left
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

# Clock to control FPS
clock = pygame.time.Clock()

move_sound = pygame.mixer.Sound("footsteps.wav")
collision_sound = pygame.mixer.Sound("collision.wav")
pick_sound = pygame.mixer.Sound("pick.wav")

player_right_img = pygame.image.load("player_right.png")
player_left_img = pygame.image.load("player_left.png")
boost_img = pygame.image.load("boost.png")
wall_img = pygame.image.load("wall.png")
monster_left_img = pygame.image.load("monster_left.png")
monster_right_img = pygame.image.load("monster_right.png")
heart_img = pygame.image.load("heart.png")
exit_img = pygame.image.load("exit.png")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font_Maze = pygame.font.Font(None, 36)

class Man(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_right_img
        self.rect = self.image.get_rect()
        self.power = 0
        self.lives = 3
        self.boost_count = 0  
        self.last_collision_time = 0

    def move(self, dx=0, dy=0, walls=None):
        old_x, old_y = self.rect.x, self.rect.y
        self.rect.x += dx
        self.rect.y += dy

        # Collision with walls: rollback if collided
        if walls and pygame.sprite.spritecollideany(self, walls):
            self.rect.x, self.rect.y = old_x, old_y  # Revert movement if collision occurs
        else:
            move_sound.play()  # Play sound only if movement is valid

    def is_collision(self, other):
        return self.rect.colliderect(other.rect)
    
    def collect_boost(self):
        self.boost_count += 1
        pick_sound.play()

    def handle_collision_with_enemy(self):
        """Handle the collision with the enemy and lose a life if necessary."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_collision_time > 1000:  # 1 second delay
            self.lives -= 1
            collision_sound.play()
            self.last_collision_time = current_time

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = wall_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = boost_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destroy(self):
        self.kill()  # Remove boost from game

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = monster_left_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = random.choice(["up", "down", "left", "right"])
        self.last_move_time = pygame.time.get_ticks()

    def move(self, walls, man):
        current_time = pygame.time.get_ticks()

        # Move every 500ms to slow down enemy movement
        if current_time - self.last_move_time >= 500:
            dx, dy = 0, 0
            if self.direction == "up":
                dy = -24
            elif self.direction == "down":
                dy = 24
            elif self.direction == "left":
                dx = -24
                self.image = monster_left_img
            elif self.direction == "right":
                dx = 24
                self.image = monster_right_img

            old_x, old_y = self.rect.x, self.rect.y
            self.rect.x += dx
            self.rect.y += dy

            # Check for wall collision
            if pygame.sprite.spritecollideany(self, walls):
                self.rect.x, self.rect.y = old_x, old_y  # Revert movement if collision occurs
                self.direction = random.choice(["up", "down", "left", "right"])  # Change direction

            # Update move time
            self.last_move_time = current_time
            
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = exit_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Setup maze layout
walls = pygame.sprite.Group()
boosts = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

def setup_maze(level):
    global exit_point
    for y, row in enumerate(level):
        for x, char in enumerate(row):
            screen_x = x * 24
            screen_y = y * 24
            if char == "X":
                wall = Wall(screen_x, screen_y)
                walls.add(wall)
                all_sprites.add(wall)
            elif char == "B":
                boost = Boost(screen_x, screen_y)
                boosts.add(boost)
                all_sprites.add(boost)
            elif char == "E":
                enemy = Enemy(screen_x, screen_y)
                enemies.add(enemy)
                all_sprites.add(enemy)
            elif char == "M":
                man.rect.x = screen_x
                man.rect.y = screen_y
            elif char == "Z":
                exit_point = Exit(screen_x, screen_y)
                all_sprites.add(exit_point)

# Define the game level
level_1 = [
"                                 ",
"                                 ",
"                                 ",
"        XXXXXXXXXXXXXXXXXXXXXXXXX",
"        XM XXXXXXXE          XXXX",
"        X  XXXXXXX   XXXXX   XXXX",
"        X       XX   XXXXX   XXXX",
"        X       XX   XXX       XX",
"        XXXXXX  XX   XXX      EXX",
"        XXXXXX  XX   XXXXX   XXXX",
"        XXXXXX         XXXB  XXXX",
"        X  XXX     XXXXXXXXXXXXXX",
"        X EXXX         XXXXXXXXXX",
"        X               XXXXB   X",
"        XXXXXXXXX       XXXX    X",
"        XXXZXXXXXXXX    XXXX    X",
"        XX    XXXXXX            X",
"        XXX                     X",
"        XXX             XXXXXXXXX",
"        XXXXXXXXX       XXXXXXXXX",
"        XXXXXXXXXX             XX",   
"        XXB   XXXX             XX",
"        XX    XXXXXXXXXX       XX",
"        XX    XXXXXXXXXX     XXXX",
"        XX     XXXXXXXXX     XXXX",
"        XX         XXXXX        X",
"        XXXE                    X",
"        XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Create the player and add to the sprite group
man = Man()
all_sprites.add(man)

# Initialize game state
setup_maze(level_1)

exit_message = ""
show_exit_message = False
message_start_time = 0


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
medicine_delay_duration = 3000

ai_delay_start = 0
ai_delay_duration = 3000 
ai_waiting = False
global ai_hit_time, ai_blood_duration
ai_hit_time = None 
ai_blood_duration = 3000  
player_hit_time = None
player_blood_duration = 3000 
player_heart = hearts
ai_heart = hearts
ai_turn_ready = False
playing_totem = False
restore_after_video = False

# Initialize global variables for items
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
magnifier_bullet_type = None 
ai_waiting_after_medicine = False  
ai_waiting_before_shoot = False  
ai_delay_start = 0  
ai_shoot_complete = False 
magnifier_delay_start = 0
magnifier_delay_duration = 6000  
magnifier_delay_active = False

true_ending = False
bad_ending = False

def reset_game_state_after_maze():
    global player_hp, ai_hp, player_totem_used, ai_totem_used, handsaw1_used_by_player, handsaw2_used_by_ai
    global num_real_bullets, num_fake_bullets, bullets, turn, current_round, player_hit_time, ai_hit_time
    global handsaw_damage_pending_player, handsaw_damage_pending_ai, magnifier1_used_by_player, magnifier2_used_by_ai
    global video_playing, current_video_clip, video_start_time, magnifier_bullet_type, ai_waiting, ai_delay_start
    global player_heart, ai_heart, player_restored, ai_restored, player_shoot_message, ai_shoot_message
    global playing_totem, player_hp_restored, ai_hp_restored, num_real_bullets, num_fake_bullets, bullets

    # Reset player and AI health
    player_hp = 4
    ai_hp = 3

    player_heart = hearts
    ai_heart = hearts

    # Reset totem usage for player and AI
    player_totem_used = False
    ai_totem_used = False
    player_restored = False
    ai_restored = False

    # Reset handsaw usage for player and AI
    handsaw1_used_by_player = False
    handsaw2_used_by_ai = False
    handsaw_damage_pending_player = False
    handsaw_damage_pending_ai = False

    # Reset magnifier usage
    magnifier1_used_by_player = False
    magnifier2_used_by_ai = False
    magnifier_bullet_type = None

    # Reset turn to player's turn
    turn = "player"

    # Reset bullets and bullet-related variables
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

    # Reset video playback
    video_playing = False
    current_video_clip = None
    video_start_time = 0

    # Reset messages
    player_shoot_message = ""
    ai_shoot_message = ""

    # Reset AI waiting and delay for AI turns
    ai_waiting = False
    ai_delay_start = 0

    # Reset health displays
    player_hit_time = None
    ai_hit_time = None
    player_heart = hearts
    ai_heart = hearts

    # Reset playing_totem and restore flags
    playing_totem = False
    player_hp_restored = False
    ai_hp_restored = False

    # Reset round to 1
    current_round = 1

def true_ending():
    global max_hp, player_hp
    if man.boost_count == 3:
        player_hp = 4
        true_ending = True
        if true_ending == True:
            print ("Congraz")

    else:
        player_hp = min (player_hp, max_hp)

def check_if_all_bullets_used():
    global bullets, player_hp, ai_hp, current_round

    if not bullets:
        if player_hp > 0 and ai_hp > 0:
            if current_round == 1:
                round_2()  
            elif current_round == 2:
                round_3()  
            elif current_round == 3:
                show_game_over("Final round completed. It's a draw!")
                pygame.quit() 

def draw_health_bars():
    global player_hp, max_hp
    hearts_y = 280
    # Player's hearts
    for i in range(max_hp):
        if i < player_hp:
            screen.blit(hearts, (50 + i * 60, hearts_y))
        else:
            screen.blit(broken_hearts, (50 + i * 60, hearts_y))  
    # Dealer's hearts
    for i in range(max_hp):
        if i < ai_hp:
            screen.blit(hearts, (900 - i * 60, hearts_y))  
        else:
            screen.blit(broken_hearts, (900 - i * 60, hearts_y))  

def health_boost():
    global max_hp, player_hp
    if man.boost_count == 0:
        max_hp = 3
    if man.boost_count == 2 or man.boost_count == 3:
        player_hp = 4
    else:
        pass

# Initialize global variables for health restoration, totem usage and can be eliminated or not
player_restored = False
ai_restored = False
player_totem_used = False  
ai_totem_used = False  
player_can_be_eliminated = False  
ai_can_be_eliminated = False  

class AI:
    def __init__(self):
        self.hp = 3
        self.totem_used = False
        self.game_over = False  

    def check_if_game_over(self):
        if self.hp <= 0 and self.totem_used:
            self.game_over = True

class Player:
    def __init__(self):
        self.hp = 3  
        self.totem_used = False  
        self.game_over = False 

    def check_if_game_over(self):
        if self.hp <= 0 and self.totem_used:
            self.game_over = True 

    def restore_hp(self):
        if self.hp <= 0 and not self.totem_used:
            self.hp = 1
            self.totem_used = True

    def reset(self):
        self.hp = 3
        self.game_over = False  
        self.totem_used = False

    #Draw out defeated screen when player is defeated
    def draw_lose_screen(self):
        if self.game_over:
            screen.fill(BLACK)
            screen.blit(lose_text_surface, (lose_x, lose_y))
            pygame.display.update()
            pygame.time.delay(2000)
            self.reset

def check_game_over():
    global ai_hp, player_hp, player_totem_used, ai_totem_used, current_round, running, num_real_bullets, num_fake_bullets

    if ai_hp <= 0:
        if not ai_totem_used and current_round < 3:
            ai_hp = 1
            ai_totem_used = True
            return

        if current_round == 3:
            if man.boost_count == 2:
                screen.fill(BLACK)
                screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))

                text_19_x = 0
                base_y = 450
                line_spacing = 60
                fixed_y_positions = [base_y, base_y + line_spacing, base_y + 2 * line_spacing, base_y + 3 * line_spacing]

                for i, line in enumerate(lines_1):
                    text_19_surface = font_7.render(line, True, WHITE)
                    screen.blit(text_19_surface, (text_19_x, fixed_y_positions[i]))

                screen.blit(crying, crying_rect.topleft)

            elif man.boost_count == 3 or man.boost_count == 0:
                screen.fill(BLACK)
                screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))

                text_20_x = 0
                base_y = 450
                line_spacing = 60
                fixed_y_positions = [base_y, base_y + line_spacing, base_y + 2 * line_spacing, base_y + 3 * line_spacing]

                for i, line in enumerate(lines_2):
                    text_20_surface = font_7.render(line, True, WHITE)
                    screen.blit(text_20_surface, (text_20_x, fixed_y_positions[i]))

                screen.blit(hug, hug_rect.topleft)

            running = False
            return

        if ai_totem_used and current_round == 1:
            current_round = 2
            round_2()
            return
        elif ai_totem_used and current_round == 2:
            current_round = 3
            round_3()
            return

    if player_hp <= 0:
        if not player_totem_used and current_round < 3:
            player_hp = 1
            player_totem_used = True
            return

        if current_round == 3:
            show_game_over("Foolish gambler. Try again would ya?")
            running = False
            return

        show_game_over("Foolish gambler. Try again would ya?")
        return

    if num_real_bullets == 0:
        if current_round == 1:
            current_round = 2
            round_2()
            return
        elif current_round == 2:
            current_round = 3
            round_3()
            return
        elif current_round == 3:
            show_game_over(f"No bullets left. {name} win.")
            running = False
            return

def handle_shooting(shooter, target):
    global bullets, num_real_bullets, num_fake_bullets

    if bullets:
        current_bullet = bullets.pop(0) 
        if current_bullet == 1: 
            if shooter == "player":
                shoot_message = f"{name} shot {target} with a real bullet!"
            elif shooter == "ai":
                shoot_message = "AI shot {target} with a real bullet!"
            return "real"
        elif current_bullet == 0:  
            if shooter == "player":
                shoot_message = f"{name} shot {target} with a fake bullet!"
            elif shooter == "ai":
                shoot_message = "AI shot {target} with a fake bullet!"
            return "fake"
    else:
        return None

def handle_hp_restoration():
    global player_hp, player_heart, player_totem_used, video_playing, current_video_clip, video_start_time

    if current_round < 3:  
        if player_hp <= 0 and not player_totem_used:
            player_hp = 1  
            player_heart = hearts
            player_totem_used = True

            current_video_clip = totem
            video_playing = True
            video_start_time = pygame.time.get_ticks()
            totem_sound.play()

def handle_ai_hp_restoration():
    global ai_hp, ai_heart, ai_totem_used, video_playing, current_video_clip, video_start_time

    if current_round < 3:  
        if ai_hp <= 0 and not ai_totem_used:
            ai_hp = 1  
            ai_heart = hearts
            ai_totem_used = True  

            current_video_clip = totem
            video_playing = True
            video_start_time = pygame.time.get_ticks()
            totem_sound.play()

def handle_magnifier(who_used):
    global magnifier_bullet_type, magnifier_message, magnifier_display_time
    
    if num_real_bullets == 0 and num_fake_bullets == 0:
        magnifier_bullet_type = None  
        return

    bullet_type = bullets[0] 

    if who_used == "player":
        if bullet_type == 1:  
            magnifier_bullet_type = "real"
            magnifier_message = "Real Bullet! Go ahead FIREEEE"
        else:
            magnifier_bullet_type = "fake"
            magnifier_message = "Fake Bullet. Not the time yet."
    elif who_used == "ai":
        if bullet_type == 1:
            magnifier_bullet_type = "real"
            magnifier_message = "Dealer saw: Real Bullet! GG"
        else:  
            magnifier_bullet_type = "fake"
            magnifier_message = "Dealer saw: Fake Bullet! God bless"
    
    magnifier_display_time = pygame.time.get_ticks() 

def render_magnifier_result():
    current_time = pygame.time.get_ticks()

    if current_time - magnifier_display_time <= 3000:  
        box_width, box_height = 700, 40
        box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2 - 50, box_width, box_height)
        pygame.draw.rect(screen, LIGHTGREY, box_rect)

        magnifier_surface = fontshoot.render(magnifier_message, True, RED)
        text_rect = magnifier_surface.get_rect(center=box_rect.center)
        screen.blit(magnifier_surface, text_rect.topleft)

def show_game_over(message):
    font_game_over = pygame.font.Font("Creepster.ttf", 100)
    game_over_surface = font_game_over.render(message, True, RED)
    game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    running = False  
    
def render_health_restoration():
    global playing_totem, player_restored, ai_restored, player_heart, ai_heart

    if not video_playing and playing_totem:
        if player_hp <= 0 and not player_totem_used:
            player_hp = 1  
            player_heart = hearts  
            player_totem_used = True 
        if ai_hp <= 0 and not ai_totem_used:
            ai_hp = 1  
            ai_heart = hearts  
            ai_totem_used = True
        playing_totem = False  

def render_player_image():
    global player_hit_time, player_blood_duration, playerblood, playerblood_rect, user, user_rect

    current_time = pygame.time.get_ticks()

    if player_hit_time and current_time - player_hit_time <= player_blood_duration:
        screen.blit(playerblood, playerblood_rect.topleft)  
    else:
        screen.blit(user, user_rect.topleft)  

def render_ai_image():
    global ai_hit_time, ai_blood_duration, dealer, debtorblood, dealer_rect

    current_time = pygame.time.get_ticks()

    if ai_hit_time and current_time - ai_hit_time <= ai_blood_duration:
        screen.blit(debtorblood, debtorblood_rect.topleft) 
    else:
        screen.blit(dealer, dealer_rect.topleft)  

def restore_health():
    global player_hp, ai_hp, player_restored, ai_restored, player_heart, ai_heart, playing_totem
    if playing_totem:  
        if player_hp <= 0 and not player_restored:
            player_hp = 1  
            player_heart = hearts 
            player_restored = True 
        if ai_hp <= 0 and not ai_restored:
            ai_hp = 1  
            ai_heart = hearts  
            ai_restored = True 
        playing_totem = False  

def handle_medicine(who_used):
    global current_video_clip, video_playing, video_start_time
    global player_hp, ai_hp, medicine_message, medicine_display_time

    if who_used == "player":
        # 99% chance for the player to heal, 1% chance to take damage
        medicine_outcome = 'heal' if random.randint(1, 100) > 1 else 'damage'
        
        if medicine_outcome == 'heal':
            medicine_message = f"{name} used medicine and healed! +1 HP"
            player_hp = min(player_hp + 1, max_hp)
        else:
            medicine_message = f"{name} used medicine and damaged! -1 HP"
            player_hp -= 1
            if player_hp <= 0:
                handle_hp_restoration()

    elif who_used == "ai":
        # 99% chance for the AI to take damage, 1% chance to heal
        medicine_outcome = 'damage' if random.randint(1, 100) > 1 else 'heal'
        
        if medicine_outcome == 'heal':
            medicine_message = "Dealer used medicine and healed! +1 HP"
            ai_hp = min(ai_hp + 1, max_hp)
        else:
            medicine_message = "Dealer used medicine and damaged! -1 HP"
            ai_hp -= 1
            if ai_hp <= 0:
                handle_ai_hp_restoration()

    if (who_used == "player" and player_hp <= 0) or (who_used == "ai" and ai_hp <= 0):
        current_video_clip = totem
        video_playing = True
        video_start_time = pygame.time.get_ticks()
    
    medicine_display_time = pygame.time.get_ticks()  

def render_medicine_result():
    global medicine_display_time
    current_time = pygame.time.get_ticks()

    if medicine_display_time and current_time - medicine_display_time <= 3000: 
        box_width, box_height = 700, 40
        box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2 - 50, box_width, box_height)
        pygame.draw.rect(screen, LIGHTGREY, box_rect)

        medicine_surface = fontshoot.render(medicine_message, True, RED)
        text_rect = medicine_surface.get_rect(center=box_rect.center)
        screen.blit(medicine_surface, text_rect.topleft)
    else:
        medicine_display_time = 0 

def handle_handsaw_usage(shooter, target):
    global shoot_message, player_hp, ai_hp, ai_hit_time, player_hit_time
    global num_real_bullets, num_fake_bullets
    global handsaw_damage_pending_player, handsaw_damage_pending_ai
    global magnifier2_used_by_ai, magnifier_bullet_type

    if shooter == "ai" and magnifier2_used_by_ai and magnifier_bullet_type == 'fake':
        return

    bullet_type = None
    if magnifier_bullet_type: 
        bullet_type = magnifier_bullet_type
    elif num_real_bullets > 0 and num_fake_bullets > 0:
        bullet_type = random.choice(['real', 'fake'])
    elif num_real_bullets > 0:
        bullet_type = 'real'
    elif num_fake_bullets > 0:
        bullet_type = 'fake'

    if bullet_type == 'real' and num_real_bullets > 0:
        num_real_bullets -= 1
        gun_sound.play()

        if shooter == "player":
            if target == "ai":
                shoot_message = f"{name} used handsaw and shot dealer with real bullets! Nice Job"
                ai_hp -= 2  
                ai_hit_time = pygame.time.get_ticks()
            else:
                shoot_message = f"{name} used handsaw and shot themselves with real bullets! Interesting"
                player_hp -= 2 
                player_hit_time = pygame.time.get_ticks()
                handsaw_damage_pending_player = False
                return

        elif shooter == "ai":
            if target == "player":
                shoot_message = f"Dealer used handsaw and shot {name} with real bullets. Sad"
                player_hp -= 2  
                player_hit_time = pygame.time.get_ticks()
            else:
                shoot_message = "Dealer used handsaw and shot itself with real bullets. Dumb dealer"
                ai_hp -= 2  

    elif bullet_type == 'fake' and num_fake_bullets > 0:
        num_fake_bullets -= 1
        emptygun_sound.play()

        if shooter == "player":
            if target == "ai":
                shoot_message = f"{name} used handsaw and shot dealer with fake bullets. LOL"
            else:
                shoot_message = f"{name} used handsaw and shot themselves with fake bullets!"
                handsaw_damage_pending_player = False
                return

        elif shooter == "ai":
            if target == "player":
                shoot_message = f"AI used handsaw and shot {name} with fake bullets."
            else:
                shoot_message = "Dealer used handsaw and shot itself with fake bullets."

    handle_hp_restoration()
    handle_ai_hp_restoration()
    check_game_over()

    handsaw_damage_pending_player = False
    handsaw_damage_pending_ai = False

totemplayer = font_13.render("You have been resurrected, cherish it.", True, WHITE)
totemplayer_x, totemplayer_y = (screen_width // 2 - totemplayer.get_width() // 2), (screen_height // 2 + 200)

totemdealer = font_13.render("Dealer has been resurrected.", True, WHITE)
totemdealer_x, totemdealer_y = (screen_width // 2 - totemdealer.get_width() // 2), (screen_height // 2 + 250)

def render_resurrection_message():
    if video_playing and current_video_clip == totem:
        if player_hp == 1 and not player_restored: 
            screen.blit(totemplayer, (totemplayer_x, totemplayer_y))
        if ai_hp == 1 and not ai_restored: 
            screen.blit(totemdealer, (totemdealer_x, totemdealer_y))

def bullets_reset():
    global bullets, num_fake_bullets, num_real_bullets
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

def handle_player_hit():
    global player_hp, player_hit_time, player_heart, broken_hearts
    player_hp -= 1 
    player_hit_time = pygame.time.get_ticks() 
    player_heart = broken_hearts
    print(f"Player was hit! Health is now {player_hp}.")

def handle_ai_hit():
    global ai_hp, ai_hit_time, ai_heart, broken_hearts

    ai_hp -= 1  
    ai_hit_time = pygame.time.get_ticks()  
    ai_heart = broken_hearts  

def player_turn():
    global turn, handsaw1_used_by_player, handsaw_damage_pending_player, num_real_bullets, num_fake_bullets
    global player_hp, ai_hp, player_hit_time, ai_hit_time, player_heart, ai_heart
    global medicine1_used_by_player, medicine_display_time, gun_sound, emptygun_sound, shoot_message
    global ai_waiting, ai_delay_start, video_playing, current_video_clip, video_start_time
    global magnifier1_used_by_player, current_round, magnifier_bullet_type

    mouse_pos = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()

    # Handling medicine in round 1
    if current_round == 1 and medicine1_rect.collidepoint(mouse_pos) and not medicine1_used_by_player:
        handle_medicine("player")
        medicine1_used_by_player = True
        medicine_display_time = pygame.time.get_ticks()
        return

    # Handling magnifier and handsaw in round 2
    if current_round == 2:
        if magnifier1_rect.collidepoint(mouse_pos) and not magnifier1_used_by_player:
            handle_magnifier("player")
            magnifier1_used_by_player = True
            return

        if handsaw1_rect.collidepoint(mouse_pos) and not handsaw1_used_by_player:
            handsaw1_used_by_player = True
            handsaw_damage_pending_player = True
            handsaw_sound.play()
            video_playing = True
            current_video_clip = handsawvideo1
            video_start_time = pygame.time.get_ticks()
            return

    # Handling handsaw usage
    if handsaw_damage_pending_player:
        if user_rect.collidepoint(mouse_pos):
            handle_handsaw_usage("player", "player")
        elif dealer_rect.collidepoint(mouse_pos):
            handle_handsaw_usage("player", "ai")
            handsaw_damage_pending_player = False
            turn = "ai"
            return

    # Prevent player from shooting within 500ms of getting hit
    if player_hit_time and current_time - player_hit_time < 500:
        return

    # Handle shooting self with a fake bullet
    if magnifier_bullet_type == 'fake':
        if user_rect.collidepoint(mouse_pos):
            shoot_message = f"{name} shot themselves with a fake bullet."
            emptygun_sound.play()
            magnifier_bullet_type = None  
            num_fake_bullets -= 1
            return  

    # Handle shooting self
    if user_rect.collidepoint(mouse_pos):
        if magnifier_bullet_type == 'real':
            bullet_type = 'real'
        else:
            bullet_type = random.choice(['real', 'fake']) if num_real_bullets > 0 and num_fake_bullets > 0 else 'fake'

        if bullet_type == 'real' and num_real_bullets > 0:
            num_real_bullets -= 1
            gun_sound.play()  
            shoot_message = f"{name} shot themselves with a real bullet."
            player_hp -= 1  
            player_hit_time = pygame.time.get_ticks() 
            player_heart = broken_hearts

            if player_hp <= 0:
                handle_hp_restoration()
            check_game_over()

        elif bullet_type == 'fake' and num_fake_bullets > 0:
            num_fake_bullets -= 1
            emptygun_sound.play()  
            shoot_message = f"{name} shot themselves with a fake bullet."
            return

    # Handle shooting the AI
    if dealer_rect.collidepoint(mouse_pos):
        if magnifier_bullet_type is not None:
            bullet_type = magnifier_bullet_type
        else:
            if num_real_bullets > 0:
                bullet_type = 'real'
            elif num_fake_bullets > 0:
                bullet_type = 'fake'
            else:
                bullet_type = None

        if bullet_type == 'real' and num_real_bullets > 0:
            num_real_bullets -= 1
            gun_sound.play()
            shoot_message = f"{name} shot the dealer with a real bullet!"
            ai_hp -= 1
            ai_hit_time = pygame.time.get_ticks()
            ai_heart = broken_hearts

            if ai_hp <= 0:
                handle_ai_hp_restoration()
            check_game_over()

        elif bullet_type == 'fake' and num_fake_bullets > 0:
            num_fake_bullets -= 1
            emptygun_sound.play()
            shoot_message = f"{name} shot the dealer with a fake bullet."

        turn = "ai"  
        ai_delay_start = pygame.time.get_ticks()
        ai_waiting = True

    # Reset the magnifier bullet type for the next turn
    magnifier_bullet_type = None
    check_if_all_bullets_used()

ai_self_shots = 0

def reset_ai_self_shots():
    global ai_self_shots
    ai_self_shots = 0

def handle_ai_round_1():
    global ai_hp, player_hp, num_real_bullets, num_fake_bullets, player_hit_time
    global medicine2_used_by_ai, ai_shoot_message, turn
    global medicine_display_time, medicine_delay_duration, medicine_message
    global ai_hit_time, ai_blood_duration, ai_heart, ai_self_shots
    global ai_delay_start, ai_waiting 

    current_time = pygame.time.get_ticks()

    if player_hp <= 0:
        check_game_over()
        return

    if medicine2_used_by_ai:
        if current_time < medicine_display_time + medicine_delay_duration:
            return 
        medicine_message = ""
        medicine_display_time = 0
        medicine2_used_by_ai = False 

        ai_delay_start = current_time
        ai_waiting = True 

    if ai_waiting:
        if current_time - ai_delay_start < 3000: 
            return 
        ai_waiting = False  

    if ai_hp < 2 and not medicine2_used_by_ai:
        handle_medicine("ai")  
        medicine2_used_by_ai = True
        medicine_display_time = current_time  
        ai_shoot_message = "Dealer used medicine!" 

    bullet_type = handle_shooting("ai", "player")  

    if bullet_type == "real" and num_real_bullets > 0:
        num_real_bullets -= 1
        gun_sound.play()

        if medicine2_used_by_ai:
            ai_shoot_message = f"Dealer used medicine and then shot {name} with a real bullet!"
        else:
            ai_shoot_message = f"Dealer shot {name} with a real bullet!"
        
        player_hp -= 1
        player_hit_time = current_time
        player_heart = broken_hearts  

        check_game_over() 
        turn = "player"  
        return

    elif bullet_type == "fake" and num_fake_bullets > 0:
        num_fake_bullets -= 1
        emptygun_sound.play()

        if medicine2_used_by_ai:
            ai_shoot_message = f"Dealer used medicine and then shot {name} with a fake bullet!"
        else:
            ai_shoot_message = f"Dealer shot {name} with a fake bullet!"
        
        turn = "player"  
        return

    if ai_hp <= 0:
        ai_hit_time = current_time  
        ai_hp = 0
        ai_heart = broken_hearts  
        ai_shoot_message = "Dealer was shot!" 
        check_game_over()

    if player_hp > 0:
        turn = "player"
    else:
        turn = "player"

def handle_ai_magnifier():
    global magnifier_delay_active, magnifier_delay_start, magnifier2_used_by_ai, magnifier_bullet_type, ai_shoot_message, ai_waiting, ai_delay_start

    if not magnifier2_used_by_ai:
        handle_magnifier("ai")  
        magnifier2_used_by_ai = True
        magnifier_delay_start = pygame.time.get_ticks()  
        magnifier_delay_active = True 
        ai_shoot_message = "Dealer used the magnifier!"
    return True

def handle_ai_handsaw():
    global handsaw2_used_by_ai, handsaw_damage_pending_ai, video_playing, current_video_clip, video_start_time
    global ai_waiting, ai_delay_start

    if not handsaw2_used_by_ai:
        handsaw2_used_by_ai = True
        handsaw_damage_pending_ai = True  
        handsaw_sound.play()  
        video_playing = True 
        current_video_clip = handsawvideo2 
        video_start_time = pygame.time.get_ticks()  

        ai_delay_start = pygame.time.get_ticks()
        ai_waiting = True  
    return False  

def handle_ai_round_2():
    global magnifier_bullet_type, ai_shoot_message, turn, num_real_bullets, num_fake_bullets, player_hp
    global player_hit_time, player_heart, ai_self_shots, ai_waiting, ai_delay_start, handsaw_damage_pending_ai
    global video_playing, current_video_clip, video_start_time
    global handsaw2_used_by_ai  
    current_time = pygame.time.get_ticks()

    if handle_ai_magnifier():
        if magnifier_bullet_type == "fake":
            emptygun_sound.play()
            ai_shoot_message = "Dealer saw: Fake bullet! AI shot itself."
            ai_self_shots += 1 
            num_fake_bullets -= 1 

            if not handsaw2_used_by_ai:
                handle_ai_handsaw()
                return 

            if not video_playing: 
                handle_handsaw_usage("ai", "ai") 
                handsaw_damage_pending_ai = False  
                return 

        elif magnifier_bullet_type == "real":
            # Check if AI used handsaw, if not, trigger it
            if not handsaw2_used_by_ai:
                handle_ai_handsaw()
                return  # Wait for handsaw video to finish
            
            # Ensure the handsaw video finishes playing before proceeding
            if not video_playing:
                handle_handsaw_usage("ai", "player")  # AI shoots player
                handsaw_damage_pending_ai = False  
                turn = "player"  # Switch turn after AI action
                return

    # Handle AI waiting state
    if ai_waiting:
        if current_time - ai_delay_start < 3000:  # Wait for 3 seconds
            return  # Still in waiting state
        ai_waiting = False  # Done waiting

    # Proceed with shooting after magnifier or handsaw actions
    bullet_type = handle_shooting("ai", "player")  
    if bullet_type == "real":
        num_real_bullets -= 1  
        gun_sound.play()
        ai_shoot_message = f"Dealer shot {name} with a real bullet!"
        player_hp -= 2  
        player_hit_time = current_time  
        player_heart = broken_hearts  
        check_game_over()
    else:
        num_fake_bullets -= 1  
        emptygun_sound.play()
        ai_shoot_message = f"Dealer shot {name} with a fake bullet!"

    # After the AI shoots (real or fake), switch turn to player
    turn = "player"

def handle_ai_round_3():
    global num_real_bullets, num_fake_bullets, ai_shoot_message, turn, player_hp

    # Check if player_hp is properly initialized and valid
    if player_hp is None or player_hp <= 0:
        print("Error: Invalid player_hp value.")
        return
    
    # Handle shooting logic
    bullet_type = handle_shooting("ai", "player")
    
    if bullet_type == "real":
        num_real_bullets -= 1
        gun_sound.play()
        ai_shoot_message = f"Dealer shot {name} with real bullet!"
        player_hp -= 1  # Ensure this doesn't go below 0
        player_hit_time = pygame.time.get_ticks()
        player_heart = broken_hearts
        
        # Ensure player_hp does not go below 0
        if player_hp <= 0:
            player_hp = 0
            handle_hp_restoration()  # Trigger any restoration logic if needed
        check_game_over()

    elif bullet_type == "fake":
        num_fake_bullets -= 1
        emptygun_sound.play()
        ai_shoot_message = f"Dealer shot {name} with fake bullet!"
    
    turn = "player"

def ai_turn():
    global turn, ai_waiting, ai_delay_start, ai_delay_duration
    global num_real_bullets, num_fake_bullets, ai_shoot_message, player_hp, ai_hp
    global handsaw2_used_by_ai, handsaw_damage_pending_ai, video_playing, current_video_clip, video_start_time
    global ai_hit_time, player_hit_time, ai_heart, player_heart, ai_waiting, medicine2_used_by_ai
    global magnifier2_used_by_ai, medicine_message, medicine_display_time, current_round, magnifier_bullet_type
    global ai_shoot_complete  # Flag to track if AI has completed its turn

    current_time = pygame.time.get_ticks()

    # Handle AI waiting time (delay before taking action)
    if ai_waiting:
        if current_time - ai_delay_start >= ai_delay_duration:  # Check if the delay time has passed
            if current_round == 1:
                handle_ai_round_1()  # AI's logic for Round 1
            elif current_round == 2:
                handle_ai_round_2()  # AI's logic for Round 2
            elif current_round == 3:
                handle_ai_round_3()  # AI's logic for Round 3
            ai_waiting = False  # AI is no longer waiting
            ai_shoot_complete = True  # AI has completed its action

    # Now, handle video completion check, only if the video clip is not None
    if current_video_clip is not None and current_time - video_start_time >= current_video_clip.duration:
        video_playing = False  # Mark the video as finished

    # Check if all bullets have been used
    check_if_all_bullets_used()

    # Ensure the AI's turn completes before switching back to the player's turn
    if not video_playing and not ai_waiting and ai_hp > 0 and ai_shoot_complete:
        turn = "player"  # Switch to the player's turn
        ai_shoot_complete = False  # Reset the flag for the next AI turn
        ai_waiting = False  # Ensure AI waiting is reset for the next turn

#Create player and AI objects
global player
player = Player() 
ai = AI()

# Define bullet text position
bullet_text_x = 30
bullet_text_y = 40
bullet_line_spacing = 10  

def render_bullet_info():
    bullet_header_text = f"Number of Bullets in Round {current_round}"
    bullet_header_surface = fontbulletbig.render(bullet_header_text, True, WHITE)
    screen.blit(bullet_header_surface, (bullet_text_x, bullet_text_y))
    
    real_bullets_y = bullet_text_y + bullet_header_surface.get_height() + bullet_line_spacing

    real_bullets_text = fontbulletsmall.render(f"Real Bullets: {num_real_bullets}", True, WHITE)
    screen.blit(real_bullets_text, (bullet_text_x, real_bullets_y))
    
    fake_bullets_y = real_bullets_y + real_bullets_text.get_height() + bullet_line_spacing

    fake_bullets_text = fontbulletsmall.render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
    screen.blit(fake_bullets_text, (bullet_text_x, fake_bullets_y))
##########################################################################################################################################################################
def player_name():
    input_box = pygame.Rect(screen_width // 2 - 300, screen_height // 2 - 75, 600, 120)
    color_inactive = pygame.Color(WHITE)
    color_active = pygame.Color(LIGHTRED)
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    sound_clickbox.play()
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    delete_sound.play()
                    text = text[:-1]  
                elif event.key == pygame.K_RETURN:
                    sound_clickbox.play()
                    return text 
                else:
                    if event.unicode.isprintable() and len(text) < 7:  # Limit to 7 words that can insert
                        text += event.unicode
                        delete_sound.play()

        screen.fill(BLACK)
        txt_surface = input_font_name.render(text, True, color)
        width = max(600, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 10)
        screen.blit(text_11_surface, (text_11_button_x, text_11_button_y))

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
                if text_5_button_rect.collidepoint(mouse_pos):
                    soundclick.play()
                    current_screen = SCREEN_PLAY 
                    pygame.display.set_caption('Life Roulette')
                    return

        screen.fill(BLACK)
        name_surface = font_10.render(f'Hello {name}, Welcome to Life Roulette', True, RED)
        screen.blit(name_surface, (screen_width // 2 - name_surface.get_width() // 2, screen_height // 2 - name_surface.get_height() // 2))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))

        pygame.display.flip()
        clock.tick(30)
##########################################################################################################################################################################
# Bullet setting for round 1
bullets = []
num_real_bullets = 5
num_fake_bullets = 3

bullets = [1] * num_real_bullets + [0] * num_fake_bullets

turn = "player"

shoot_message = " "
ai_shoot_message = " "
shoot_message_time = 0  
ai_shoot_message_time = 0  

#Define the rounds
current_round = 1

def roundmessage(message, background_color=BLACK):
    screen.fill(background_color)

    welcome_surface = font_turn.render(message, True, WHITE)
    welcome_rect = welcome_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(welcome_surface, welcome_rect)
    pygame.display.update()  
    pygame.time.delay(3000)
    screen.fill(background_color)
    pygame.display.update()

#Define for reset bullets for every round
def bullets_reset():
    global bullets, num_fake_bullets, num_real_bullets
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

def round_1():
    global turn, num_real_bullets, num_fake_bullets, bullets
    global handsaw1_used_by_player, handsaw_damage_pending_player
    global handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier2_used_by_ai, magnifier1_used_by_player
    global max_hp, player_hp

    num_real_bullets = 10
    num_fake_bullets = 3
    turn = "player"
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)
    bullets_reset()
    
    # Handsaw and magnifier not available in Round 1
    handsaw1_used_by_player = False
    handsaw_damage_pending_player = False
    handsaw2_used_by_ai = False
    handsaw_damage_pending_ai = False
    magnifier1_used_by_player = False
    magnifier2_used_by_ai = False

def round_2():
    global turn, num_real_bullets, num_fake_bullets, bullets, current_round
    global handsaw1_used_by_player, handsaw_damage_pending_player, handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier1_used_by_player, magnifier2_used_by_ai
    global player_hp, ai_hp
    global shoot_message, ai_shoot_message

    shoot_message = ""
    ai_shoot_message = ""

    # Player HP continues from the previous round
    ai_hp = 2

    # Define bullets for round 2
    num_real_bullets = 3
    num_fake_bullets = 2
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)

    handsaw1_used_by_player = False
    handsaw_damage_pending_player = False
    handsaw2_used_by_ai = False
    handsaw_damage_pending_ai = False
    magnifier1_used_by_player = False
    magnifier2_used_by_ai = False

    current_round = 2

    roundmessage("Welcome to Round 2")
    turn = "ai"  
    ai_delay_start = pygame.time.get_ticks() 
    ai_waiting = True  

def render_items_in_round_2():
    if current_round == 2:
        # Show magnifier and handsaw for player and AI 
        if not magnifier1_used_by_player:
            screen.blit(magnifier1, magnifier1_rect)
        if not handsaw1_used_by_player:
            screen.blit(handsaw1, handsaw1_rect)
        if not magnifier2_used_by_ai:
            screen.blit(magnifier2, magnifier2_rect)
        if not handsaw2_used_by_ai:
            screen.blit(handsaw2, handsaw2_rect)

def round_3():
    global turn, num_real_bullets, num_fake_bullets, bullets, current_round
    global handsaw1_used_by_player, handsaw_damage_pending_player, handsaw2_used_by_ai, handsaw_damage_pending_ai
    global magnifier1_used_by_player, magnifier2_used_by_ai
    global player_hp, ai_hp
    global shoot_message, ai_shoot_message
    global ai_delay_start, ai_waiting  

    shoot_message = ""  
    ai_shoot_message = "" 

    # Player HP continues from the previous round
    # Reset AI's HP for the final round
    ai_hp = 1

    # Set up the number of real and fake bullets for the final round
    num_real_bullets = 2
    num_fake_bullets = 2
    bullets = [1] * num_real_bullets + [0] * num_fake_bullets
    random.shuffle(bullets)  

    # Set the status of the handsaw and magnifier items
    handsaw1_used_by_player = False
    handsaw_damage_pending_player = False  
    handsaw2_used_by_ai = False  
    handsaw_damage_pending_ai = False  
    magnifier1_used_by_player = False  
    magnifier2_used_by_ai = False 

    current_round = 3

    roundmessage("Welcome to Final Round")

    turn = "ai"

    ai_delay_start = pygame.time.get_ticks()  
    ai_waiting = True 

def current_bullet():
    global bullets

    if bullets:
        return bullets[0] 
    else:
        return None  
##########################################################################################################################################################################
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
                    soundclick.play()
                    current_screen = SCREEN_PLAY
                    pygame.display.set_caption('Storyline')
                elif button_text3_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_HOW_TO_PLAY
                    pygame.display.set_caption('How to Play')

            elif current_screen == SCREEN_PLAY:
                if text_5_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_STORY1
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_MAIN

            # How to Play screen
            elif current_screen == SCREEN_HOW_TO_PLAY:
                if text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

            # Story screens
            elif current_screen == SCREEN_STORY1:
                if text_5_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_STORY2
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_PLAY

            elif current_screen == SCREEN_STORY2:
                if text_5_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_STORY3
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_STORY1

            elif current_screen == SCREEN_STORY3:
                if text_5_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    dealerlaugh.play()
                    current_screen = SCREEN_STORY4
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_STORY2

            elif current_screen == SCREEN_STORY4:
                if text_5_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    show_input_box = True
                    current_screen = SCREENNAME
                    pygame.display.set_caption('Enter your Name')
                elif text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_STORY3
            
            elif current_screen == SCREENNAME:
                name = player_name()
                pygame.display.set_caption('Storyline') 
                
            elif current_screen == SCREEN_STORY5:
                if text_5_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    show_input_box = True
                    current_screen = SCREEN_PLAYMAZE
                    pygame.display.set_caption('Play Maze?')
                elif text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREENNAME
                    pygame.display.set_caption('Enter your name')    

            elif current_screen == SCREEN_PLAYMAZE:
                if text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_STORY5
                    pygame.display.set_caption('Storyline') 
                if text_16_button_rect.collidepoint(event.pos): #YES
                    soundclick.play()
                    current_screen = SCREEN_MAZE
                    pygame.display.set_caption('MAZE')
                if text_17_button_rect.collidepoint(event.pos): #No
                    soundclick.play()
                    SCREENDISPLAY(name)
                    current_screen = SCREEN_PLAY1
                    pygame.display.set_caption('Life Roulette')          
            
            elif current_screen == SCREEN_MAZE:
                if text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    SCREENDISPLAY(name)
                    current_screen = SCREEN_PLAY1
                    pygame.display.set_caption('Ending')
                SCREENDISPLAY(name)

            elif current_screen == SCREEN_ENDING1:
                if text_5_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    show_input_box = True
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Ending')
                elif text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Ending') 
                    pygame.display.flip()
                    time.sleep(3)  
                    pygame.quit()
                    sys.exit()  
                
                else:
                    pygame.display.update()

            elif current_screen == SCREEN_PLAY1:
                if text_4_button_rect.collidepoint(event.pos):
                    soundclick.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

                if turn == "player":
                    player_turn()  # Handle player actions

                if player_hp <= 0:
                    handle_hp_restoration()

                if current_round == 1:
                    if not medicine1_used_by_player:
                        screen.blit(medicine1, medicine1_rect)
                    if not medicine2_used_by_ai:
                            screen.blit(medicine2, medicine2_rect)

                elif current_round == 2:
                    render_items_in_round_2()

    if turn == "ai" and not ai_waiting:
        ai_delay_start = pygame.time.get_ticks() 
        ai_waiting = True  

    if turn == "ai" and ai_waiting:
        current_time = pygame.time.get_ticks()
        if current_time - ai_delay_start >= ai_delay_duration:  
            ai_turn()  
            ai_waiting = False  

            if ai_hp <= 0:
                handle_ai_hp_restoration()

            render_health_restoration()

            turn = "player"

    if video_playing:
        if current_video_clip == handsawvideo2:
            if not center_video(current_video_clip, screen_width, screen_height): 
                video_playing = False 
                handle_handsaw_usage("ai", "player")  
                if ai_hp > 0:
                    turn = "player"  

        elif current_video_clip == totem:
            if turn == "player" and player_hp == 1:
                screen.blit(totemplayer, (totemplayer_x, totemplayer_y))
            elif turn == "ai" and ai_hp == 1:
                screen.blit(totemdealer, (totemdealer_x, totemdealer_y))

            if not center_video(current_video_clip, screen_width, screen_height):
                video_playing = False
                current_video_clip = None
                render_health_restoration()
                handle_ai_hp_restoration()
                handle_hp_restoration()

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
        create_rounded_speech_bubble("Well, well... finally answering, huh? Took your sweet time. Your little girl... she's with me now.",
        player_x + 400, player_y - 140, width=400, height=100)
        create_rounded_speech_bubble("You've been dodging me for months. 10 million. With that 20% interest, you owe me over 12 million. And now? Time's up. Your luck's run dry.",
        player_x + 500, player_y  + 10, width=400, height=140)
        draw_custom_shape(screen, WHITE, 700, 490, 210, 220)
        draw_multiline_text(screen, "Dad, I'm scared ! Help me!", fonttext1, RED, 700, 510, max_width=140)
        
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
        screen.blit(father, (player_x, player_y))
        create_rounded_speech_bubble("Please, listen, I... I don't have that kind of money right now! Let her go! Just give me more time! Ten days, that's all I'm asking for!",
        player_x + 400, player_y - 90, width=400, height=130)
          
    elif current_screen == SCREEN_STORY2:
        # Show on Story 2 Screen
        screen.fill(BLACK)
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(kidnapper, (player_x, player_y))
        create_rounded_speech_bubble("Time? You really think you get to bargain with me?",
        player_x + 400, player_y - 130, width=410, height=70)
        create_rounded_speech_bubble("Here's how it's going to work. You're going to play a game. My game. Win, and you'll get 20 days to gather my money. Lose? Well... your daughter won't see another sunrise.",
        player_x + 500, player_y +30, width=410, height=160)

    elif current_screen == SCREEN_STORY3:
        # Show on Story 3 Screen
        screen.fill(BLACK) 
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(father, (player_x, player_y))
        create_rounded_speech_bubble("I'll do it. I'll play your game. Just don't hurt her, please!!",
        player_x + 400, player_y - 90, width=400, height=70)

    elif current_screen == SCREEN_STORY4:
        # Show on Story 4 Screen
        screen.fill(BLACK) 
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))
        screen.blit(monster, (player_x, player_y)) 
        draw_custom_shape(screen, WHITE, 700, 300, 220, 220)
        draw_multiline_text(screen, "Good. Let's begin!", fonttext2, RED, 700, 320, max_width=170)
    
    elif current_screen == SCREENNAME:
        # Show on Enter your name Screen
        screen.fill(BLACK)
        name = player_name()  
        current_screen = SCREEN_STORY5

    elif current_screen == SCREEN_STORY5:
        screen.fill(BLACK) 
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(witch, (player_x, player_y))
        draw_custom_shape(screen, WHITE, 700, 100, 180, 200)
        draw_multiline_text(screen, "Ahhh, so you'll play... but will you survive?", font, LIGHTRED, 700, 100, max_width=140)
        create_rounded_speech_bubble("But there's more to this game than you know. A maze awaits you, twisting and shifting. Collect all the booster and find the exit, only then will you gain a precious life and an antidote to face the kidnapper.",
        player_x + 500, player_y - 10, width=400, height=190)
        create_rounded_speech_bubble("But beware -- get at least two boosts, and while you'll survive, but the antidote will be lost. ",
        player_x + 500, player_y + 190, width=400, height=100)
        create_rounded_speech_bubble("If you find one.... or none,your fate is sealed. You and your daughter will perish. No mercy. No escape. The maze decides, not you.",
        player_x + 500, player_y +300, width=400, height=130)
  
    elif current_screen == SCREEN_PLAYMAZE :
        screen.fill(BLACK)
        screen.blit(text_15_surface, (text_15_button_x, text_15_button_y))
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_16_surface, (text_16_button_x, text_16_button_y))
        screen.blit(text_17_surface, (text_17_button_x, text_17_button_y))

    elif current_screen == SCREEN_MAZE:
        screen.fill(BLACK)
        # Main game loop
        maze_running = True
        while maze_running:
            screen.fill((BLACK)) 

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Player movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        man.move(dx=-24, walls=walls)
                    if event.key == pygame.K_RIGHT:
                        man.move(dx=24, walls=walls)
                    if event.key == pygame.K_UP:
                        man.move(dy=-24, walls=walls)
                    if event.key == pygame.K_DOWN:
                        man.move(dy=24, walls=walls)

            for boost in boosts:
                if man.is_collision(boost):
                    pick_sound.play()
                    boost.destroy()
                    man.boost_count += 1

            # Handle enemy movements and chase logic
            for enemy in enemies:
                enemy.move(walls, man)
                if man.is_collision(enemy):
                    man.handle_collision_with_enemy()
                    collision_sound.play()
            
                # Check if player loses all lives
            if man.lives <= 0:
                current_screen = SCREEN_ENDING1
                break
            
            # Handle exit point collision
            if man.is_collision(exit_point):
                if man.boost_count >= 2:
                    SCREENDISPLAY(name)
                    current_screen = SCREEN_PLAY1  # Move to the next screen
                    maze_running = False  # Exit the maze loop
                else:
                    exit_message = "Get at least two boosts to exit"
                    message_start_time = pygame.time.get_ticks()
            
            if show_exit_message:
                current_time = pygame.time.get_ticks()
                if current_time - message_start_time > 2000:  #2 seconds
                    show_exit_message = False
                else:
                    message_surface = font_Maze.render(exit_message, True, WHITE)
                    screen.blit(message_surface, (screen.get_width() // 2 - message_surface.get_width() // 2, screen.get_height() // 2 - 350))

            # Drawing everything
            all_sprites.draw(screen)

                # Display player lives
            for i in range(man.lives):
                screen.blit(heart_img, (10 + i * 40, 10))

            # Update display and control frame rate
            pygame.display.flip()
            clock.tick(60)
       
    elif current_screen == SCREEN_PLAY1:
        # Show on Screen Play
        screen.fill(BLACK) 
        turn_message = turn_message = f"{name if turn == 'player' else 'Dealer'}'s Turn"
        turn_surface = font_turn.render(turn_message, True, WHITE)
        screen.blit(turn_surface, (350, 180))

        #Define for boost collected
        health_boost()
        if video_playing and current_video_clip:
            totem_rect = get_video_rect(totem, align="center")
            center_video(current_video_clip, screen_width, screen_height, x=totem_rect[0], y=totem_rect[1])
            render_resurrection_message()
            if not video_playing: 
                render_health_restoration()

        render_player_image()
        render_ai_image()
        draw_health_bars()
        render_bullet_info()

        if ai_hit_time and current_time - ai_hit_time <= ai_blood_duration:
            screen.blit(debtorblood, debtorblood_rect.topleft)
        else:
            screen.blit(dealer, dealer_rect.topleft)

        render_medicine_result()
        render_magnifier_result()

        shoot_surface = fontshoot.render(shoot_message, True, WHITE)
        screen.blit(shoot_surface, (50, 650))

        ai_shoot_surface = fontshoot.render(ai_shoot_message, True, WHITE)
        screen.blit(ai_shoot_surface, (50, 700))

        if current_round == 1:
            if not medicine1_used_by_player:
                screen.blit(medicine1, medicine1_rect)
            if not medicine2_used_by_ai:
                screen.blit(medicine2, medicine2_rect)

        elif current_round == 2:
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
            
    elif current_screen == SCREEN_ENDING1:
        screen.fill(BLACK) 
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))

        text_18_x = 0           #Can ajust for X position
        base_y = 450            # Starting Y position
        line_spacing = 60  
        fixed_y_positions = [base_y, base_y + line_spacing, base_y + 2 * line_spacing, base_y + 3 * line_spacing]

    # Render each line of the long text at fixed positions
        for i, line in enumerate(lines):
            text_18_surface = font_7.render(line, True, WHITE)  
            screen.blit(text_18_surface, (text_18_x, fixed_y_positions[i]))

        screen.blit(debtor, debtor_rect.topleft)
        
            
    pygame.display.flip()   
    pygame.time.Clock().tick(30)