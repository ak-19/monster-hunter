import pygame
from random import choice, randint
from monster import Monster, MonsterType, MonsterTypeImage

from text import Text
from player import Player
from sound import Sound
from colors import Colors
from screen import Screen

class Game:
    def __init__(self, display) -> None:
        self.display = display
        self.run = True
        self.pause = False
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.sound = Sound()
        self.text = Text(display)
        self.monsterTypeImage = MonsterTypeImage()   

        self.start_new_game()

    def make_monsters(self):
        self.monster_group = pygame.sprite.Group()
        self.monster_group.add(Monster(100*1, randint(Screen.TOP_BORDER, Screen.BOTTOM_BORDER - Screen.TOP_BORDER), self.monsterTypeImage, MonsterType.Green))
        self.monster_group.add(Monster(100*1, randint(Screen.TOP_BORDER, Screen.BOTTOM_BORDER - Screen.TOP_BORDER), self.monsterTypeImage, MonsterType.Blue))
        self.monster_group.add(Monster(100*5, randint(Screen.TOP_BORDER, Screen.BOTTOM_BORDER - Screen.TOP_BORDER), self.monsterTypeImage, MonsterType.Purple))
        self.monster_group.add(Monster(100*5, randint(Screen.TOP_BORDER, Screen.BOTTOM_BORDER - Screen.TOP_BORDER), self.monsterTypeImage, MonsterType.Orange))

    def make_player(self):
        self.player = Player()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)        

    def update(self):
        self.player_group.update()
        self.monster_group.update()
        self.round_time += 1
        self.check_collisions()
                
    def draw(self):
        self.display.fill(Colors.BLACK)

        self.text.top_panel(self.monsterTypeImage.get_image(self.curr_catch), 
                            self.score, 
                            self.player.lives, 
                            self.round_time, 
                            self.player.warps, 
                            self.round_number )

        self.player_group.draw(self.display)
        self.monster_group.draw(self.display)        
        pygame.display.update()

    def start_new_game(self):
        self.make_player()
        self.make_monsters()
        self.score = 0
        self.round_number = 1
        self.round_time = 0
        self.curr_catch = self.monsterTypeImage.get_random_type()

    def start_new_round(self):
        self.round_number += 1
        self.round_time = 0        
        self.curr_catch = self.monsterTypeImage.get_random_type()
        self.player.reset_poistion()
        self.make_monsters()

    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.curr_catch:
                self.sound.catch()
                self.score += 1

                if len(self.monster_group) == 1:
                    self.start_new_round()
                else:
                    self.player.reset_poistion()  
                    self.choose_new_target()     
            else:
                self.player.lives -= 1
                self.sound.die()
                self.player.reset_poistion()                
                if self.player.lives == 0:
                    self.pause = True                   


    def choose_new_target(self):
        for  monster in self.monster_group:
            if monster.type == self.curr_catch:
                self.monster_group.remove(monster)
                break
        self.curr_catch = self.monster_group.sprites()[-1].type

    def run_game_loop(self):

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False    
                elif event.type == pygame.KEYDOWN and self.pause and event.key == pygame.K_p:
                    self.pause = False
                    self.start_new_game()                         

            if not self.pause:
                self.update()                        
                self.draw()
            
            self.clock.tick(self.fps)