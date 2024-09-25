import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np
import random
import turtle
import math
import time


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
gun_sound = pygame.mixer.Sound("gunsound.mp3")
emptygun_sound = pygame.mixer.Sound("emptygun.mp3")
delete_sound = pygame.mixer.Sound("delete.mp3")
ring_sound = pygame.mixer.Sound("ring.mp3")


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

text_12 = "Do you want to play maze?"
text_12_surface = font_3.render(text_12, True, WHITE)

text_13 = "YES"
text_13_surface = font_3.render(text_13, True, WHITE)

text_14 = "NO"
text_14_surface = font_3.render(text_14, True, WHITE)


# Fonts setting for How many bullets left
font_12_size = 36
font_12_path = "Nerko.ttf"
font_12 = pygame.font.Font(font_12_path, font_12_size)

font_13_size = 28
font_13_path = "Nerko.ttf"
font_13 = pygame.font.Font(font_13_path, font_13_size)

# Show (Life) on screen and positioning
life_text = "Life:"
life_text_surface = font_5.render(life_text, True, RED)
life_x = 3
life_y = 0

# Font setting for You lose
font_6_size = 40
font_6_path = 'Matemasie.ttf'
font_6 = pygame.font.Font(font_6_path, font_6_size)

# Font setting for You win
font_7_size = 40
font_7_path = 'Matemasie.ttf'
font_7 = pygame.font.Font(font_7_path, font_7_size)

# Show (You win) on screen and positioning
win_text = "Your humanity didn't betray you."
win_text_surface = font_7.render(win_text, True, WHITE)
win_x = 50
win_y = 50

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

text_12_width, text_12_height = text_12_surface.get_size()
text_12_button_x = (screen_width - text_11_width) // 2 -50
text_12_button_y = screen_width // 2- text_11_height - 200
text_12_button_rect = pygame.Rect(text_12_button_x, text_12_button_y, text_12_width, text_12_height)

text_13_width, text_13_height = text_13_surface.get_size()
text_13_button_x = (screen_width - text_13_width) // 2 -100
text_13_button_y = screen_height - text_13_height // 2 -400
text_13_button_rect = pygame.Rect(text_13_button_x, text_13_button_y, text_13_width, text_13_height)

text_14_width, text_14_height = text_14_surface.get_size()
text_14_button_x = (screen_width - text_14_width) // 2 +100
text_14_button_y = screen_height - text_14_height // 2 -400
text_14_button_rect = pygame.Rect(text_14_button_x, text_14_button_y, text_14_width, text_14_height)

# Image settings for magnifier
image_1 = pygame.image.load('magnifier.png') 
image_1_size = (200, 200)
image_1 = pygame.transform.scale(image_1, image_1_size)
image_1_width, image_1_height = image_1.get_size()
image_1_x = 70
image_1_y = (screen_height - image_1_height) // 2 + 150

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

image_2 = pygame.image.load('medicine.png') 
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

image_3 = pygame.image.load('handsaw.png') 
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

# Load and scale the image for Gun 
image_4 = pygame.image.load('Gun.png')
image_4_size = (150, 100)
image_4 = pygame.transform.scale(image_4, image_4_size)
image_4_width, image_4_height = image_4.get_size()
image_4_x = (screen_width - image_4_width) // 2
image_4_y = (screen_height - image_4_height) // 2

# Frame around the image 
frame_thickness_4 = 10
image_with_frame_surface_4 = pygame.Surface((image_4_width + 2 * frame_thickness_4, image_4_height + 2 * frame_thickness_4), pygame.SRCALPHA)
image_with_frame_surface_4.fill(WHITE)
pygame.draw.rect(image_with_frame_surface_4, DARKRED, (0, 0, image_with_frame_surface_4.get_width(), image_with_frame_surface_4.get_height()), frame_thickness_4)
image_with_frame_surface_4.blit(image_4, (frame_thickness_4, frame_thickness_4))

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
SCREEN_ENDING1 = 10
SCREEN_STORY9 = 11
SCREEN_PLAY1 = 12
SCREENNAME = 13
SCREENDISPLAY = 14
current_screen = SCREEN_MAIN

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

witchimage = pygame.image.load('witch.png')
witch = pygame.transform.scale(witchimage, (500,500))

