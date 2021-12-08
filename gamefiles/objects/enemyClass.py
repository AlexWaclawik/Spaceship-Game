import pygame
import math
import random

# enemy ship class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/ships/enemy.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.direction = 0
        self.laserDirection = 0
        self.thrust = 4
        #self.charge = 10
        self.status = "Dead"
    
    # update sprite
    def update(self):
        self.move()
        self.checkBounds()
        self.rect.center = (self.x, self.y)
    
    # move sprite
    def move(self):
        self.x += self.thrust * math.cos(self.direction * math.pi / 180)
        #self.y += self.thrust * math.sin(self.direction * math.pi / 180)
    
    # check if sprite is off screen
    def checkBounds(self):
        if self.x >= 1280:
            self.status = "Dead"
        if self.x <= -80:
            self.status = "Dead"
        #if self.y > 800:
            #self.status = "Dead"
        #if self.y < 0:
            #self.status = "Dead"
    
    def spawn(self):
        # set status to alive
        self.status = "Alive"
        # roll for random spawnpoint
        self.x = random.choice((0, 1200))
        self.y = random.randint(50, 750)
        # set movement to the right or left depending on spawn
        if self.x == 0:
            self.direction = 0
        else:
            self.direction = 180