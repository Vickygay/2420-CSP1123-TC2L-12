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

# Load and resize video clips
def resize_video(video_clip, size):
    return video_clip.resize(newsize=size)

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

# Background music in Menu
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.set_volume(0.0)
pygame.mixer.music.play(-1)

# Sound effects when clicking
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
BLUE = (0, 0, 255)
LIGHTGREY = (211, 211, 211)

# Player and AI images
player_img = pygame.image.load('player.png')
ai_img = pygame.image.load('dealer.png')
player_img = pygame.transform.scale(player_img, (200, 200))
ai_img = pygame.transform.scale(ai_img, (200, 200))
handsaw1 = pygame.image.load('handsaw1.png')
handsaw1 = pygame.transform.scale(handsaw1, (120, 120))
handsaw2 = pygame.image.load('handsaw2.png')
handsaw2 = pygame.transform.scale(handsaw2, (120, 120))
medicine1 = pygame.image.load('medicine1.png')
medicine1 = pygame.transform.scale(medicine1, (100, 100))
medicine2 = pygame.image.load('medicine2.png')
medicine2 = pygame.transform.scale(medicine2, (100, 100))

# Define rectangles for objects
handsaw1_rect = handsaw1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2))
handsaw2_rect = handsaw2.get_rect(topleft=(screen_width // 2 + 150, screen_height // 2))
medicine1_rect = medicine1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2 - 100))
medicine2_rect = medicine2.get_rect(topleft=(screen_width // 2 + 150, screen_height // 2 - 100))  

# Load heart images
heartsimage = pygame.image.load('hearts.png')
hearts = pygame.transform.scale(heartsimage, (50, 50))
broken_hearts = pygame.image.load('broken_hearts.png')
broken_hearts = pygame.transform.scale(broken_hearts, (50, 50))

# Blood effects
debtorblood = pygame.image.load('debtorblood.png')
debtorblood = pygame.transform.scale(debtorblood, (200, 250))
debtorblood_rect = debtorblood.get_rect(topleft=(740, 285))
playerblood = pygame.image.load('playerblood.png')
playerblood = pygame.transform.scale(playerblood, (200, 300))
playerblood_rect = playerblood.get_rect(topleft=(50, 230))

# Define areas for clicking
player_rect = player_img.get_rect(topleft=(50, 300))
ai_rect = ai_img.get_rect(topleft=(750, 300))

# Turn indicator text
font_turn = pygame.font.Font("Creepster.ttf", 60)
font13 = pygame.font.Font("Creepster.ttf", 50)
turn_message = "Player's Turn"
font = pygame.font.Font("Gloria.ttf", 30)
font_12_size = 36
font_12_path = "Nerko.ttf"
font_12 = pygame.font.Font(font_12_path, font_12_size)

# Variables to track turns and bullets
num_real_bullets = 5
num_fake_bullets = 3
turn = "player"
shoot_message = " "
ai_shoot_message = " "
medicine_message = ""  
medicine_display_time = 0  

# Player and AI health
max_hp = 1
player_hp = max_hp
ai_hp = max_hp

# Time tracking for AI delay
ai_delay_start = 0
ai_delay_duration = 3000  # 3 seconds delay for AI to choose
ai_waiting = False

# Time tracking for changing AI image
ai_hit_time = None
ai_blood_duration = 3000  # 3 seconds for blood effect

# Time tracking for changing player image
player_hit_time = None
player_blood_duration = 3000  # 3 seconds for blood effect

# Flags to control heart state
player_heart = hearts
ai_heart = hearts

# Global variables to ensure they are initialized
handsaw_used_by_player = False
handsaw_used_by_ai = False
medicine1_used_by_player = False
medicine2_used_by_ai = False
playing_totem = False 

# Function to draw health bars using hearts
def draw_health_bars():
    screen.blit(player_heart, (50, 50))
    screen.blit(ai_heart, (900, 50))

# Add restoration flags for both player and AI
player_restored = False
ai_restored = False

# Function to handle HP restoration and video playback
def handle_hp_restoration():
    global player_hp, video_playing, current_video_clip, video_start_time, player_restored, player_heart, playing_totem, restore_after_video

    if player_hp <= 0 and not player_restored:
        player_heart = broken_hearts
        video_playing = True
        current_video_clip = totem
        video_start_time = pygame.time.get_ticks()
        player_restored = True
        playing_totem = True
        restore_after_video = True
        totem_sound.play()

def handle_ai_hp_restoration():
    global ai_hp, video_playing, current_video_clip, video_start_time, ai_restored, ai_heart, playing_totem, restore_after_video

    if ai_hp <= 0 and not ai_restored:
        ai_heart = broken_hearts
        video_playing = True
        current_video_clip = totem
        video_start_time = pygame.time.get_ticks()
        ai_restored = True
        playing_totem = True
        restore_after_video = True
        totem_sound.play()

# Restore back original heart after the totem video
def restore_hearts():
    global player_heart, ai_heart, player_restored, ai_restored, playing_totem, player_hp, ai_hp

    if player_restored:
        player_hp = 1
        player_heart = hearts
    if ai_restored:
        ai_hp = 1
        ai_heart = hearts
    playing_totem = False

# Expired medicine function (handles both player and AI)
def handle_medicine(who_used):
    global player_hp, ai_hp, medicine_message, medicine1_used_by_player, medicine2_used_by_ai, medicine_display_time, video_playing, current_video_clip, playing_totem

    medicine_outcome = random.choice(['heal', 'damage'])
    
    if who_used == "player":
        if medicine_outcome == 'heal':
            medicine_message = "Player healed! +1 HP"
            player_hp = min(player_hp + 1, max_hp)
        else:
            medicine_message = "Player damaged! -1 HP"
            player_hp = max(player_hp - 1, 0)
            if player_hp <= 0 and not player_restored:
                video_playing = True
                current_video_clip = totem
                playing_totem = True
        medicine1_used_by_player = True 
        medicine1 = pygame.Surface((0, 0))  

    elif who_used == "ai":
        if medicine_outcome == 'heal':
            medicine_message = "AI healed! +1 HP"
            ai_hp = min(ai_hp + 1, max_hp)
        else:
            medicine_message = "AI damaged! -1 HP"
            ai_hp = max(ai_hp - 1, 0)
            if ai_hp <= 0 and not ai_restored:
                video_playing = True
                current_video_clip = totem
                playing_totem = True
        medicine2_used_by_ai = True  
        medicine2 = pygame.Surface((0, 0))  

    medicine_display_time = pygame.time.get_ticks() 

# Function to render the medicine result message with transparency
def render_medicine_result():
    global medicine1_used_by_player, medicine2_used_by_ai
    current_time = pygame.time.get_ticks()
    
    if (medicine1_used_by_player or medicine2_used_by_ai) and current_time - medicine_display_time <= 3000:
        box_width, box_height = 450, 50
        box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2 - 200, box_width, box_height)
        
        # Create a surface with alpha transparency
        transparent_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        transparent_surface.fill((255, 255, 255, 128)) 

        medicine_surface = font13.render(medicine_message, True, (255, 0, 0, 128))  
        text_rect = medicine_surface.get_rect(center=box_rect.center)
        
        # Blit the transparent box and the text onto the screen
        screen.blit(transparent_surface, box_rect.topleft)
        screen.blit(medicine_surface, text_rect.topleft)
    else:
        # Reset medicine flags after message disappears
        medicine1_used_by_player = False
        medicine2_used_by_ai = False

# Function to hide the medicine and handsaw once they're used (remove medicine image)
def player_turn():
    global turn, num_real_bullets, num_fake_bullets, shoot_message, player_hp, ai_hp, ai_delay_start, ai_waiting, ai_hit_time, player_hit_time
    global handsaw_used_by_player, medicine1_used_by_player, handsaw_used_by_ai, medicine2_used_by_ai  # Added necessary global variables

    shoot_message = ""

    mouse_pos = pygame.mouse.get_pos()

    # Check if player clicked on handsaw1
    if handsaw1_rect.collidepoint(mouse_pos) and not handsaw_used_by_player:
        bullet_type = random.choice(['real', 'fake'])
        if bullet_type == 'real':
            num_real_bullets -= 1
            gun_sound.play()
            shoot_message = "You used handsaw! -2 HP"
            ai_hp -= 2  
            handsaw_used_by_player = True  # Mark handsaw as used
            handsaw_sound.play()
            turn = "ai"
            ai_delay_start = pygame.time.get_ticks()  
            ai_waiting = True
        else:
            shoot_message = "Fake bullet, no effect."
            turn = "ai"
            ai_delay_start = pygame.time.get_ticks() 
            ai_waiting = True
    
    # Check if player clicked on medicine1
    elif medicine1_rect.collidepoint(mouse_pos) and not medicine1_used_by_player:
        handle_medicine("player")
        medicine1_used_by_player = True  # Mark medicine as used
        turn = "player" 
    
    # Check if player clicked on AI (AI shooting logic)
    elif ai_rect.collidepoint(mouse_pos):
        bullet_type = random.choice(['real', 'fake'])
        if bullet_type == 'real' and num_real_bullets > 0:
            num_real_bullets -= 1
            gun_sound.play()
            shoot_message = "You shot the AI with a real bullet!"
            ai_hp -= 1
            ai_hit_time = pygame.time.get_ticks()  # Track when AI was shot
            if ai_hp <= 0:
                handle_ai_hp_restoration()
            turn = "ai"
            ai_delay_start = pygame.time.get_ticks()
            ai_waiting = True
        elif bullet_type == 'fake' and num_fake_bullets > 0:
            num_fake_bullets -= 1
            emptygun_sound.play()
            shoot_message = "You shot the AI with a fake bullet!"
            turn = "ai"
            ai_delay_start = pygame.time.get_ticks()
            ai_waiting = True

    # Continue with the normal shooting logic if player shoots themselves
    elif player_rect.collidepoint(mouse_pos):
        bullet_type = random.choice(['real', 'fake'])
        if bullet_type == 'real' and num_real_bullets > 0:
            num_real_bullets -= 1
            gun_sound.play()
            shoot_message = "You shot yourself with a real bullet!"
            player_hp -= 1
            player_hit_time = pygame.time.get_ticks()  # Track when player was shot
            if player_hp <= 0:
                handle_hp_restoration()  
            turn = "ai"
            ai_delay_start = pygame.time.get_ticks()  
            ai_waiting = True
        elif bullet_type == 'fake' and num_fake_bullets > 0:
            num_fake_bullets -= 1
            emptygun_sound.play()
            shoot_message = "You shot yourself with a fake bullet!"
            turn = "ai"
            ai_delay_start = pygame.time.get_ticks()  
            ai_waiting = True

def ai_turn():
    global turn, num_real_bullets, num_fake_bullets, ai_shoot_message, player_hp, ai_hp, ai_waiting, ai_hit_time, player_hit_time
    global medicine2_used_by_ai  # Declare medicine2_used_by_ai as global

    ai_shoot_message = ""

    # AI makes a decision based on its current health
    if ai_hp <= 0.5: 
        if not medicine2_used_by_ai:
            handle_medicine("ai")
            medicine2_used_by_ai = True  # Mark medicine as used
            ai_shoot_message = "AI used medicine2!"
            turn = "player"
        return

    # If AI health is fine, randomly choose between using handsaw2 or shooting
    action_choice = random.choice(["use_handsaw2", "shoot"])

    if action_choice == "use_handsaw2" and not handsaw_used_by_ai:
        # AI uses the handsaw
        bullet_type = random.choice(['real', 'fake'])
        if bullet_type == 'real':
            num_real_bullets -= 1
            gun_sound.play()
            ai_shoot_message = "AI used handsaw2! -2 HP to you!"
            player_hp -= 2
            handsaw_used_by_ai = True  # Mark handsaw as used
            handsaw_sound.play()
        else:
            ai_shoot_message = "AI used handsaw2 but it was a fake!"
        turn = "player"
        return

    # AI chooses to shoot either itself or the player
    target = random.choice(["player", "ai"])

    bullet_type = random.choice(['real', 'fake'])
    if bullet_type == 'real' and num_real_bullets > 0:
        num_real_bullets -= 1
        gun_sound.play()

        if target == "player":
            ai_shoot_message = "AI shot you with a real bullet!"
            player_hp -= 1
            player_hit_time = pygame.time.get_ticks()
            if player_hp <= 0:
                handle_hp_restoration()  
            turn = "player"
        elif target == "ai":
            ai_shoot_message = "AI shot itself with a real bullet!"
            ai_hp -= 1
            ai_hit_time = pygame.time.get_ticks()
            if ai_hp <= 0:
                handle_ai_hp_restoration()
            turn = "player"
    elif bullet_type == 'fake' and num_fake_bullets > 0:
        num_fake_bullets -= 1
        emptygun_sound.play()

        if target == "player":
            ai_shoot_message = "AI shot you with a fake bullet!"
            turn = "player"
        elif target == "ai":
            ai_shoot_message = "AI shot itself with a fake bullet!"
            turn = "player"

    ai_waiting = False

# Define video playback states
video_playing = False
current_video_clip = None
video_start_time = 0

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == "player":
                mouse_pos = pygame.mouse.get_pos()
                
                if handsaw1_rect.collidepoint(mouse_pos):
                    video_playing = True
                    current_video_clip = handsawvideo1
                    video_start_time = pygame.time.get_ticks()
                    handsaw1 = pygame.Surface((0, 0))  
                    handsaw_sound.play()  
                else:
                    player_turn()

            if turn == "ai":
                mouse_pos = pygame.mouse.get_pos()
                
                if handsaw2_rect.collidepoint(mouse_pos):
                    video_playing = True
                    current_video_clip = handsawvideo2
                    video_start_time = pygame.time.get_ticks()
                    handsaw2 = pygame.Surface((0, 0))  
                    handsaw_sound.play()  
                else:
                    player_turn()


    if video_playing:
        current_time = pygame.time.get_ticks() - video_start_time
        frame_time = current_time / 1000  

        if frame_time < current_video_clip.duration:
            frame = get_frame_as_surface(current_video_clip.get_frame(frame_time))
            frame_rect = frame.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(frame, frame_rect.topleft)
        else:
            video_playing = False
            current_video_clip = None
            if playing_totem:  
                restore_hearts()  

    if player_hp <= 0 or ai_hp <= 0:
        handle_hp_restoration()

    if turn == "ai" and ai_waiting:
        current_time = pygame.time.get_ticks()
        if current_time - ai_delay_start >= ai_delay_duration:  
            ai_turn()  

    # Render the turn message
    turn_message = f"{'Player' if turn == 'player' else 'AI'}'s Turn"
    turn_surface = font_turn.render(turn_message, True, WHITE)
    screen.blit(turn_surface, (350, 50))

    # Display the player image or playerblood image
    if player_hit_time and current_time - player_hit_time <= player_blood_duration:
        screen.blit(playerblood, playerblood_rect.topleft)
    else:
        screen.blit(player_img, player_rect.topleft)

    # Display AI image or debtorblood depending on the timing
    if ai_hit_time and current_time - ai_hit_time <= ai_blood_duration:
        screen.blit(debtorblood, debtorblood_rect.topleft)
    else:
        screen.blit(ai_img, ai_rect.topleft)

    # Draw health bars
    draw_health_bars()

    # Show medicine result if it was used
    render_medicine_result()

    shoot_surface = font.render(shoot_message, True, WHITE)
    screen.blit(shoot_surface, (50, 600))

    ai_shoot_surface = font.render(ai_shoot_message, True, WHITE)
    screen.blit(ai_shoot_surface, (50, 700))

    real_bullets_text = font_12.render(f"Real Bullets: {num_real_bullets}", True, WHITE)
    fake_bullets_text = font_12.render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
    screen.blit(real_bullets_text, (30, 150))
    screen.blit(fake_bullets_text, (750, 150))

    if not medicine1_used_by_player:
        screen.blit(medicine1, medicine1_rect)
    if not medicine2_used_by_ai:
        screen.blit(medicine2, medicine2_rect)

    if not handsaw_used_by_player:
        screen.blit(handsaw1, handsaw1_rect)
    if not handsaw_used_by_ai:
        screen.blit(handsaw2, handsaw2_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
