import pygame

class Label(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Calibri", 48)
        self.text = ""
        self.fgColor = ((0xFF, 0xFF, 0xFF))
        self.bgColor = ((0x00, 0x00, 0x00))
        self.center = (100, 100)
        self.size = (150, 50)
    
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        xPos = (self.image.get_width() - fontSurface.get_width()) / 2
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center