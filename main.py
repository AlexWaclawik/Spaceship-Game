import pygame
from gamefiles.menu.mainMenu import Menu
from gamefiles.menu.chooseDiff import Difficulty
from gamefiles.engine import Engine

difficulty = 1

def splashScreen():
    mainMenu = Menu()
    mainMenu.start()
    
def chooseDifficulty():
    diffMenu = Difficulty()
    diffMenu.start()
    difficulty = diffMenu.selection

def startGame():
    newEngine = Engine(difficulty)
    newEngine.start()

def main():
    pygame.init()
    pygame.mixer.init()
    theme = pygame.mixer.Sound("assets/sounds/soundtrack/menutheme.mp3")
    theme.set_volume(0.5)
    theme.play(loops=-1)
    splashScreen()
    chooseDifficulty()
    keepGoing = True
    while keepGoing:
        theme.stop()
        startGame()
    
if __name__ == "__main__":
    main()