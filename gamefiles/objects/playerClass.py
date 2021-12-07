import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageThrust = pygame.image.load("assets/sprites/ships/ship-1/ship-thrust.png")
        self.imageThrust = self.imageThrust.convert()
        self.imageCruise = pygame.image.load("assets/sprites/ships/ship-1/ship-cruise.png")
        self.imageCruise = self.imageCruise.convert()
        self.imageLeft = pygame.image.load("assets/sprites/ships/ship-1/ship-left.png")
        self.imageLeft = self.imageLeft.convert()
        self.imageRight = pygame.image.load("assets/sprites/ships/ship-1/ship-right.png")
        self.imageRight = self.imageRight.convert()
        self.soundFiring = pygame.mixer.Sound("assets/sounds/effects/player-gun.flac")
        self.soundFiring.set_volume(0.1)
        self.imageMaster = self.imageCruise
        self.image = self.imageMaster
        self.rect = self.image.get_rect()
        
        self.x = 600
        self.y = 400
        self.dx = 0
        self.dy = 0
        self.direction = 0
        self.turnRate = 4
        self.thrust = 0
        self.charge = 25
        
    def update(self, screen):
        self.checkKeys()
        self.rotate()
        self.calcVector()
        self.setPos()
        self.checkBounds(screen)
        self.rect.center = (self.x, self.y)
        
    def checkKeys(self):
        key = pygame.key.get_pressed()
        self.imageMaster = self.imageCruise
        if key[pygame.K_d]:
            self.direction -= self.turnRate
            if self.direction < 0:
                self.direction = 360 - self.turnRate
            self.imageMaster = self.imageRight
        if key[pygame.K_a]:
            self.direction += self.turnRate
            if self.direction > 360:
                self.direction = self.turnRate
            self.imageMaster = self.imageLeft
        if key[pygame.K_w]:
            self.thrust = 0.10
            self.imageMaster = self.imageThrust
        else:
            self.thrust = 0
    
    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imageMaster, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
    
    def calcVector(self):
        radians = self.direction * math.pi / 180
        
        thrustDx = self.thrust * math.cos(radians)
        thrustDy = self.thrust * math.sin(radians)
        thrustDy *= -1
        
        self.dx += thrustDx
        self.dy += thrustDy
        self.speed = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))
    
    def setPos(self):
        self.x += self.dx
        self.y += self.dy
    
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
        laser.x = self.rect.centerx
        laser.y = self.rect.centery
        laser.speed = self.charge
        laser.direction = self.direction
        self.soundFiring.play()