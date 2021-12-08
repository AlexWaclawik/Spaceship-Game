import pygame

class Menu(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Splash Screen")
        self.background = pygame.image.load("assets/background/splashscreen.png")
        self.background = self.background.convert()
        self.clock = pygame.time.Clock()
        self.screen.blit(self.background, (0, 0))

    # starts the main loop
    def start(self):
        self.keepGoing = True
        while self.keepGoing:
            self.mainLoop()
        
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
                    self.keepGoing = False