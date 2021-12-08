import pygame

class Difficulty(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.selection = 0
        pygame.display.set_caption("Select Difficulty")
        self.background = pygame.image.load("assets/background/select-easy.png")
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
                if event.key == pygame.K_1:
                    self.selection = 1
                    self.background = pygame.image.load("assets/background/select-easy.png")
                    self.background = self.background.convert()
                    self.screen.blit(self.background, (0, 0))
                if event.key == pygame.K_2:
                    self.selection = 2
                    self.background = pygame.image.load("assets/background/select-medium.png")
                    self.background = self.background.convert()
                    self.screen.blit(self.background, (0, 0))
                if event.key == pygame.K_3:
                    self.selection = 3
                    self.background = pygame.image.load("assets/background/select-hard.png")
                    self.background = self.background.convert()
                    self.screen.blit(self.background, (0, 0))
                if event.key == pygame.K_RETURN:
                    self.keepGoing = False