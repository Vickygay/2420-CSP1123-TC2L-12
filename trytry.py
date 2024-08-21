import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np

pygame.init()

# Screen Size
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Life Roulette')

# Video
video_clip = VideoFileClip('shake22.mp4')  
fps = video_clip.fps  

#Frame per second
FPS = 60
clock= pygame.time.Clock()

def get_frame_as_surface(frame):
    frame_bgr = np.flip(frame, axis=0)  
    frame_bgr = np.rot90(frame_bgr, k=-1) 
    return pygame.surfarray.make_surface(frame_bgr)

# Background music in Menu
pygame.mixer.music.load('song.mp3')  
pygame.mixer.music.set_volume(0.4)  
pygame.mixer.music.play(-1)  # Play infinity

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
button_2_rect = pygame.Rect(text_2_x, text_2_y, text_2_width, text_2_height)
button_3_rect = pygame.Rect(text_3_x, text_3_y, text_3_width, text_3_height)

# Back button 
text_4_width, text_4_height = text_4_surface.get_size()
text_4_button_x = (screen_width - text_4_width) // 2 +400
text_4_button_y = screen_height - text_4_height // 2 -50
text_4_button_rect = pygame.Rect(text_4_button_x, text_4_button_y, text_4_width, text_4_height)

# Next button 
text_5_width, text_5_height = text_4_surface.get_size()
text_5_button_x = (screen_width - text_5_width) // 2 +400
text_5_button_y = screen_height - text_5_height // 2 -50
text_5_button_rect = pygame.Rect(text_5_button_x, text_5_button_y, text_5_width, text_5_height)

# Each screen states
SCREEN_MAIN = 0
SCREEN_PLAY = 1
SCREEN_HOW_TO_PLAY = 2
current_screen = SCREEN_MAIN

# Player and AI health bar
def draw_health_bar(screen, x, y, hp, max_hp):
    bar_length = 100
    bar_height = 10
    fill = (hp / max_hp) * bar_length
    border = pygame.Rect(x, y, bar_length, bar_height)
    fill = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(screen, GREEN, fill)
    pygame.draw.rect(screen, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 4, screen_height // 2)
        self.hp = 3
        self.max_hp = 3

#AI class
class AI(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width * 3 // 4, screen_height // 2)
        self.hp = 3
        self.max_hp = 3

#Create player and AI objects
player = Player()
ai = AI()

#Group the sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ai)


#####################################################################################################################################################
# IMPORTANT!!!
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == SCREEN_MAIN:
                if button_2_rect.collidepoint(mouse_pos):
                    sound_play.play()
                    current_screen = SCREEN_PLAY
                    pygame.display.set_caption('Playing')
                elif button_3_rect.collidepoint(mouse_pos):
                    sound_how_to_play.play()
                    current_screen = SCREEN_HOW_TO_PLAY
                    pygame.display.set_caption('How to Play')
            elif current_screen in [SCREEN_PLAY, SCREEN_HOW_TO_PLAY]:
                if text_4_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')
    
    # Key 
    keys = pygame.key.get_pressed()
    if current_screen == SCREEN_PLAY and keys[pygame.K_b]:
        current_screen = SCREEN_MAIN
        pygame.display.set_caption('Life Roulette')

    # Show on current screen
    if current_screen == SCREEN_MAIN:
        # Get the current frame
        current_time = pygame.time.get_ticks() / 1000.0  # Convert milliseconds to seconds
        frame_time = current_time % video_clip.duration  # Loop video
        frame = video_clip.get_frame(frame_time)
        
        # Convert frame to Pygame surface
        frame_surface = get_frame_as_surface(frame)
        
        screen.fill(BLACK)
        
        # Draw the video frame
        screen.blit(frame_surface, (0, 0))
        
        # Draw the transparent surface on top
        screen.blit(transparent_surface, (0, 0))
        
        # Draw both text surfaces
        screen.blit(text_1_surface, (text_1_x, text_1_y))  
        screen.blit(text_2_surface, (text_2_x, text_2_y))  
        screen.blit(text_3_surface, (text_3_x, text_3_y))  

    elif current_screen == SCREEN_PLAY:
        # Show on Play screen
        screen.fill(BLACK)
        play_1_text = "Life:"
        play_1_text_surface = font_2.render(play_1_text, True, RED)
        play_1_text_width, play_text_height = play_1_text_surface.get_size()
        play_1_text_x = (screen_width - play_1_text_width) // 2
        play_1_text_y = (screen_height - play_text_height) // 2
        screen.blit(play_1_text_surface, (play_1_text_x - 430, play_1_text_y -370))
        screen.blit(text_5_surface, (text_5_button_x, text_5_button_y))  
        draw_health_bar(screen, player.rect.x -100, player.rect.y - 340, player.hp, player.max_hp)
        draw_health_bar(screen, ai.rect.x, ai.rect.y - 340, ai.hp, ai.max_hp)

    elif current_screen == SCREEN_HOW_TO_PLAY:
        # Show on How to Play screen
        screen.fill(BLACK)
        how_text1_ = "Instructions"
        how_text1_surface = font_3.render(how_text1_, True, WHITE)
        how_text1_width, how_to_play_height = how_text1_surface.get_size()
        how_text1_x = (screen_width - how_text1_width) // 2
        how_text1_y = (screen_height - how_to_play_height) // 2 -350
        screen.blit(how_text1_surface, (how_text1_x, how_text1_y))
        screen.blit(text_4_surface, (text_4_button_x, text_4_button_y))  

    pygame.display.flip() 
    
    pygame.time.Clock().tick(fps)
    clock.tick(FPS)
pygame.quit()
