
from random import randint
import pygame

from screen import Screen
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/monster.png')
        self.rect = self.image.get_rect()
        self.x, self.y = randint(0, Screen.WIDTH - 64), randint(0, Screen.HEIGHT - 64)
        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.x, self.y = randint(0, Screen.WIDTH - 64), randint(0, Screen.HEIGHT - 64)
        self.rect.topleft = (self.x, self.y)