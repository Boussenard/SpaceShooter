import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, vector, center):
        super().__init__()
        self.image = pygame.surface.Surface((2, 2))
        self.image.fill('White')
        self.rect = self.image.get_rect(center=center)
        self.direction = vector * 200
        self.teleports = 0

    def death(self):
        if self.teleports > 1:
            self.kill()

    def move(self):
        self.rect.center += self.direction

        if self.rect.centerx > WIDTH:
            self.rect.centerx -= WIDTH
            self.teleports += 1

        elif self.rect.centerx < 0:
            self.rect.centerx += WIDTH
            self.teleports += 1

        elif self.rect.centery > HEIGHT:
            self.rect.centery -= HEIGHT
            self.teleports += 1

        elif self.rect.centery < 0:
            self.rect.centery += HEIGHT
            self.teleports += 1

    def update(self):
        self.move()
        self.death()
