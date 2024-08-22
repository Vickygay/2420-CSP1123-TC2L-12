import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np


# Initialize Pygame
pygame.init()

# Set up display
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Life Roulette')

# Load the video using moviepy
video_clip = VideoFileClip('shake22.mp4')  # Replace with your video file path
fps = video_clip.fps  # Frames per second of the video

def get_frame_as_surface(frame):
    """ Convert a numpy array frame to a Pygame Surface. """
    frame_bgr = np.flip(frame, axis=0)  # Convert RGB to BGR (Pygame expects BGR)
    frame_bgr = np.rot90(frame_bgr, k=-1)  # Rotate 90 degrees clockwise
    return pygame.surfarray.make_surface(frame_bgr)

# Load and play background music
pygame.mixer.music.load('song.mp3')  # Replace with your music file
pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Play music looped (-1 means loop indefinitely)

# Load sounds for button clicks
sound_play = pygame.mixer.Sound('clicksound.mp3')
sound_how_to_play = pygame.mixer.Sound('clicksound.mp3')
sound_back = pygame.mixer.Sound('clicksound.mp3')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load the custom font for Life Roulette
font_1_size = 70
font_1_path = 'Creepster.ttf'  # Correct path to your .ttf file
font_1 = pygame.font.Font(font_1_path, font_1_size)

# Define and render the first text (Life Roulette)
text_1 = "Life Roulette"
text_1_surface = font_1.render(text_1, True, RED)

# Load the custom font for Start button
font_2_size = 60
font_2_path = 'Creepster.ttf'  
font_2 = pygame.font.Font(font_2_path, font_2_size)

# Define and render the second text (Start button)
text_2 = "Start"
text_2_surface = font_2.render(text_2, True, RED)

# Load the custom font for How to Play
font_3_size = 50
font_3_path = 'Creepster.ttf'  
font_3 = pygame.font.Font(font_3_path, font_3_size)

# Define and render the third text (How to Play)
text_3 = "How to Play"
text_3_surface = font_3.render(text_3, True, WHITE) 


# Define and render the Back button
font_back_size = 45
font_back_path = 'Matemasie.ttf'  
font_back = pygame.font.Font(font_back_path, font_back_size)
text_back = "Back"
text_back_surface = font_back.render(text_back, True, WHITE)

font_next_size = 45
font_next_path = 'Matemasie.ttf'  
font_next = pygame.font.Font(font_back_path, font_back_size)
text_next = "Next"
text_next_surface = font_back.render(text_back, True, WHITE)

font_4_size = 45
font_4_path = 'Matemasie.ttf'
font_4 = pygame.font.Font(font_4_path, font_4_size)

font_5_size = 45
font_5_path = 'Matemasie.ttf'
font_5 = pygame.font.Font(font_5_path, font_5_size)

text_4 = "Back"
text_4_surface = font_4.render(text_4, True, WHITE)

# Create a surface with transparency
transparent_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 0, 128))  # RGBA color, where A is alpha (0-255)

# Calculate text positions
text_1_width, text_1_height = text_1_surface.get_size()
text_1_x = (screen_width - text_1_width) // 2
text_1_y = (screen_height - text_1_height) // 2 -150

text_2_width, text_2_height = text_2_surface.get_size()
text_2_x = (screen_width - text_2_width) // 2
text_2_y = (screen_height - text_2_height) // 2 -25  

text_3_width, text_3_height = text_3_surface.get_size()
text_3_x = (screen_width - text_3_width) // 2
text_3_y = (screen_height - text_3_height) // 2 +75 

text_4_width, text_4_height = text_4_surface.get_size()
text_4_button_x = (screen_width - text_4_width) // 2 +400
text_4_button_y = screen_height - text_4_height // 2 -50
text_4_button_rect = pygame.Rect(text_4_button_x, text_4_button_y, text_4_width, text_4_height)

text_5 = "Next"
text_5_surface = font_5.render(text_5, True, WHITE)

# Define the button areas (x, y, width, height)
button_2_rect = pygame.Rect(text_2_x, text_2_y, text_2_width, text_2_height)
button_3_rect = pygame.Rect(text_3_x, text_3_y, text_3_width, text_3_height)

# Define the Back button area
text_back_width, text_back_height = text_back_surface.get_size()
back_button_x = (screen_width - text_back_width) // 2 +400
back_button_y = screen_height - text_back_height // 2 -50
back_button_rect = pygame.Rect(back_button_x, back_button_y, text_back_width, text_back_height)

text_next_width, text_next_height = text_next_surface.get_size()
next_button_x = (screen_width - text_next_width) // 2 +200
next_button_y = screen_height - text_next_height // 2 -50
next_button_rect = pygame.Rect(next_button_x, next_button_y, text_next_width, text_next_height)

# Define screen states
SCREEN_MAIN = 0
SCREEN_PLAY = 1
SCREEN_HOW_TO_PLAY = 2
SCREEN_STORY1 = 3
current_screen = SCREEN_MAIN

kidnapperimage = pygame.image.load('kidnapper.png')
kidnapper = pygame.transform.scale(kidnapperimage,(500,500))

manimage = pygame.image.load('father.png')
man = pygame.transform.scale(manimage,(500,500))


player_x = 50
player_y = 200

# Load fonts
font = pygame.font.SysFont(None, 24)

# Function to create a rounded rectangle
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

