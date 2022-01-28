import pygame

from colors import Colors
from screen import Screen

class Text:
    def __init__(self, display) -> None:
        self.display = display
        self.main_font = pygame.font.Font('assets/Abrushow.ttf', 42)
        self.sub_font = pygame.font.Font('assets/Abrushow.ttf', 32)
        self.top_panel_font = pygame.font.Font('assets/Abrushow.ttf', 24)

    def game_over(self, score):
        game_over_text = self.main_font.render('Game over', True, (255, 255, 255), (0, 0, 0))
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (Screen.WIDTH // 2, Screen.HEIGHT // 2)
        self.display.blit(game_over_text, game_over_text_rect)


        play_again_text = self.sub_font.render('Press "p" to play again', True, (255, 255, 255), (0, 0, 0))
        play_again_text_text_rect = play_again_text.get_rect()
        play_again_text_text_rect.center = (Screen.WIDTH // 2, Screen.HEIGHT // 2 + 60)
        self.display.blit(play_again_text, play_again_text_text_rect)

        score_text = self.top_panel_font.render(f'Final score: {score}', True, (255, 255, 255), (0, 0, 0))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (Screen.WIDTH // 2, Screen.HEIGHT // 2 - 60)
        self.display.blit(score_text, score_text_rect)        



    def blit_this_at(self, text, text_param, pos, left_align = True):
        text = self.top_panel_font.render(f'{text} {text_param}', True, (255, 255, 255), (0, 0, 0))
        rect = text.get_rect()
        if left_align: rect.topleft = pos
        else: rect.topright = pos   
        self.display.blit(text, rect)        
        
    def top_panel(self, catch_image, score, lives, round_time, warps, round_number):
        pygame.draw.rect(self.display, Colors.GREEN, (1, Screen.TOP_BORDER, Screen.WIDTH - 2, Screen.BOTTOM_BORDER - Screen.TOP_BORDER), 2)

        
        catch_text = self.top_panel_font.render(f'Current catch: ', True, (255, 255, 255), (0, 0, 0))
        catch_text_rect = catch_text.get_rect()
        catch_text_rect.centerx = Screen.WIDTH // 2
        catch_text_rect.centery = 20
        self.display.blit(catch_text, catch_text_rect)

        catch_image_rect = catch_image.get_rect()
        catch_image_rect.centerx = Screen.WIDTH // 2
        catch_image_rect.centery = 80
        self.display.blit(catch_image, catch_image_rect)

        self.blit_this_at('Score: ', score, (40, 20))
        self.blit_this_at('Lives: ', lives, (40, 60))
        self.blit_this_at('Current round: ', round_number, (40, 100))
        self.blit_this_at('Round time: ', round_time // 60, (Screen.WIDTH - 20, 20), False)
        self.blit_this_at('Warps: ', warps, (Screen.WIDTH - 20, 60), False)
                          