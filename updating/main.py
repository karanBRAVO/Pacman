import pygame
from pygame.locals import *
import sys


class Game():
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "green": (0, 255, 0),
            "grey": (192, 192, 192),
            "silver": (188, 198, 204),
            "charcoalBlue": (54, 69, 79),
            "pink": (255, 0, 255),
            "aqua": (0, 255, 255),
        }
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.windowWidth = 750
        self.windowHeight = 350
        self.window = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Pacman")
        self.run = True

    def drawGameWindow(self):
        self.window.fill(self.colors["white"])

    def startGame(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
            self.drawGameWindow()
            self.updateDisplay()
            self.clock.tick(self.fps)
        self.stopGame()

    def updateDisplay(self):
        pygame.display.update()

    def stopGame(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    gameInstance = Game()
    gameInstance.startGame()
