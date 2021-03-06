import pygame
from settings import *
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('data/asteroid1.png').convert_alpha()
        self.image2 = pygame.image.load('data/asteroid2.png').convert_alpha()
        self.image = random.choice([self.image1, self.image2])
        self.image_copy = self.image

        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        self.rect = self.image.get_rect(center=random.choice([(x, -100), (-100, y)]))

        x = random.choice([random.randint(-4, -1), random.randint(1, 4)])
        y = random.choice([random.randint(-4, -1), random.randint(1, 4)])
        self.direction = pygame.math.Vector2(x, y)

        self.direction = self.direction.normalize()
        self.rotate_value = random.randint(-4, 4)
        self.angle = 0
        self.speed = 4

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
