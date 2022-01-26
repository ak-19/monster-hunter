import pygame

from colors import Colors
from screen import Screen

class Text:
    def __init__(self, display) -> None:
        self.display = display
        self.main_font = pygame.font.Font('assets/Abrushow.ttf', 42)
        self.sub_font = pygame.font.Font('assets/Abrushow.ttf', 32)
        self.top_panel_font = pygame.font.Font('assets/Abrushow.ttf', 24)

    def game_over(self):
        game_over_text = self.main_font.render('Game over', True, (255, 255, 255), (0, 0, 0))
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (Screen.WIDTH // 2, Screen.HEIGHT // 2)
        self.display.blit(game_over_text, game_over_text_rect)
        
    def top_panel(self, score, lives, round_time, warps):
        pygame.draw.rect(self.display, Colors.WHITE, (1,1,Screen.WIDTH - 2, 100), 2)
        
        score_text = self.top_panel_font.render(f'Score: {score}', True, (255, 255, 255), (0, 0, 0))
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (40, 20)
        self.display.blit(score_text, score_text_rect)

        lives_text = self.top_panel_font.render(f'Lives: {lives}', True, (255, 255, 255), (0, 0, 0))
        lives_text_rect = lives_text.get_rect()
        lives_text_rect.topleft = (40, 60)
        self.display.blit(lives_text, lives_text_rect)    

        round_text = self.top_panel_font.render(f'Round time: {round_time}', True, (255, 255, 255), (0, 0, 0))
        round_text_rect = round_text.get_rect()
        round_text_rect.topleft = (150, 20)
        self.display.blit(round_text, round_text_rect)   


        warp_text = self.top_panel_font.render(f'Warps: {warps}', True, (255, 255, 255), (0, 0, 0))
        warp_text_rect = warp_text.get_rect()
        warp_text_rect.topleft = (150, 60)
        self.display.blit(warp_text, warp_text_rect)                        