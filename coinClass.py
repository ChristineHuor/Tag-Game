import pygame
from constants import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        self.draw_coin()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_coin(self):
        pygame.draw.circle(self.image, (255, 255, 0), (cell_size // 2, cell_size // 2), cell_size // 2)
        pygame.draw.circle(self.image, (0, 0, 0), (cell_size // 2, cell_size // 2), cell_size // 2, 2)