import pygame


class Menu:
    def __init__(self):
        self.font = pygame.font.Font(pygame.font.get_default_font(), 100)

        self.message = self.font.render('Test', False, 'White')

    def draw(self, screen):
        screen.blit(self.message, (100, 100))
