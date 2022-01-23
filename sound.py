import pygame


class Sound:
    def __init__(self) -> None:
        self.catch_sound  = pygame.mixer.Sound('assets/catch.wav')
        self.warp_sound  = pygame.mixer.Sound('assets/warp.wav')
        self.next_level_sound  = pygame.mixer.Sound('assets/next_level.wav')
        self.die_sound  = pygame.mixer.Sound('assets/next_level.wav')

    def warp(self):
        self.warp_sound.play()

    def catch(self):
        self.catch_sound.set_volume(.1)
        self.catch_sound.play()        

    def die(self):
        self.die_sound.play()                

    def next_level(self):
        self.next_level_sound.play()                        