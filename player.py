import pygame
from global_variables import *

class Player(pygame.sprite.Sprite):
    speed = 0
    jumping = False

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((100, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = SCREEN_HEIGHT

    def update_pos(self, pressed_keys):
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_STEP, 0)

        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_STEP, 0)
        
        if pressed_keys[pygame.K_SPACE]:
            if not(self.jumping):
                self.speed = 1.5 * PLAYER_STEP
                self.jumping = True
        
        self.rect.move_ip(0, -self.speed)
        if(self.speed > -1.5 * PLAYER_STEP):
            self.speed -= 1
        else:
            self.jumping = False

        
        # KEEP PLAYER ON THE SCREEN

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
