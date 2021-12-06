import pygame
import sys
from gamefiles.objects.playerClass import Player
from gamefiles.objects.laserClass import Laser

class Scene(object):
    
    # constructor
    def __init__(self):
        # initialize pygame and display
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Modern Asteroids")
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.screen.blit(self.background, (0, 0))
        
        # define sprites and sprites group
        self.laser = Laser()
        self.player = Player()
        self.playerGroup = pygame.sprite.Group(self.player)
        self.laserGroup = pygame.sprite.Group(self.laser)
        
    # starts the main loop
    def start(self):
        self.keepGoing = True
        while self.keepGoing:
            self.mainLoop()
            
    # stops the main loop
    def stop(self):
        self.keepGoing = False
        
    # manages all the main events
    def mainLoop(self):
        self.clock.tick(60)
        self.events()
        self.update()
        self.draw()
        pygame.display.flip()
    
    # manages input events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    if self.laser.canShoot:
                        self.player.fireLaser(self.laser)
                        self.laser.canShoot = False
            
    # updates objects
    def update(self):
        self.playerGroup.clear(self.screen, self.background)
        self.laserGroup.clear(self.screen, self.background)
        self.playerGroup.update(self.screen)
        self.laserGroup.update(self.screen)
    
    # draws screen
    def draw(self):
        self.playerGroup.draw(self.screen)
        self.laserGroup.draw(self.screen)