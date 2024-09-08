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
sound_clickbox = pygame.mixer.Sound("clickbox.mp3")

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

# Font setting for Click Shift first before enter your name
font_11_size = 45
font_11_path = 'Nerko.ttf'
font_11 = pygame.font.Font(font_11_path, font_11_size)

# Show (Click Shift first before enter your name)
text_11 = "Click Shift key before Entering your Name!"
text_11_surface = font_11.render(text_11, True, WHITE)

# Show (Life) on screen and positioning
life_text = "Life:"
life_text_surface = font_5.render(life_text, True, RED)
life_x = 3
life_y = 0

# Font setting for You lose
font_6_size = 40
font_6_path = 'Matemasie.ttf'
font_6 = pygame.font.Font(font_6_path, font_6_size)

# Show (You lose) on screen and positioning
lose_text = "Try to gamble again would ya?"
lose_text_surface = font_6.render(lose_text, True, RED)
lose_x = 200
lose_y = 200

# Font setting for You win
font_7_size = 40
font_7_path = 'Matemasie.ttf'
font_7 = pygame.font.Font(font_7_path, font_7_size)

# Show (You win) on screen and positioning
win_text = "Your humanity didn't betray you."
win_text_surface = font_7.render(win_text, True, WHITE)
win_x = 50
win_y = 50

# Font setting for Round two
font_8_size = 40
font_8_path = 'Matemasie.ttf'
font_8 = pygame.font.Font(font_8_path, font_8_size)

# Show (Round two) on screen and positioning
round_2 = "Round 2"
round_2_surface = font_8.render(round_2, True, WHITE)
round_2_x = 200
round_2_y = 100

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
text_11_button_y = screen_width // 2- text_11_height - 250
text_11_button_rect = pygame.Rect(text_11_button_x, text_11_button_y, text_11_width, text_11_height)

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

tooltip_text_2 = "MED KIT: 50% chance to get heal or else deduct"

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
dealer = pygame.transform.scale(dealer, (200,200)) 

user = pygame.image.load('player.png')
user = pygame.transform.scale(user, (200,200))

#Display positions of images
player_x = 50
player_y = 200

# Load fonts
font = pygame.font.Font("DMRegular.ttf", 18)
font3 = pygame.font.Font("Nerko.ttf", 22)

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
max_hp = 3
ai_hp = 3

# Class for Player and AI 
# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = user
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 10, screen_height // 2)
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.hp_positions = [(0, 0), (50, 0), (100, 0)]
        self.game_over = False

#Draw out the hearts for Player
    def draw_hp(self, surface):
        for i in range(self.max_hp):
            if i < self.current_hp:
                surface.blit(hearts, self.hp_positions[i])
            else:
                surface.blit(broken_hearts, self.hp_positions[i])

#Check for player's heart
    def player_check_hp(self):
        if self.current_hp <= 0:
            self.game_over = True

#Draw out defeated screen when player is defeated
    def draw_lose_screen(self):
        if self.game_over:
            screen.fill(BLACK)
            screen.blit(lose_text_surface, (lose_x, lose_y))

#Reset the gameplay after player was defeated
    def reset(self):
        self.current_hp = max_hp
        self.game_over = False
    

