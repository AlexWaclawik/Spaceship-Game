import pygame

class Score():

    def __init__(self, content, color, fontsize, x, y, screen):
        self.text = pygame.font.SysFont("Calibri", fontsize).render(content, True, color)
        self.rect = (x, y)
        screen.blit(self.text, self.rect)