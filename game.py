import sys, pygame
from player import Player
from ball import Ball
from global_variables import *


pygame.init()
clock = pygame.time.Clock()

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()
ball = Ball()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    pressed_keys = pygame.key.get_pressed()
    player.update_pos(pressed_keys)
    ball.update_pos()
    screen.blit(player.surf, player.rect)
    screen.blit(ball.surf, ball.rect)
    if(ball.on_ground):
        sys.exit()
    

    
    pygame.display.flip()
    clock.tick(30)