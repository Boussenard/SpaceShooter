import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, vector, center):
        super().__init__()
        self.image = pygame.surface.Surface((2, 2))
        self.image.fill('White')
        self.rect = self.image.get_rect(center=center)
        self.direction = vector * 100

    def death(self):
        if self.rect.centerx > WIDTH or self.rect.centerx < 0 or self.rect.centery > HEIGHT or self.rect.centery < 0:
            self.kill()

    def update(self):
        self.rect.center += self.direction
        self.death()
