import pygame

from screen import Screen

class Setup:
    def __init__(self) -> None:
        pygame.init()

    def get_display(self):
        pygame.display.set_caption('Monster Hunter')
        return pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

    def quit(self):
        pygame.quit()
