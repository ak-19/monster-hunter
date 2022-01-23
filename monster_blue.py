import pygame
from monster import Monster


class MonsterBlue(Monster):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/blue_monster.png')
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)    