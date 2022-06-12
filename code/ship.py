import pygame
from settings import *


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/space_ship.png').convert_alpha()
        self.image_copy = self.image
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))

        self.angle = 0
        self.sight_vector = pygame.math.Vector2(0.1, 0)
        self.sight_vector_copy = self.sight_vector
        self.direction = pygame.math.Vector2()
        self.moving = False

    def rotate(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.angle -= 2

            self.image = pygame.transform.rotate(self.image_copy, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

            # rotating sight_vector with ship
            self.sight_vector = self.sight_vector_copy.rotate(-self.angle)
            self.sight_vector.normalize()

        elif keys[pygame.K_a]:
            self.angle += 2

            self.image = pygame.transform.rotate(self.image_copy, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

            # rotating sight_vector with ship
            self.sight_vector = self.sight_vector_copy.rotate(-self.angle)
            self.sight_vector.normalize()

    def move(self):
        keys = pygame.key.get_pressed()

        # changing direction if W key is pressed
        if keys[pygame.K_w]:
            self.direction += self.sight_vector
            if self.direction.length() > 10:
                self.direction -= self.sight_vector

            # animation
            self.image_copy = pygame.image.load('data/space_ship_moving.png').convert_alpha()
            self.image = self.image = pygame.transform.rotate(self.image_copy, self.angle)

        else:
            # animation
            self.image_copy = pygame.image.load('data/space_ship.png').convert_alpha()
            self.image = self.image = pygame.transform.rotate(self.image_copy, self.angle)

        self.rect.center += self.direction

        # teleporting ship back if it is out of screen
        if self.rect.centerx > WIDTH:
            self.rect.centerx -= WIDTH

        elif self.rect.centerx < 0:
            self.rect.centerx += WIDTH

        elif self.rect.centery > HEIGHT:
            self.rect.centery -= HEIGHT

        elif self.rect.centery < 0:
            self.rect.centery += HEIGHT

    def update(self):
        self.rotate()
        self.move()
