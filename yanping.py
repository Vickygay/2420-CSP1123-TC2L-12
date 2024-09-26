import turtle
import math
import random
import pygame
import time

pygame.mixer.init() 

move_sound = pygame.mixer.Sound("footsteps.wav")
collision_sound = pygame.mixer.Sound("collision.wav")
pick_sound = pygame.mixer.Sound("pick.wav")


win = turtle.Screen()
win.bgcolor("black")
win.title("A Maze Game")
win.setup(1000,800)
win.tracer(0)

images = ["player_right.gif","player_left.gif","boost.gif","wall.gif",
          "monster_left.gif","monster_right.gif","hearts.gif","exit.gif"]

for image in images:
    turtle.register_shape(image)

legend_turtle = turtle.Turtle()
legend_turtle.penup()
legend_turtle.hideturtle()
legend_turtle.speed(0)

def show_legend():
    start_x = -250 
    start_y = 320  

    legend_turtle.goto(start_x, start_y)
    legend_turtle.shape("boost.gif")
    legend_turtle.stamp()  # Show image
    legend_turtle.goto(start_x, start_y - 30)
    legend_turtle.color("white")
    legend_turtle.write("Boost", align="center", font=("Arial", 12, "normal"))
    
    legend_turtle.goto(start_x + 80, start_y)
    legend_turtle.shape("exit.gif")
    legend_turtle.stamp()  
    legend_turtle.goto(start_x + 80, start_y - 30)
    legend_turtle.write("Exit", align="center", font=("Arial", 12, "normal"))

show_legend()


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
    
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("player_right.gif")
        self.penup()
        self.speed(0)
        self.power = 0
        self.lives = 3
        self.boost_count = 0
        self.last_collision_time = time.time()
        self.exit_prompt_shown = False

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            move_sound.play()
    
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            move_sound.play()

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape("player_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            move_sound.play()

    def go_right(self):
        move_to_x = self.xcor() +24
        move_to_y = self.ycor()
        self.shape("player_right.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            move_sound.play()

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        current_time = time.time()
        if distance < 24 and (current_time - self.last_collision_time > 1.0):
            self.last_collision_time = current_time
            return True
        else:
            return False
    
    def collect_boost(self):
        self.boost_count += 1

            
    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            display_lives() 

            if self.lives == 0:
                time.sleep(2)
                turtle.bye()  # Exit the game when out of lives

class Boost(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("boost.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("monster_left.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up","down","left","right"])
    
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0.
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("monster_left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("monster_right.gif")
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"


        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)             
        else: 
            self.direction = random.choice(["up","down","left","right"])

        turtle.ontimer(self.move, t=random.randint(100,300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt( (a ** 2) + (b ** 2) )

        if distance < 75:
            return True
        else:
            return False

class Exit(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exit.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def reached_exit(self):
        if player.boost_count >= 2:   
            answer = turtle.textinput("Maze Exit", "Do you want to exit the maze? (yes/no)")
            if answer and answer.lower() == "yes":
                print("You chose to exit. Game Over!")
                turtle.bye()
            elif answer and answer.lower() == "no":
                show_continue_message()
                win.update()
                time.sleep(2)
                turtle.bye() 
            else:
                show_error_message()
                win.update()
                time.sleep(2)
                return False
            return True
        else:
            show_cannotexit_message()
            return False


levels = [""]

level_1 = [
"                         ",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXE          XXXX",
"X  XXXXXXX   XXXXX   XXXX",
"X       XX   XXXXX   XXXX",
"X       XX   XXX       XX",
"XXXXXX  XX   XXX      EXX",
"XXXXXX  XX   XXXXX   XXXX",
"XXXXXX         XXXB  XXXX",
"X  XXX     XXXXXXXXXXXXXX",
"X EXXX         XXXXXXXXXX",
"X               XXXXB   X",
"XXXXXXXXX       XXXX    X",
"XXXZXXXXXXXX    XXXX    X",
"XX    XXXXXX            X",
"XXX                     X",
"XXX             XXXXXXXXX",
"XXXXXXXXX       XXXXXXXXX",
"XXXXXXXXXX             XX",   
"XXB   XXXX             XX",
"XX    XXXXXXXXXX       XX",
"XX    XXXXXXXXXX     XXXX",
"XX     XXXXXXXXX     XXXX",
"XX         XXXXX        X",
"XXXE                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]


levels.append(level_1)

pen = Pen()
player = Player()
lives_display  = turtle.Turtle()
lives_display.penup()
lives_display.hideturtle()


walls = []
boosts = []
enemies = []
exit_point = None

def setup_maze(level):
    global exit_point
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "B":
                boosts.append(Boost(screen_x, screen_y))
            
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))
            
            if character == "Z":
                exit_point = (Exit(screen_x, screen_y))

message_turtle = turtle.Turtle()
message_turtle.hideturtle()  # Hide the turtle pointer

def show_continue_message():
    message_turtle.clear()
    message_turtle.penup()
    message_turtle.hideturtle()
    message_turtle.goto(0, 0)
    message_turtle.color("white")
    message_turtle.write("You don't have this choice. Bye!", align="center", font=("Arial", 16, "normal"))
            
def show_error_message():
    message_turtle.clear()
    message_turtle.penup()
    message_turtle.hideturtle()
    message_turtle.goto(0, 0)
    message_turtle.color("white")
    message_turtle.write("Invalid choice. Please try again.", align="center", font=("Arial", 16, "normal"))

def show_cannotexit_message():
    message_turtle.clear()
    message_turtle.penup()
    message_turtle.hideturtle()
    message_turtle.goto(0, 0)
    message_turtle.color("white")
    message_turtle.write("You need at least 2 boosts to exit the maze.", align="center", font=("Arial", 16, "normal"))

    turtle.ontimer(clear_message, 2000)

def clear_message():
    message_turtle.clear()

def display_lives():
    lives_display.clear()
    lives_display.goto(220,290)
    for i in range(player.lives):
        lives_display.shape("hearts.gif")
        lives_display.stamp()
        lives_display.forward(30)


setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

win.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

display_lives()


while True:
    for boost in boosts:
        if player.is_collision(boost):
            pick_sound.play()
            boost.destroy()
            player.collect_boost()
            boosts.remove(boost)
    
    for enemy in enemies:
        if player.is_collision(enemy):
            collision_sound.play()
            player.lose_life() 
            if player.lives == 0:
                break

    if exit_point and player.is_collision(exit_point):
        if exit_point.reached_exit():
            break

    win.update()
