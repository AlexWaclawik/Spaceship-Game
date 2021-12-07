import pygame
from gamefiles.utilities.label import Label

class Menu(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Main Menu")
        self.background = pygame.image.load("assets/background/menu.jpg")
        self.background = self.background.convert()
        self.theme = pygame.mixer.Sound("assets/sounds/soundtrack/menutheme.mp3")
        self.theme.set_volume(0.5)
        self.theme.play(loops=-1)
        self.clock = pygame.time.Clock()
        self.screen.blit(self.background, (0, 0))

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
        self.clock.tick(30)
        self.events()
        pygame.display.update()
    
    # manages input events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    self.theme.stop()
                    self.keepGoing = False