
from enum import Enum
from random import choice, randint
import pygame

from screen import Screen

class MonsterType(Enum):
    Green = 1
    Purple = 2
    Blue = 3

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, image, monster_type: MonsterType) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)     

        self.type = monster_type

        self.dx = choice([-1,1])
        self.dy = choice([-1,1])
        self.velocity = randint(1, 5)

    def update(self):
        if self.rect.y + self.velocity * self.dy + 64 > Screen.HEIGHT or self.rect.y + self.velocity * self.dy < 0:
            self.dy *= -1

        if self.rect.x + self.velocity * self.dx + 64 > Screen.WIDTH or self.rect.x + self.velocity * self.dx < 0:
            self.dx *= -1

        self.rect.y += self.velocity * self.dy
        self.rect.x += self.velocity * self.dx