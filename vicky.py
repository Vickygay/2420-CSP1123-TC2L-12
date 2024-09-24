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
totem = VideoFileClip('totem.mp4')
handsawvideo1 = VideoFileClip('handsawvideo1.mp4')
handsawvideo2 = VideoFileClip('handsawvideo2.mp4')

# Resize videos to fit the screen
video_size = (200, 200)
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
user = pygame.image.load('player.png')
user = pygame.transform.scale(user, (200, 200))
user_rect = user.get_rect(topleft=(50, 300))

dealer = pygame.image.load('dealer.png')
dealer = pygame.transform.scale(dealer, (200, 200))
dealer_rect = dealer.get_rect(topleft=(750, 300))

handsaw1 = pygame.image.load('handsaw1.png')
handsaw1 = pygame.transform.scale(handsaw1, (100, 100))
handsaw1_rect = handsaw1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2))
handsaw2 = pygame.image.load('handsaw2.png')
handsaw2 = pygame.transform.scale(handsaw2, (100, 100))
handsaw2_rect = handsaw2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2))

medicine1 = pygame.image.load('medicine1.png')
medicine1 = pygame.transform.scale(medicine1, (100, 100))
medicine1_rect = medicine1.get_rect(topleft=(screen_width // 2 - 300, screen_height // 2 - 100))
medicine2 = pygame.image.load('medicine2.png')
medicine2 = pygame.transform.scale(medicine2, (100, 100))
medicine2_rect = medicine2.get_rect(topleft=(screen_width // 2 + 170, screen_height // 2 - 100))

hearts = pygame.image.load('hearts.png')
hearts = pygame.transform.scale(hearts, (50, 50))
broken_hearts = pygame.image.load('broken_hearts.png')
broken_hearts = pygame.transform.scale(broken_hearts, (50, 50))

debtorblood = pygame.image.load('debtorblood.png')
debtorblood = pygame.transform.scale(debtorblood, (200, 250))
debtorblood_rect = debtorblood.get_rect(topleft=(740, 285))

playerblood = pygame.image.load('playerblood.png')
playerblood = pygame.transform.scale(playerblood, (200, 300))
playerblood_rect = playerblood.get_rect(topleft=(50, 230))

# Turn indicator text
font_turn = pygame.font.Font("Creepster.ttf", 60)
turn_message = "Player's Turn"
font = pygame.font.Font("Gloria.ttf", 28)
font_10 = pygame.font.Font("Gloria.ttf", 47)
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
max_hp = 3
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

# Function to restore player HP using the totem (only once)
def handle_player_totem():
    global player_hp, player_totem_used, player_can_be_eliminated, player_heart, playing_totem, video_playing, current_video_clip, video_start_time
    if player_hp <= 0 and not player_totem_used and not video_playing:
        current_video_clip = totem
        video_playing = True
        playing_totem = True
        video_start_time = pygame.time.get_ticks()
        totem_sound.play()
        player_totem_used = True  # Mark the totem as used
        player_can_be_eliminated = True  # The player can be eliminated next time their HP hits 0

# Function to restore AI HP using the totem (only once)
def handle_ai_totem():
    global ai_hp, ai_totem_used, ai_can_be_eliminated, ai_heart, playing_totem, video_playing, current_video_clip, video_start_time
    if ai_hp <= 0 and not ai_totem_used and not video_playing:
        current_video_clip = totem
        video_playing = True
        playing_totem = True
        video_start_time = pygame.time.get_ticks()
        totem_sound.play()
        ai_totem_used = True  # Mark the totem as used
        ai_can_be_eliminated = True

def handle_hp_restoration():
    global player_hp, player_can_be_eliminated, player_heart, playing_totem, player_restored, video_playing, current_video_clip, video_start_time, player_totem_used

    # If player's HP is zero, totem hasn't been used, and no video is playing, play totem video
    if player_hp <= 0 and not player_restored and not video_playing and not player_totem_used:
        current_video_clip = totem
        video_playing = True
        playing_totem = True
        video_start_time = pygame.time.get_ticks()
        totem_sound.play()  # Play the totem sound
    
    # After the totem video has finished, restore one heart
    if not video_playing and playing_totem:
        player_hp = 1  # Restore player health to 1
        player_heart = hearts  # Restore one broken heart to full heart
        player_can_be_eliminated = True  # Player can now be eliminated on the next hit
        player_restored = True  # Mark the player as restored to prevent further totem use
        player_totem_used = True  # Mark the totem as used for the player
        playing_totem = False  # Stop the totem flag to ensure it doesn't play again
        print("Player's health restored by totem!")

def handle_ai_hp_restoration():
    global ai_hp, ai_totem_used, ai_can_be_eliminated, ai_heart, playing_totem, video_playing, current_video_clip, video_start_time

    # If AI's HP is zero or below, totem hasn't been used, and no video is playing, play totem video
    if ai_hp <= 0 and not ai_totem_used and not video_playing:
        print("AI totem triggered")  # Debug message
        current_video_clip = totem
        video_playing = True
        playing_totem = True
        video_start_time = pygame.time.get_ticks()
        totem_sound.play()
        ai_totem_used = True  # Mark the totem as used
        ai_can_be_eliminated = True  # AI can now be eliminated next time its HP hits 0

    # After the totem video has finished, restore one heart
    if not video_playing and playing_totem:
        ai_hp = 1  # Restore AI health to 1
        ai_heart = hearts  # Restore one broken heart to full heart
        ai_can_be_eliminated = True  # AI can now be eliminated on the next hit
        playing_totem = False  # Stop the totem flag
        print("AI's health restored by totem!")

def check_game_over():
    global running

    # Game over if player HP is 0 and they've already used the totem
    if player_hp <= 0 and player_can_be_eliminated and player_totem_used:
        font_game_over = pygame.font.Font("Creepster.ttf", 100)
        game_over_surface = font_game_over.render("Game Over! Dealer Wins!", True, RED)
        game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False  # Stop the game loop

    # Game over if AI HP is 0 and they've already used the totem
    elif ai_hp <= 0 and ai_can_be_eliminated and ai_totem_used:
        font_game_over = pygame.font.Font("Creepster.ttf", 100)
        congrats_surface = font_game_over.render("Congrats! You Win!", True, GREEN)
        congrats_rect = congrats_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(congrats_surface, congrats_rect)
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False  # Stop the game loop

    # If AI HP is 0 and the totem has not been used, trigger AI totem
    if ai_hp <= 0 and not ai_totem_used:
        handle_ai_hp_restoration()  # Call the function to handle AI restoration

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
    if playing_totem:
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
    global player_hp, ai_hp, medicine_message, medicine1_used_by_player, medicine2_used_by_ai
    global medicine_display_time, player_heart, ai_heart, player_hit_time, ai_hit_time
    global player_totem_used, ai_totem_used, video_playing, current_video_clip, video_start_time, playing_totem

    medicine_outcome = random.choice(['heal', 'damage'])

    if who_used == "player":
        if medicine_outcome == 'heal':
            medicine_message = "Player healed! +1 HP"
            player_hp = min(player_hp + 1, max_hp)
            player_heart = hearts  # Set heart to normal if healed
        else:  # If the player gets damaged by medicine
            if player_hp - 1 <= 0 and not player_totem_used:
                handle_hp_restoration()  # Player saved by totem
            elif player_hp - 1 > 0:
                medicine_message = "Player damaged! -1 HP"
                player_hp -= 1
                player_heart = broken_hearts  # Set heart to broken if damaged
                player_hit_time = pygame.time.get_ticks()  # Track when player gets hit by medicine
            check_game_over()  # Check for game over
        medicine1_used_by_player = True

    elif who_used == "ai":
        if medicine_outcome == 'heal':
            medicine_message = "AI healed! +1 HP"
            ai_hp = min(ai_hp + 1, max_hp)
            ai_heart = hearts  # Set AI heart to normal if healed
        else:  # If the AI gets damaged by medicine
            if ai_hp - 1 <= 0 and not ai_totem_used:
                handle_ai_hp_restoration()  # AI saved by totem
            elif ai_hp - 1 > 0:
                medicine_message = "AI damaged! -1 HP"
                ai_hp -= 1
                ai_heart = broken_hearts  # Set AI heart to broken if damaged
                ai_hit_time = pygame.time.get_ticks()  # Track when AI gets hit by medicine
            check_game_over()  # Check for game over
        medicine2_used_by_ai = True

    medicine_display_time = pygame.time.get_ticks()

def render_medicine_result():
    current_time = pygame.time.get_ticks()

    # Show the result message for 3 seconds
    if (medicine1_used_by_player or medicine2_used_by_ai) and current_time - medicine_display_time <= 3000:
        box_width, box_height = 500, 50
        box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2 - 200, box_width, box_height)
        pygame.draw.rect(screen, LIGHTGREY, box_rect)
        
        # Change text color to WHITE for better visibility
        medicine_surface = font_10.render(medicine_message, True, WHITE)
        text_rect = medicine_surface.get_rect(center=box_rect.center)
        screen.blit(medicine_surface, text_rect.topleft)

def handle_handsaw_usage(shooter, target):
    global shoot_message, player_hp, ai_hp, ai_hit_time, player_hit_time, num_real_bullets, num_fake_bullets, handsaw_damage_pending_player, handsaw_damage_pending_ai

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

# Add a small delay (cooldown) after player shoots themselves to prevent rapid shooting
def player_turn():
    global turn, handsaw1_used_by_player, handsaw_damage_pending_player, num_real_bullets, num_fake_bullets
    global player_hp, ai_hp, player_hit_time, ai_hit_time, player_heart, ai_heart
    global medicine1_used_by_player, medicine_display_time, gun_sound, emptygun_sound, shoot_message
    global ai_waiting, ai_delay_start, video_playing, current_video_clip, video_start_time

    mouse_pos = pygame.mouse.get_pos()

    # Prevent rapid shooting by adding a cooldown
    current_time = pygame.time.get_ticks()

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
        if user_rect.collidepoint(mouse_pos):
            handle_handsaw_usage("player", "player")
        elif dealer_rect.collidepoint(mouse_pos):
            handle_handsaw_usage("player", "ai")
            handsaw_damage_pending_player = False
            turn = "ai"
            return

    # Player uses the medicine
    elif medicine1_rect.collidepoint(mouse_pos) and not medicine1_used_by_player:
        handle_medicine("player")  # Apply medicine effects
        medicine1_used_by_player = True
        medicine_display_time = pygame.time.get_ticks()
        return

    # Cooldown between shooting actions
    if player_hit_time and current_time - player_hit_time < 500:  # Add a 0.5 second cooldown
        return  # Skip the rest of the logic during cooldown

    # Player shoots themselves
    if user_rect.collidepoint(mouse_pos):
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

    # Player shoots the AI
    elif dealer_rect.collidepoint(mouse_pos):
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

    ai_shoot_message = ""  # Reset AI shoot message

    # AI uses the handsaw and chooses target after video
    if not handsaw2_used_by_ai:
        handsaw2_used_by_ai = True  # Mark handsaw as used
        handsaw_damage_pending_ai = True  # Indicate damage will happen after target selection
        handsaw_sound.play()  # Play the handsaw sound
        video_playing = True  # Set video playing state to true
        current_video_clip = handsawvideo2  # Set the correct video for handsaw
        video_start_time = pygame.time.get_ticks()  # Track the start time of the video
        return  # Exit the function to wait for target selection after the video

    # After handsaw video plays, AI randomly chooses whether to shoot real or fake bullets
    if handsaw_damage_pending_ai:
        bullet_type = random.choice(['real', 'fake'])  # AI randomly selects real or fake bullet

        if bullet_type == 'real' and num_real_bullets > 0:  # AI shoots player with real bullet
            num_real_bullets -= 1
            player_hp -= 2  # Apply -2 HP to Player
            player_hit_time = pygame.time.get_ticks()  # Track player shot time
            player_heart = broken_hearts  # Update player's heart to broken
            gun_sound.play()  # Play gun sound for real bullet
            ai_shoot_message = "AI used handsaw and shot Player with real bullets! Player -2 HP"
            if player_hp <= 0:
                handle_hp_restoration()  # Handle player health restoration if necessary
            check_game_over()  # Check if game is over

        elif bullet_type == 'fake' and num_fake_bullets > 0:  # AI shoots player with fake bullet
            num_fake_bullets -= 1
            emptygun_sound.play()  # Play empty gun sound for fake bullet
            ai_shoot_message = "AI used handsaw and shot Player with fake bullets! Nothing happened."

        handsaw_damage_pending_ai = False  # Reset the handsaw flag
        turn = "player"  # Return to player's turn
        return

    # AI uses the medicine if its health is less than 2 and hasn't used medicine yet
    if ai_hp < 2 and not medicine2_used_by_ai:
        handle_medicine("ai")
        medicine2_used_by_ai = True  # Mark medicine as used
        return  # AI ends its turn after using medicine

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
        check_game_over()  # Check if game over
        turn = "player"  # Change turn to the player
    elif bullet_type == 'fake':
        num_fake_bullets -= 1
        emptygun_sound.play()
        ai_shoot_message = "AI shot you with a fake bullet!"
        turn = "player"  # Change turn to the player

    ai_waiting = False  # Reset AI waiting flag

# Define video playback states
video_playing = False
current_video_clip = None
video_start_time = 0

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
                player_turn()

    # Handle AI turns with delay
    if turn == "ai" and not ai_waiting:
        ai_delay_start = pygame.time.get_ticks()  # Start delay timer
        ai_waiting = True  # Set AI as waiting for delay

    if turn == "ai" and ai_waiting:
        current_time = pygame.time.get_ticks()
        # Check if 3 seconds have passed since AI's turn started
        if current_time - ai_delay_start >= ai_delay_duration:
            ai_turn()  # AI chooses who to shoot again after 3-second delay
            ai_waiting = False  # Reset waiting for the next turn

    # Handle video playback
    if video_playing:
        elapsed_time = pygame.time.get_ticks() - video_start_time
        frame_time = elapsed_time / 1000  # Convert to seconds

        if frame_time < current_video_clip.duration:
            # Display the video frame
            frame = get_frame_as_surface(current_video_clip.get_frame(frame_time))
            frame_rect = frame.get_rect(center=(screen_width // 2, screen_height // 2))
        else:
            # Video has finished
            video_playing = False
            current_video_clip = None

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

    # Render the turn message
    turn_message = f"{'Player' if turn == 'player' else 'AI'}'s Turn"
    turn_surface = font_turn.render(turn_message, True, WHITE)
    screen.blit(turn_surface, (350, 50))

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

    shoot_surface = font.render(shoot_message, True, WHITE)
    screen.blit(shoot_surface, (50, 600))

    ai_shoot_surface = font.render(ai_shoot_message, True, WHITE)
    screen.blit(ai_shoot_surface, (50, 700))

    real_bullets_text = font_12.render(f"Real Bullets: {num_real_bullets}", True, WHITE)
    fake_bullets_text = font_12.render(f"Fake Bullets: {num_fake_bullets}", True, WHITE)
    screen.blit(real_bullets_text, (30, 150))
    screen.blit(fake_bullets_text, (750, 150))

    # Only draw the medicine if it hasn't been used by the player or AI
    if not medicine1_used_by_player:
        screen.blit(medicine1, medicine1_rect)

    if not medicine2_used_by_ai:    
        screen.blit(medicine2, medicine2_rect)

    # Only draw the handsaw if it hasn't been used by the player or AI
    if not handsaw1_used_by_player:
        screen.blit(handsaw1, handsaw1_rect)

    if not handsaw2_used_by_ai:
        screen.blit(handsaw2, handsaw2_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
