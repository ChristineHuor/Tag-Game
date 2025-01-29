import pygame
from constants import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, r, g, b, mult, multi):
        super().__init__()
        self.image = pygame.Surface((cell_size * mult, cell_size * multi))
        self.image.fill((r, g, b))  # Black color for the obstacle
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y