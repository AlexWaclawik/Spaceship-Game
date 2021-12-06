import pygame
import math

class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/lasers/red-laser.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.speed = 0
        self.direction = 0
        self.reset()
        self.canShoot = True
        
    def update(self, screen):
        self.calcVector()
        self.calcPos()
        self.checkBounds(screen)
        self.rect.center = (self.x, self.y)
        
    def calcVector(self):
        radians = self.direction * math.pi / 180
        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1
        
    def calcPos(self):
        self.x += self.dx
        self.y += self.dy
        
    def checkBounds(self, screen):
        if self.x > screen.get_width():
            self.reset()
        if self.x < 0:
            self.reset()
        if self.y > screen.get_height():
            self.reset()
        if self.y < 0:
            self.reset()
            
    def reset(self):
        self.x = -100
        self.y = -100
        self.speed = 0
        self.canShoot = True
        