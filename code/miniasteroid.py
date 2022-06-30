import pygame
from settings import *
import random


class MiniAsteroid(pygame.sprite.Sprite):
    def __init__(self, num, center):
        super().__init__()
        if num == 1:
            self.image = pygame.image.load('data/asteroidmini1.png').convert_alpha()
        else:
            self.image = pygame.image.load('data/asteroidmini2.png').convert_alpha()
        self.image_copy = self.image
        self.rect = self.image.get_rect(center=center)

        x, y = random.randint(1, 4), random.randint(1, 4)
        self.direction = pygame.math.Vector2(x, y)

        if num == 1:
            self.direction = self.direction.rotate(random.choice([random.randint(20, 70), random.randint(110, 160)]))
        else:
            self.direction = self.direction.rotate(random.choice([random.randint(200, 250), random.randint(290, 340)]))
        self.direction = self.direction.normalize()

        self.rotate_value = random.randint(-4, 4)
        self.angle = 0
        self.speed = 3

    def move(self):
        self.rect.center += self.direction * self.speed

        if self.rect.centerx > WIDTH + 100:
            self.rect.centerx -= WIDTH + 100

        elif self.rect.centerx < -100:
            self.rect.centerx += WIDTH + 200

        elif self.rect.centery > HEIGHT + 100:
            self.rect.centery -= HEIGHT + 200

        elif self.rect.centery < -100:
            self.rect.centery += HEIGHT + 200

    def rotate(self):
        self.angle += self.rotate_value
        self.image = pygame.transform.rotate(self.image_copy, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.move()
        self.rotate()
