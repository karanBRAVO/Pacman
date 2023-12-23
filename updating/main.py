import pygame
from pygame.locals import *
import sys
from assets import player
from assets.utils import logger


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
        playerData = {
            "playerStart_x": 10,
            "playerStart_y": 10,
            "playerWidth": 18,
            "playerHeight": 18,
            "playerSpeed": 1,
            "imagesDir": "./assets/images/player"
        }
        self.player = player.Player(
            self.window, self.colors, playerData["playerStart_x"], playerData["playerStart_y"], playerData["playerWidth"], playerData["playerHeight"], playerData["playerSpeed"], playerData["imagesDir"])

    def drawGrid(self, step: int, color):
        for i in range(0, self.windowWidth, step):
            pygame.draw.line(self.window, color, (i, 0),
                             (i, self.windowHeight), 1)
        for j in range(0, self.windowHeight, step):
            pygame.draw.line(self.window, color, (0, j),
                             (self.windowWidth, j), 1)

    def drawGameWindow(self):
        self.window.fill(self.colors["black"])
        self.drawGrid(10, self.colors["pink"])
        self.player.drawFace()

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
    logger.print_cyan("[*] Pacman is starting ...")
    gameInstance = Game()
    logger.print_green("[*] Pacman started ...")
    gameInstance.startGame()