#AI class
class ai(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dealer
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width * 5 // 5.5, screen_height // 2)
        self.max_hp = ai_hp
        self.ai_current_hp = ai_hp
        self.ai_hp_positions = [(850, 0), (900, 0), (950, 0)]
        self.game_over = False

    def draw_hp(self, surface):
        for i in range(self.max_hp):
            if i < self.ai_current_hp:
                surface.blit(hearts, self.ai_hp_positions[i])
            else:
                surface.blit(broken_hearts, self.ai_hp_positions[i])

    def reset(self):
            self.ai_current_hp = ai_hp

    def ai_check_hp(self):
        if self.ai_current_hp <= 0:
            return True

def reset_game():
    player.reset()
    ai.reset()
    global current_screen
    current_screen = SCREEN_MAIN


#Create player and AI objects
player = Player()
ai = ai()   

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
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        return text
                    else:
                        text += event.unicode

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
                    current_screen = SCREEN_STORY5  
                    pygame.display.set_caption('Storyline')
                    return

        screen.fill(BLACK)
        name_surface = font_10.render(f'Hello, {name}, Welcome to Life Roulette', True, RED)
        screen.blit(name_surface, (screen_width // 2 - name_surface.get_width() // 2, screen_height // 2 - name_surface.get_height() // 2))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))

        pygame.display.flip()
        clock.tick(30)
##########################################################################################################################################################################
# Bullet setting for round 1
num_real_bullets = 5
num_fake_bullets = 3
turn = "player"
shoot_message = " "
ai_shoot_message = " "

def bullet():
    global num_real_bullets, num_fake_bullets, shoot_message
    mouse_pos = pygame.mouse.get_pos()
    
    #Define the first turn for player first
    if turn == "player":
        mouse_pos = pygame.mouse.get_pos()

    # Click on Image
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
                gun_sound.play()
                shoot_message = (f"{name} shot a Real bullet!")
            else:
                num_fake_bullets -= 1
                emptygun_sound.play()
                shoot_message = (f"{name} shot a Fake bullet!")
        else:
            shoot_message = "No bullets left!"

        turn == "ai"

    #Define the next turn after player for AI
    elif turn == "ai":
        ai_fire()
        turn == "player" #Switch to player after AI

#Define for AI to fire 
def ai_fire():
    global num_real_bullets_ai, num_fake_bullets_ai, ai_shoot_message

    if num_real_bullets_ai > 0 or num_fake_bullets_ai > 0:
        available_bullets_ai = []
        if num_real_bullets_ai > 0:
            available_bullets_ai.append("real")
        if num_fake_bullets_ai > 0:
            available_bullets_ai.append("fake")

        bullet_type_ai = random.choice(available_bullets_ai)

        if bullet_type_ai == "real":
            num_real_bullets_ai -= 1
            gun_sound.play()
            ai_shoot_message = "AI shot a Real bullet!"
        else:
            num_fake_bullets_ai -= 1
            emptygun_sound.play()
            ai_shoot_message = "AI shot a Fake bullet!"
    else:
        ai_shoot_message = "AI has no bullets left!"



##########################################################################################################################################################################
# IMPORTANT!!!
show_input_box = False
running = True
while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
#FOR TESTING PURPOSE        
        elif event.type == pygame.KEYDOWN:
            # Increase or decrease player HP
            if event.key == pygame.K_UP:
                player.current_hp = min(player.max_hp, player.current_hp + 1)  # Increase HP

            elif event.key == pygame.K_DOWN:
                player.current_hp = max(0, player.current_hp - 1)  # Decrease HP
            
            # Increase or decrease AI HP
            elif event.key == pygame.K_LEFT:
                ai.ai_current_hp = max(0, ai.ai_current_hp - 1)  # Decrease AI HP

            elif event.key == pygame.K_RIGHT:
                ai.ai_current_hp = min(ai.max_hp, ai.ai_current_hp + 1)  # Increase AI HP
      
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Settings for click on Play and move to storyline
            if current_screen == SCREEN_MAIN:
                if button_text2_rect.collidepoint(mouse_pos):
                    sound_play.play()
                    current_screen = SCREEN_PLAY
                    pygame.display.set_caption('Storyline')

                # Settings for How to Play and How to Play Back
                elif button_text3_rect.collidepoint(mouse_pos):
                    sound_how_to_play.play()
                    current_screen = SCREEN_HOW_TO_PLAY
                    pygame.display.set_caption('How to Play')
            elif current_screen == SCREEN_HOW_TO_PLAY:
                if text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

                # Setting for Play and move to Story 1 and Screen Play back to Main
            elif current_screen == SCREEN_PLAY:
                if text_5_button_rect.collidepoint(mouse_pos):
                    sound_next.play()
                    current_screen = SCREEN_STORY1
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')

                # Setting for Story 1 and move to Story 2 and Story 1 back to Play
            elif current_screen == SCREEN_STORY1:
                if text_5_button_rect.collidepoint(mouse_pos):
                    sound_next.play()
                    current_screen = SCREEN_STORY2
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_PLAY
                    pygame.display.set_caption('Storyline')

            elif current_screen == SCREEN_STORY2:
                if text_5_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY3
                    pygame.display.set_caption('Storyline')
                elif text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY1
                    pygame.display.set_caption('Storyline')
            
            elif current_screen == SCREEN_STORY3:
                if text_5_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY4
                elif text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY2
                    pygame.display.set_caption('Storyline')

            elif current_screen == SCREEN_STORY4:
                if text_5_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    show_input_box = True
                    current_screen = SCREENNAME
                    pygame.display.set_caption('Enter your Name')
                elif text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY3
                    pygame.display.set_caption('Storyline')

            elif current_screen == SCREENNAME:
                name = player_name()
                SCREENDISPLAY(name)
            
            elif current_screen == SCREEN_STORY5:
                if text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')
            
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
        how_text2_y = (screen_height - how_to_play_2_height) // 2 + 30
        screen.blit(how_text1_surface, (how_text1_x, how_text1_y))
        screen.blit(how_text2_surface, (how_text2_x, how_text2_y))
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y)) 
        screen.blit(image_with_frame_surface, (image_1_x, image_1_y))
        screen.blit(image_with_frame_surface_2, (image_2_x, image_2_y))
        screen.blit(image_with_frame_surface_3, (image_3_x, image_3_y))
        create_rounded_speech_bubble_2("The game consists of three rounds. At the start of the round the dealer loads the shotgun with a certain amount of red live shells and grey blanks shells in random order. Players then ask to choose either to shoot the dealer or themselves. Depending on whether the player chooses to shoot themselves or the dealer, if the shell is live then either the dealer or the player will lose a life. Each player has a certain amount of life depending on the round. At the first two round you will be save by defibrillators, at the third round where everything gets serious defibrillators will be cut off no more waking up.  Starting on round 2, a set of items will be distributed to you and the dealer. Every item will give you a different advantage.",
        player_x +6 , player_y -100 , width=900, height=255)

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

    elif current_screen == SCREEN_STORY5:
        # Show on Story 5 Screen
        screen.fill(BLACK) 
        all_sprites.draw(screen)        #Draw out the class and def for player and ai
        player.draw_hp(screen)
        player.player_check_hp()
        if player.game_over:
            player.draw_lose_screen()
            pygame.display.update()
            pygame.time.delay(5000)
            reset_game()
        else:
            pass
        ai.draw_hp(screen)
        

    pygame.display.flip()
    
    pygame.time.Clock().tick(30)