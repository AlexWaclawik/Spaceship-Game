import pygame
import sys
import random
from gamefiles.objects.playerClass import Player
from gamefiles.objects.laserClass import Laser
from gamefiles.objects.enemyClass import Enemy
from gamefiles.objects.enemyLaserClass import EnemyLaser
from gamefiles.utilities.label import Label

class Engine(object):
    
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
        # setup player score and player lives
        self.playerScore = 0
        self.scoreDisplay = Label()
        self.scoreDisplay.text = str(self.playerScore)
        self.scoreDisplay.center = (75, 25)
        self.playerLives = "LIVES: 3"
        self.livesDisplay = Label()
        self.livesDisplay.text = self.playerLives
        self.livesDisplay.center = (600, 25)
        self.scoreSprites = pygame.sprite.Group(self.scoreDisplay, self.livesDisplay)
        # define player sprites and player sprite groups
        self.laser = Laser()
        self.player = Player()
        self.playerGroup = pygame.sprite.Group(self.player)
        self.laserGroup = pygame.sprite.Group(self.laser)
        # define enemy sprites and enemy sprite groups
        self.enemyLaser = EnemyLaser()
        self.enemy = Enemy()
        self.enemyGroup = pygame.sprite.Group(self.enemy)
        self.enemyLaserGroup = pygame.sprite.Group(self.enemyLaser)
        
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
        self.checkCollide()
        pygame.display.update()
    
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
        # clear groups
        self.playerGroup.clear(self.screen, self.background)
        self.laserGroup.clear(self.screen, self.background)
        self.enemyGroup.clear(self.screen, self.background)
        self.enemyLaserGroup.clear(self.screen, self.background)
        self.scoreSprites.clear(self.screen, self.background)
        # update groups
        self.playerGroup.update(self.screen)
        self.laserGroup.update(self.screen)
        self.scoreSprites.update()
        # check if enemy is dead, and roll chance to spawn if so
        if self.enemy.status == "Dead":
            if random.randrange(0, 100) == 1:
                self.enemy.spawn()
        else:
            self.enemyGroup.update()
            if self.enemyLaser.timer == 0:
                # create pseudorandom laser fire
                if self.enemy.y < 400:
                    self.enemy.laserDirection = random.randint(30, 150)
                else:
                    self.enemy.laserDirection = random.randint(210, 330)
                self.enemyLaser.firing.play()
                self.enemyLaser.x = self.enemy.x
                self.enemyLaser.y = self.enemy.y
                self.enemyLaser.direction = self.enemy.laserDirection
                self.enemyLaser.timer = 60
            else:
                self.enemyLaserGroup.update(self.screen)
    
    # draws screen
    def draw(self):
        self.playerGroup.draw(self.screen)
        self.laserGroup.draw(self.screen)
        self.enemyGroup.draw(self.screen)
        self.enemyLaserGroup.draw(self.screen)
        self.scoreSprites.draw(self.screen)
        
    # check for sprite collosions
    def checkCollide(self):
        # check if player laser has hit enemy
        if (pygame.sprite.groupcollide(self.enemyGroup, self.laserGroup, False, False)):
            if self.enemy.direction == 180:
                self.enemy.x = 1280
            else:
                self.enemy.x = -80
            self.playerScore += 100
            self.scoreDisplay.text = str(self.playerScore)
        # check if enemy laser has hit player
        #if (pygame.sprite.groupcollide(self.playerGroup, self.enemyLaserGroup, True, False)):'''