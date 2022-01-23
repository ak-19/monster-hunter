
from random import randint
import pygame

class Monster(pygame.sprite.Sprite):
    def update(self):
        self.y += randint(0, 5)
        self.rect.topleft = (self.x, self.y)