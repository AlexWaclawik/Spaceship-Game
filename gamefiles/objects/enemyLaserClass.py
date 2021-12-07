import pygame
import math

# enemy laser class
class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, startx, starty, startDirection, charge):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/lasers/red-laser.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.x = startx
        self.y = starty
        self.direction = startDirection
        self.laserCharge = charge
        self.timer = 60
    
    # update sprite
    def update(self, screen):
        self.move()
        self.calcPos()
        self.checkBounds(screen)
        self.rect.center = (self.x, self.y)
        self.timer -= 1
    
    # move sprite
    def move(self):
        self.x += self.laserCharge * math.cos(self.direction * math.pi / 180)
        self.y += self.laserCharge * math.sin(self.direction * math.pi / 180)
    
    # check if sprite is off screen
    def checkBounds(self, screen):
        if self.x > screen.get_width():
            self.x = 0
        if self.x < 0:
            self.x = 0
        if self.y > screen.get_height():
            self.y = 0
        if self.y < 0:
            self.y = 0