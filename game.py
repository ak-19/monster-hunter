from random import randint
import pygame

from hero import Hero
from monster import Monster


class Game:
    def __init__(self, display) -> None:
        self.display = display
        self.run = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.hero_group = pygame.sprite.Group()
        for i in range(10): 
            self.hero_group.add(Hero(100*i, 700))

        self.monster_group = pygame.sprite.Group()
        for i in range(10): 
            self.monster_group.add(Monster(100*i, randint(-120,200)))

    def run_game_loop(self):

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False                    

            self.display.fill((0,0,0))

            self.hero_group.update()
            self.monster_group.update()

            pygame.sprite.groupcollide(self.hero_group, self.monster_group, False, True)
                        
            self.hero_group.draw(self.display)
            self.monster_group.draw(self.display)

            pygame.display.update()
            self.clock.tick(self.fps)