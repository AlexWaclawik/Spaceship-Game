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
        self.charge = 10
        self.status = "Dead"
    
    # update sprite
    def update(self, screen):
        self.move()
        self.checkBounds(screen)
        self.rect.center = (self.x, self.y)
    
    # move sprite
    def move(self):
        self.x += self.thrust * math.cos(self.direction * math.pi / 180)
        self.y += self.thrust * math.sin(self.direction * math.pi / 180)
    
    # check if sprite is off screen
    def checkBounds(self, screen):
        if self.x > screen.get_width():
            self.status = "Dead"
        if self.x < 0:
            self.status = "Dead"
        if self.y > screen.get_height():
            self.status = "Dead"
        if self.y < 0:
            self.status = "Dead"
    
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
        # roll for laser direction based on the starting position
        if self.y < 400:
            self.laserDirection = random.randint(210, 330)
        else:
            self.laserDirection = random.randint(30, 150)
        # reset laser timer
        self.laserTimer = 0