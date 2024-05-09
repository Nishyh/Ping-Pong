from pygame import *
from random import randint
from time import time as timer

font.init()
font = font.Font(None, 36)
won = font.render('YOU WON', True, (255,215,0))
loss = font.render('YOU LOST!', True, (255,0,0))

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption = ('Ping-Pong')
background_image = transform.scale(image.load('background_other.png'), (win_width, win_height))
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

ball = GameSprite('ball.png', 350, 250,5,5, 5)

paddle_right = Player('ok.png', 25, 250, 50, 90, 5)
paddle_left = Player('ok.png', 580, 250, 50, 90, 5)

speed_x = 3
speed_y = 3

while running :
    for e in event.get():
        if e.type == QUIT :
            running = False

    

    if finish == False :
        window.blit(background_image, (0,0))
        paddle_right.update_right()
        paddle_left.update_left()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y -= 1

    
    paddle_left.reset()
    paddle_right.reset()
    ball.reset()

    display.update()
    clock.tick(60)
