import pygame

from random import randint

from screen import Screen
from sound import Sound

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/hero.png')
        self.rect = self.image.get_rect()
        self.reset_poistion()
        self.sound = Sound()
        self.warps = 2
        self.lives = 5
        self.velocity = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.x - self.velocity >= 0:
                self.rect.x -= self.velocity
        elif keys[pygame.K_RIGHT]:
            if self.rect.x + self.velocity <= Screen.WIDTH - 64:
                self.rect.x += self.velocity
        elif keys[pygame.K_UP]:
            if  self.rect.y - self.velocity >= Screen.TOP_BORDER:
                self.rect.y -= self.velocity
        elif keys[pygame.K_DOWN]:
            if self.rect.y + self.velocity <= Screen.HEIGHT - 64:
                self.rect.y += self.velocity            

    def warp(self):        
        if self.warps > 0:
            self.rect.bottom = Screen.HEIGHT
            self.warps -= 1
            self.sound.warp()

    def reset_poistion(self):
        self.rect.centerx = Screen.WIDTH // 2
        self.rect.bottom = Screen.HEIGHT
