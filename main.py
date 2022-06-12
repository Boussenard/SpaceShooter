import pygame
import sys
from settings import *
from ship import Ship
from bullet import Bullet

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Shooter')
        self.clock = pygame.time.Clock()

        self.ship = Ship()

        self.bullet_group = pygame.sprite.Group()

    def run(self):
        while 1 == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bullet_group.add(Bullet(self.ship.sight_vector, self.ship.rect.center))

            self.screen.fill('Black')

            self.ship.update()

            self.bullet_group.update()

            self.screen.blit(self.ship.image, self.ship.rect)

            self.bullet_group.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
