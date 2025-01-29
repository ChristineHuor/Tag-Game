import pygame
from constants import *

class Second(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill((98, 78, 200))  # blue
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = 0
        self.color = 'blue'

    def update(self, keys, obstacles):
        new_rect = self.rect.copy()
        if keys[pygame.K_a]:
            new_rect.x = max(0, self.rect.x - speed)
        if keys[pygame.K_d]:
            new_rect.x = min(SCREEN_WIDTH - cell_size, self.rect.x + speed)
        if keys[pygame.K_w]:
            new_rect.y = max(0, self.rect.y - speed)
        if keys[pygame.K_s]:
            new_rect.y = min(SCREEN_HEIGHT - cell_size, self.rect.y + speed)
        if not any(obstacle.rect.colliderect(new_rect) for obstacle in obstacles):
            self.rect = new_rect