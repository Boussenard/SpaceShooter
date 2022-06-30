import pygame
import sys
from settings import *
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid
from miniasteroid import MiniAsteroid
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Shooter')
        self.clock = pygame.time.Clock()
        self.menu_is_on = True

        self.ship = Ship()
        self.menu = Menu()

        self.bullet_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.mini_asteroid_group = pygame.sprite.Group()

    def run(self):
        while 1 == 1:
            if self.menu_is_on:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.menu_is_on = False
                            self.asteroid_group.empty()

                self.screen.fill('Black')

                if self.asteroid_group.__len__() < 7:
                    for i in range(9):
                        self.asteroid_group.add(Asteroid())

                self.asteroid_group.update()
                self.asteroid_group.draw(self.screen)
                self.menu.draw(self.screen)

                pygame.display.update()
                self.clock.tick(FPS)

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.bullet_group.add(Bullet(self.ship.sight_vector, self.ship.rect.center))

                self.screen.fill('Black')

                # splitting big asteroid into 2 mini asteroids
                for sprite in self.asteroid_group:
                    if pygame.sprite.spritecollide(sprite, self.bullet_group, True):
                        self.mini_asteroid_group.add(MiniAsteroid(1, sprite.rect.center),
                                                     MiniAsteroid(2, sprite.rect.center))
                        sprite.kill()

                self.ship.update()
                self.bullet_group.update()
                self.asteroid_group.update()
                self.mini_asteroid_group.update()
                pygame.sprite.groupcollide(self.mini_asteroid_group, self.bullet_group, True, True)

                self.screen.blit(self.ship.image, self.ship.rect)
                self.bullet_group.draw(self.screen)
                self.asteroid_group.draw(self.screen)
                self.mini_asteroid_group.draw(self.screen)

                # spawning asteroids
                if self.asteroid_group.__len__() < 7 and self.mini_asteroid_group.__len__() < 14:
                    for i in range(7-self.asteroid_group.__len__()):
                        self.asteroid_group.add(Asteroid())

                pygame.display.update()
                self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
