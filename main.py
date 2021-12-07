import pygame
from gamefiles.engine import Engine

def main():
    pygame.init()
    pygame.mixer.init()
    mainMenu = True
    
    while (mainMenu):
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Modern Asteroids")
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.screen.blit(self.background, (0, 0))
    
    # initialize scene
    newEngine = Engine()
    # start scene
    newEngine.start()
    
if __name__ == "__main__":
    main()