font2 = pygame.font.SysFont('Arial', 20, bold=True)

def draw_custom_shape(surface, color, x, y, size):
    points = [
        (x, y - size // 3),               # Top center point
        (x + size // 2, y - size // 3),   # Top right point
        (x + size // 1.5, y),             # Middle right point
        (x + size // 2, y + size // 3),   # Bottom right point
        (x, y + size // 3),               # Bottom center point
        (x - size // 2, y + size // 3),   # Bottom left point
        (x - size // 1.5, y),             # Middle left point
        (x - size // 2, y - size // 3)    # Top left point
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
    
    # Draw the bubble on the screen
    screen.blit(bubble_surface, (x, y))


def draw_multiline_text(surface, text, font, color, x, y, max_width, line_spacing=5):
    lines = wrap_text(text, font, max_width)
    total_height = len(lines) * font.get_height() + (len(lines) - 1) * line_spacing
    start_y = y - total_height // 2
    
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, start_y + i * (font.get_height() + line_spacing)))
        surface.blit(text_surface, text_rect)


# Main loop
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
                if back_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_MAIN
                    pygame.display.set_caption('Life Roulette')
                if next_button_rect.collidepoint(mouse_pos):
                    sound_back.play()
                    current_screen = SCREEN_STORY1
                    pygame.display.set_caption('Storyline')
    
    # Handle key presses
    keys = pygame.key.get_pressed()
    if current_screen == SCREEN_PLAY and keys[pygame.K_b]:
        current_screen = SCREEN_MAIN
        pygame.display.set_caption('Life Roulette')

    # Handle screen rendering based on current screen state
    if current_screen == SCREEN_MAIN:
        # Get the current frame
        current_time = pygame.time.get_ticks() / 1000.0  # Convert milliseconds to seconds
        frame_time = current_time % video_clip.duration  # Loop video
        frame = video_clip.get_frame(frame_time)
        
        # Convert frame to Pygame surface
        frame_surface = get_frame_as_surface(frame)
        
        # Clear the screen
        screen.fill(BLACK)
        
        # Draw the video frame
        screen.blit(frame_surface, (0, 0))
        
        # Draw the transparent surface on top
        screen.blit(transparent_surface, (0, 0))
        
        # Draw both text surfaces
        screen.blit(text_1_surface, (text_1_x, text_1_y))  # Position of the first text
        screen.blit(text_2_surface, (text_2_x, text_2_y))  # Position of the second text
        screen.blit(text_3_surface, (text_3_x, text_3_y))  # Position of the third text

    elif current_screen == SCREEN_PLAY:
        # Render the Play screen
        screen.fill(BLACK)
        play_1_text = ""
        play_1_text_surface = font_2.render(play_1_text, True, GREEN)
        play_1_text_width, play_text_height = play_1_text_surface.get_size()
        play_1_text_x = (screen_width - play_1_text_width) // 2
        play_1_text_y = (screen_height - play_text_height) // 2
        screen.blit(play_1_text_surface, (play_1_text_x, play_1_text_y))
        screen.blit(text_back_surface, (back_button_x, back_button_y))  # Draw the Back button
        screen.blit(text_next_surface, (next_button_x, next_button_y))
        
        screen.blit(kidnapper, (player_x, player_y))

        create_rounded_speech_bubble("Well, well, look who's finally answering his phone. Your little girl is with me now. You know why, don't you? You owe me RM10,000,000. And with that juicy 20% interest, it's now over RM12,000,000. You've been dodging me for months, wasting your money at the tables. But guess what? Your luck just ran out.",
        player_x + 400, player_y - 150, width=400, height=230)

        draw_custom_shape(screen, WHITE, 700, 500, 200)
        draw_multiline_text(screen, "Dad, please! Help me!", font, RED, 700, 500, max_width=140)
        

            

    elif current_screen == SCREEN_HOW_TO_PLAY:
        # Render the How to Play screen
        screen.fill(BLACK)
        how_to_play_text = "Instructions"
        how_to_play_surface = font_3.render(how_to_play_text, True, WHITE)
        how_to_play_width, how_to_play_height = how_to_play_surface.get_size()
        how_to_play_x = (screen_width - how_to_play_width) // 2
        how_to_play_y = (screen_height - how_to_play_height) // 2 -350
        screen.blit(how_to_play_surface, (how_to_play_x, how_to_play_y))
        screen.blit(text_back_surface, (back_button_x, back_button_y))  # Draw the Back button
    

    elif current_screen == SCREEN_STORY1:
        # Render the How to Play screen
        screen.fill(BLACK)
        how_to_play_text = "Storyline"
        how_to_play_surface = font_3.render(how_to_play_text, True, WHITE)
        how_to_play_width, how_to_play_height = how_to_play_surface.get_size()
        how_to_play_x = (screen_width - how_to_play_width) // 2
        how_to_play_y = (screen_height - how_to_play_height) // 2 -350
        screen.blit(how_to_play_surface, (how_to_play_x, how_to_play_y))
        screen.blit(text_back_surface, (back_button_x, back_button_y))
        screen.blit(man, (player_x, player_y))

        create_rounded_speech_bubble("Sorry sorry I didn’t have so much money now. Can you leave my daughter first? Give me one 10days. 10days! I will pay back the money for you!",
        player_x + 400, player_y - 90, width=400, height=150)

        
        

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(fps)



