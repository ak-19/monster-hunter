import pygame
from random import randint
from monster import Monster, MonsterType

from text import Text
from player import Player
from sound import Sound
from colors import Colors
from screen import Screen

class Game:
    def __init__(self, display) -> None:
        self.display = display
        self.run = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.sound = Sound()
        self.text = Text(display)

        self.make_player()
        self.make_monsters()


        self.score = 0
        self.round_number = 0
        self.round_time = 0
        self.frame_count = 0
        

    def make_monsters(self):
        self.monster_group = pygame.sprite.Group()
        self.monster_group.add(Monster(100*1, randint(0,200), MonsterType.Orange))
        self.monster_group.add(Monster(100*1, randint(0,200), MonsterType.Green))
        self.monster_group.add(Monster(100*5, randint(0,300), MonsterType.Blue))
        self.monster_group.add(Monster(100*5, randint(0,300), MonsterType.Purple))

    def make_player(self):
        self.player_group = pygame.sprite.Group()
        self.player_group.add(Player())        

    def update(self):
        self.player_group.update()
        self.monster_group.update()
        pygame.sprite.groupcollide(self.player_group, self.monster_group, False, True)

    def draw(self):
        self.display.fill(Colors.BLACK)
        self.player_group.draw(self.display)
        self.monster_group.draw(self.display)        
        pygame.display.update()

    def start_new_round(self):
        pass

    def check_collisions(self):
        pass

    def choose_new_target(self):
        pass    

    def run_game_loop(self):

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False                    

            self.update()
                        
            self.draw()
            
            self.clock.tick(self.fps)