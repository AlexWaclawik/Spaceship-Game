import pygame
import math
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/ships/enemy.png")
        self.image = self.image.convert()
        self.soundPrimaryFiring = pygame.mixer.Sound("assets/sounds/effects/enemy-laser-1.ogg")
        self.soundPrimaryFiring.set_volume(0.1)
        #self.soundSecondaryFiring = pygame.mixer.Sound("assets/sounds/effects/enemy-laser-1.ogg")
        #self.soundSecondaryFiring.set_volume(0.1)
        self.rect = self.image.get_rect()
        
        self.x = -100
        self.y = -100
        #self.dx = 0
        #self.dy = 0
        self.direction = 0
        self.thrust = 5
        self.charge = 10
        self.status = "Dead"
        
    def spawn(self):
        # set status to alive
        self.status = "Alive"
        # roll for random spawnpoint
        self.x = random.choice((0, 1200))
        self.y = random.randint(0, 800)
        # set movement to the right or left depending on spawn
        if self.x == 0:
            self.direction = 0
        else:
            self.direction = 180
        
    def update(self, screen):
        if self.status == "Alive":
            self.move()
            self.checkBounds(screen)
            self.rect.center = (self.x, self.y)
    
    def move(self):
        '''radians = self.direction * math.pi / 180
        thrustDx = self.thrust * math.cos(radians)
        thrustDy = self.thrust * math.sin(radians)
        thrustDy *= -1
        self.dx += thrustDx
        self.dy += thrustDy
        self.speed = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))'''
        
        self.x += self.thrust * math.cos(self.direction * math.pi / 180)
        self.y += self.thrust * math.sin(self.direction * math.pi / 180)
    
    def checkBounds(self, screen):
        if self.x > screen.get_width():
            self.x = 0
        if self.x < 0:
            self.x = screen.get_width()
        if self.y > screen.get_height():
            self.y = 0
        if self.y < 0:
            self.y = screen.get_height()
            
    def fireLaser(self, laser):
        self.laserDirection = random.randint(0, 360)
        laser.x = self.rect.centerx
        laser.y = self.rect.centery
        laser.speed = self.charge
        laser.direction = self.laserDirection
        self.soundPrimaryFiring.play()
        
    def reset(self):
        self.x = -100
        self.y = -100
        #self.dx = 0
        #self.dy = 0
        self.direction = 0
        self.speed = 0