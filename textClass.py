import pygame
from constants import *

class Text:
    def __init__(self, content, x, y, r, g, b, font_size = cell_size):
        self.content = content
        self.font = pygame.font.Font(None, font_size)
        self.rendered_text = self.font.render(self.content, True, (r, g, b))
        self.rect = self.rendered_text.get_rect(topleft = (x, y))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        surface.blit(self.rendered_text, self.rect)