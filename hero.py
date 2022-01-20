from screen import Screen
import pygame
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/hero.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x - self.velocity >= 0:
                self.x -= self.velocity
        elif keys[pygame.K_RIGHT]:
            if self.x + self.velocity <= Screen.WIDTH - 64:
                self.x += self.velocity
        elif keys[pygame.K_UP]:
            if  self.y - self.velocity >= 0:
                self.y -= self.velocity
        elif keys[pygame.K_DOWN]:
            if self.y + self.velocity <= Screen.HEIGHT - 64:
                self.y += self.velocity            

        self.rect.topleft = (self.x, self.y)


