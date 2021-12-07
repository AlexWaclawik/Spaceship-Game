import pygame
from gamefiles.menu.mainMenu import Menu
from gamefiles.engine import Engine

def gotoMenu():
    mainMenu = Menu()
    mainMenu.start()

def startGame():
    newEngine = Engine()
    newEngine.start()

def main():
    pygame.init()
    gotoMenu()
    keepGoing = True
    while keepGoing:
        startGame()
    
if __name__ == "__main__":
    main()