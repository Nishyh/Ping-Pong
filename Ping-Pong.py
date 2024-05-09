from pygame import *
from random import randint

font.init()
font = font.Font(None, 36)
loss1 = font.render('YOU LOST! PLAYER 1', True, (255,215,0))
loss2 = font.render('YOU LOST! PLAYER 2', True, (255,0,0))

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption = ('Ping-Pong')
background_image = transform.scale(image.load('volley_court.webp'), (win_width, win_height))
clock = time.Clock()
running = True 
finish = False


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80,80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_p] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_l] and self.rect.y < win_width - 80:
            self.rect.y += self.speed   

speed_x = 3
speed_y = 3


class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y

        if self.rect.y > win_height-50 or self.rect.y < 0:
            speed_y *= -1


ball = Ball('ball.png', 350, 250,5,5, 5)

paddle_right = Player('shoyo.png', 25, 250, 70, 90, 5)
paddle_left = Player('tsukushima.png', 580, 250, 70, 90, 5)

# Countdown timer variables
countdown_seconds = 10

# Function to display countdown
def display_countdown(countdown):
    countdown_text = font.render("Game starts in: " + str(countdown), True, (0,0,0))
    window.blit(countdown_text, (win_width // 2 - countdown_text.get_width() // 2, win_height // 2 - countdown_text.get_height() // 2))

# Create a clock object to control the frame rate
clock = time.Clock()

white = (255,255,255)
# Countdown loop
for i in range(countdown_seconds, 0, -1):
    window.fill(white)
    display_countdown(i)
    display.flip()
    time.wait(1000)  # Wait for 1 second

while running :
    for e in event.get():
        if e.type == QUIT :
            running = False


    if finish == False :
        window.blit(background_image, (0,0))
        paddle_right.update_right()
        paddle_left.update_left()
        ball.update()

    if sprite.collide_rect(paddle_right, ball) or sprite.collide_rect(paddle_left, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        window.blit(loss1, (350,250))
    if ball.rect.x > 750:
        window.blit(loss2, (350,250))

    paddle_left.reset()
    paddle_right.reset()
    ball.reset()


    display.update()
    clock.tick(60)

