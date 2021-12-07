import pygame
import math

# enemy laser class
class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.firing = pygame.mixer.Sound("assets/sounds/effects/enemy-laser-1.ogg")
        self.firing.set_volume(0.1)
        self.image = pygame.image.load("assets/sprites/lasers/red-laser.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.direction = 0
        self.laserCharge = 10
        self.timer = 60
    
    # update sprite
    def update(self, screen):
        self.move()
        #self.calcPos()
        #self.checkBounds(screen)
        self.rect.center = (self.x, self.y)
        self.timer -= 1
    
    # move sprite
    def move(self):
        self.x += self.laserCharge * math.cos(self.direction * math.pi / 180)
        self.y += self.laserCharge * math.sin(self.direction * math.pi / 180)