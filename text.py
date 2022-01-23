from screen import Screen
import pygame


class Text:
    def __init__(self, display) -> None:
        self.display = display
        self.main_font = pygame.font.Font('assets/Abrushow.ttf', 42)
        self.sub_font = pygame.font.Font('assets/Abrushow.ttf', 32)

    def game_over(self):
        game_over_text = self.main_font.render('Game over', True, (255, 255, 255), (0, 0, 0))
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (Screen.WIDTH // 2, Screen.HEIGHT // 2)
        self.display.blit(game_over_text, game_over_text_rect)
        