#Display positions of images
player_x = 50
player_y = 200

# Load fonts
font = pygame.font.Font("DMRegular.ttf", 18)
font2 = pygame.font.Font('DMRegular.ttf', 26)
font3 = pygame.font.Font("Nerko.ttf", 22)




# Function to create a rounded rectangle
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)


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

##########################################################################################################################################################################

###################################################################################################

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
import pygame
import sys
import math
import random
import time

# Pygame initialization
pygame.init()

# Screen setup
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("A Maze Game")

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

# Font setup for text
font = pygame.font.Font(None, 36)

# Class Definitions
class Player(pygame.sprite.Sprite):
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

    def move(self, walls, player):
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
            elif char == "P":
                player.rect.x = screen_x
                player.rect.y = screen_y
            elif char == "Z":
                exit_point = Exit(screen_x, screen_y)
                all_sprites.add(exit_point)

# Define the game level
level_1 = [
"                                 ",
"                                 ",
"                                 ",
"        XXXXXXXXXXXXXXXXXXXXXXXXX",
"        XP XXXXXXXE          XXXX",
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
player = Player()
all_sprites.add(player)

# Initialize game state
setup_maze(level_1)

exit_message = ""
show_exit_message = False
message_start_time = 0

##########################################################################################################################################################################
# IMPORTANT!!!
show_input_box = False
running = True

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Settings for click on Play and move to storyline
            if current_screen == SCREEN_MAIN:
                if button_text2_rect.collidepoint(event.pos):
                    sound_play.play()
                    current_screen = SCREEN_PLAY
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
                if button_text2_rect.collidepoint(event.pos):
                    ring_sound.play()
                    current_screen = SCREEN_STORY2
                    pygame.display.set_caption('Storyline')
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
                    current_screen = SCREEN_STORY5
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY3
                    pygame.display.set_caption('Storyline')
            
            elif current_screen == SCREEN_STORY5:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    show_input_box = True
                    current_screen = SCREEN_PLAYMAZE
                    pygame.display.set_caption('Enter your Name')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY4 
                    pygame.display.set_caption('Storyline')
            
            elif current_screen == SCREEN_PLAYMAZE:
                if text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY5
                if text_13_button_rect.collidepoint(event.pos): #YES
                    sound_back.play()
                    current_screen = SCREEN_MAZE
                if text_14_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREENNAME
                    pygame.display.set_caption('Maze')          
            
            elif current_screen == SCREEN_MAZE:
                if text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREENNAME

            elif current_screen == SCREENNAME:
                name = player_name()
                SCREENDISPLAY(name)
            
            elif current_screen == SCREEN_PLAY1:
                if text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')
            
            elif current_screen == SCREEN_ENDING1:
                if text_5_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    show_input_box = True
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Ending')
                elif text_4_button_rect.collidepoint(event.pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Ending') 
                pygame.display.flip()
                time.sleep(3)  # Pause for 3 seconds to let the player see the message
                pygame.quit()
                sys.exit()  

            else:
                pygame.display.update()

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
        
        # Draw the transparent surface on top
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
        ring_sound.play
        create_rounded_speech_bubble("Well, well… finally answering, huh? Took your sweet time. Your little girl… she’s with me now.",
        player_x + 400, player_y - 140, width=400, height=80)
        create_rounded_speech_bubble("You’ve been dodging me for months. RM10,000,000. With that 20% interest, you owe me over RM12,000,000. And now? Time’s up. Your luck’s run dry.",
        player_x + 500, player_y  + 10, width=400, height=150)
        draw_custom_shape(screen, WHITE, 700, 490, 200)
        draw_multiline_text(screen, "Dad, please! Help me! Please!", font2, RED, 700, 500, max_width=140)
        
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
        create_rounded_speech_bubble("Please, listen, I… I don’t have that kind of money right now! Let her go! Just give me more time! Ten days, that’s all I’m asking for!",
        player_x + 400, player_y - 90, width=400, height=120)
          
    elif current_screen == SCREEN_STORY2:
        # Show on Story 2 Screen
        screen.fill(BLACK)
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(kidnapper, (player_x, player_y))
        create_rounded_speech_bubble("Time? You really think you get to bargain with me?",
        player_x + 400, player_y - 130, width=410, height=70)
        create_rounded_speech_bubble("Here’s how it’s going to work. You’re going to play a game. My game. Win, and you’ll get 20 days to gather my money. Lose? Well… your daughter won’t see another sunrise.",
        player_x + 500, player_y +30, width=410, height=140)

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

    elif current_screen == SCREEN_STORY5:
        screen.fill(BLACK) 
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y)) 
        screen.blit(witch, (player_x, player_y))
        draw_custom_shape(screen, WHITE, 700, 100, 200)
        draw_multiline_text(screen, "Ahhh, so you’ll play… but will you survive?", font, PURPLE, 700, 100, max_width=140)
        create_rounded_speech_bubble("But there’s more to this game than you know. A maze awaits you, twisting and shifting. Find the exit and collect three boosts... *only* then will you gain a precious life and an antidote to face the kidnapper",
        player_x + 450, player_y - 10, width=400, height=160)
        create_rounded_speech_bubble("But beware—get at least two boosts, and while you’ll survive, the antidote will be lost. Without it, you’ll face problems... deadly problems.",
        player_x + 500, player_y + 150, width=400, height=100)
        create_rounded_speech_bubble("If find one.... or none,your fate is sealed. You and your daughter will perish. No mercy. No escape. The maze decides, not you.",
        player_x + 500, player_y +250, width=400, height=100)

    elif current_screen == SCREEN_PLAYMAZE :
        screen.fill(BLACK)
        screen.blit(text_12_surface, (text_12_button_x, text_12_button_y))
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_14_surface, (text_14_button_x, text_14_button_y))
        screen.blit(text_13_surface, (text_13_button_x, text_13_button_y))

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

                # Player movement on key press (one box per press)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.move(dx=-24, walls=walls)
                    if event.key == pygame.K_RIGHT:
                        player.move(dx=24, walls=walls)
                    if event.key == pygame.K_UP:
                        player.move(dy=-24, walls=walls)
                    if event.key == pygame.K_DOWN:
                        player.move(dy=24, walls=walls)

            # Handle player-boost collisions
            for boost in boosts:
                if player.is_collision(boost):
                    pick_sound.play()
                    boost.destroy()
                    player.boost_count += 1

            # Handle enemy movements and chase logic
            for enemy in enemies:
                enemy.move(walls, player)
                if player.is_collision(enemy):
                    player.handle_collision_with_enemy()
                    collision_sound.play()
            
                # Check if player loses all lives
            if player.lives <= 0:
                current_screen = SCREEN_ENDING1
                break

            # Check if player reaches the exit and has enough boosts
            if player.is_collision(exit_point) and player.boost_count >= 2:
                current_screen = SCREENNAME
                break

            if player.is_collision(exit_point):
                if player.boost_count >= 2:
                    current_screen = SCREENNAME
                else:
                    exit_message = "Get at least two boosts to exit"
                    show_exit_message = True
                    message_start_time = pygame.time.get_ticks()
            
            # Show exit message for 2 seconds if necessary
            if show_exit_message:
                current_time = pygame.time.get_ticks()
                if current_time - message_start_time > 2000:  # 2000 ms = 2 seconds
                    show_exit_message = False
                else:
                    message_surface = font.render(exit_message, True, WHITE)
                    screen.blit(message_surface, (screen.get_width() // 2 - message_surface.get_width() // 2, screen.get_height() // 2 - 350))

            # Drawing everything
            all_sprites.draw(screen)

                # Display player lives
            for i in range(player.lives):
                screen.blit(heart_img, (10 + i * 40, 10))

            # Update display and control frame rate
            pygame.display.flip()
            clock.tick(60)
       
    
    elif current_screen == SCREENNAME:
        # Show on Enter your name Screen
        screen.fill(BLACK)
        name = player_name()  
        SCREENDISPLAY(name)
        current_screen = SCREEN_PLAY1

    elif current_screen == SCREEN_PLAY1:
        # Show on Screen Play
        screen.fill(BLACK) 
        screen.blit(text_8_surface, (text_8_button_x, text_8_button_y))
        screen.blit(image_with_frame_surface_4, (image_4_x, image_4_y))

    elif current_screen == SCREEN_ENDING1:
        screen.fill(BLACK) 
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))

    pygame.display.flip()   
    pygame.time.Clock().tick(30)

pygame.quit
    