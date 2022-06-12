import pygame
from settings import *
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('data/asteroid1.png').convert_alpha()
        self.image2 = pygame.image.load('data/asteroid2.png').convert_alpha()
        self.image = random.choice([self.image1, self.image2])

        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        self.rect = self.image.get_rect(center=random.choice([(x, 0), (0, y)]))

        x = random.randint(1, 4)
        y = random.randint(1, 4)
        self.direction = pygame.math.Vector2(x, y)
        self.direction.rotate(random.choice([random.randint(20, 70), random.randint(110, 160), random.randint(200, 250),
                                             random.randint(290, 340)]))
        self.direction.magnitude()

    def move(self):
        self.rect.center += self.direction

        if self.rect.centerx > WIDTH:
            self.rect.centerx -= WIDTH

        elif self.rect.centerx < 0:
            self.rect.centerx += WIDTH

        elif self.rect.centery > HEIGHT:
            self.rect.centery -= HEIGHT

        elif self.rect.centery < 0:
            self.rect.centery += HEIGHT

    def update(self):
        self.move()


