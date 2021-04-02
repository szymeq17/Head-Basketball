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
sprites = pygame.sprite.Group()
sprites.add(player, ball)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    pressed_keys = pygame.key.get_pressed()
    if pygame.sprite.collide_rect(player, ball):
        ball.collide(player.speed)
    player.update_pos(pressed_keys)
    ball.update_pos()
    screen.blit(player.surf, player.rect)
    screen.blit(ball.surf, ball.rect)
    
    pygame.display.flip()
    clock.tick(30)