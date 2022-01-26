
from enum import Enum
from random import choice, randint
import pygame

from screen import Screen

class MonsterType():
    Green = 0
    Orange = 1
    Blue = 2
    Purple = 3

class MonsterTypeImage():
    def __init__(self) -> None:
        self.images = [pygame.image.load('assets/green_monster.png'), pygame.image.load('assets/orange_monster.png'), pygame.image.load('assets/blue_monster.png'), pygame.image.load('assets/purple_monster.png')]        

    def get_image(self, monster_type: MonsterType):
        return self.images[monster_type]

    def get_random_type(self):
        return randint(0,3)

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, monsterTypeImage: MonsterTypeImage) -> None:
        super().__init__()    
        monster_type = monsterTypeImage.get_random_type()
        self.image = monsterTypeImage.get_image(monster_type)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)     

        self.type = monster_type

        self.dx = choice([-1,1])
        self.dy = choice([-1,1])
        self.velocity = randint(1, 5)

    def update(self):
        self.rect.y += self.velocity * self.dy
        self.rect.x += self.velocity * self.dx

        if self.rect.y + self.velocity * self.dy + 64 >= Screen.BOTTOM_BORDER or self.rect.y + self.velocity * self.dy <= Screen.TOP_BORDER:
            self.dy *= -1

        if self.rect.x + self.velocity * self.dx + 64 >= Screen.WIDTH or self.rect.x + self.velocity * self.dx <= 0:
            self.dx *= -1
