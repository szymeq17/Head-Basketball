import pygame
from global_variables import *

class Ball(pygame.sprite.Sprite):
    x_acc = 0
    y_acc = GRAVITY
    on_ground = False
    def __init__(self):
        super(Ball, self).__init__()

        self.surf = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        pygame.draw.circle(self.surf, (255, 161, 0), (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)

    def update_pos(self):
        if not(self.on_ground):
            self.rect.move_ip(self.x_acc, -self.y_acc)
            self.y_acc -= 1

        
        # if(self.x_acc > 0):
        #     self.x_acc -= 1
        # elif(self.x_acc < 0):
        #     self.x_acc +- 1
        # KEEP BALL ON THE SCREEN

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # if self.rect.top <= 0:
        #     self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            if(abs(self.y_acc) < 5):
                self.rect.bottom = SCREEN_HEIGHT
                self.on_ground = True
            else:
                self.y_acc = -self.y_acc / 1.5

    def collide(self, player_speed):
        print(self.y_acc)
        self.y_acc = -self.y_acc / 1.5
        self.y_acc += player_speed
        self.rect.move_ip(self.x_acc, -self.y_acc)
        self.y_acc -= 1