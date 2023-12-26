import pygame
from pygame.locals import *
import sys
from assets import player
from assets.utils import logger, soundPlayer
from assets import layout, score, ghost


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "green": (0, 255, 0),
            "yellow": (255, 255, 0),
            "grey": (192, 192, 192),
            "silver": (188, 198, 204),
            "charcoalBlue": (54, 69, 79),
            "pink": (255, 0, 255),
            "aqua": (0, 255, 255),
            "orange": (255, 165, 0),
        }
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.windowWidth = 750
        self.windowHeight = 350
        self.window = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Pacman")
        pygame.mouse.set_visible(False)  # hide mouse on window
        self.startingImagePath = "./assets/images/bg.png"
        self.startingImage = pygame.image.load(self.startingImagePath)
        self.font = pygame.font.SysFont('monospace', 16, True, False)
        self.run = True
        self.gridWidth = 10
        self.gridHeight = 10
        self.mouse_x = -1
        self.mouse_y = -1
        playerData = {
            "playerStart_x": 430,
            "playerStart_y": 261,
            "playerWidth": 10,
            "playerHeight": 10,
            "playerSpeed": 0.65,
            "imagesDir": "./assets/images/player"
        }
        self.player = player.Player(
            self.window, self.windowWidth, self.windowHeight, self.colors, playerData["playerStart_x"], playerData["playerStart_y"], playerData["playerWidth"], playerData["playerHeight"], playerData["playerSpeed"], playerData["imagesDir"], (220, 45))
        self.gameScore = score.Score(
            self.window, self.colors["red"], 1, (220, 30))
        layoutData = {
            "layoutDir": "./assets/data",
            "fileName": "pacman_world.json"
        }
        self.pacmanWorld = layout.Layout(
            self.window, self.windowWidth, self.windowHeight, self.colors, self.gridWidth, self.gridHeight, layoutData["layoutDir"], layoutData["fileName"])
        self.ghosts = ghost.get_ghosts(
            self.window, self.colors, self.gridWidth, self.gridHeight)
        self.sound_player = soundPlayer.SoundPlayer()

    def drawGrid(self, color):
        for i in range(0, self.windowWidth, self.gridWidth):
            pygame.draw.line(self.window, color, (i, 0),
                             (i, self.windowHeight), 1)
        for j in range(0, self.windowHeight, self.gridHeight):
            pygame.draw.line(self.window, color, (0, j),
                             (self.windowWidth, j), 1)

    def getMousePosition(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def drawMouse(self):
        self.getMousePosition()
        pygame.draw.rect(
            self.window, self.colors["blue"], (self.mouse_x - (self.mouse_x % self.gridWidth), self.mouse_y - (self.mouse_y % self.gridHeight), 10, 10))

    def drawGameWindow(self, layoutStatus: bool):
        if layoutStatus:
            self.window.fill(self.colors["charcoalBlue"])
            self.drawGrid(self.colors["red"])
            self.pacmanWorld.createLayout(self.mouse_x, self.mouse_y)
            self.drawMouse()
        else:
            self.window.fill(self.colors["black"])
            self.pacmanWorld.drawLayout()
            self.pacmanWorld.drawFood()
            self.pacmanWorld.detectPlayerWallCollision(self.player)
            self.player.drawFace()
            self.gameScore.showScore(self.player.pos, self.pacmanWorld.food)
            ghost.drawAllGhosts(
                self.pacmanWorld.adjList, self.pacmanWorld.parent, self.pacmanWorld.visited, self.player, self.ghosts)
            if self.player.checkWin(self.pacmanWorld.food):
                logger.print_green("You won!")
                self.sound_player.playSoundAtChannel(1, 'intermission_sound')
                self.sound_player.takePauseForSomeTime(5_100)
                self.stopGame()
            if self.player.checkLose():
                logger.print_magenta("You Lost!")
                self.sound_player.playSoundAtChannel(1, 'death_sound')
                self.sound_player.takePauseForSomeTime(1_100)
                self.stopGame()
            self.player.showLifeCount()

    def takeLayoutStatus(self):
        logger.print_cyan(f"[?] Do you want to create a new game layout")
        s = input("(yes|no): ")
        return True if s == "yes" else False

    def startGame(self):
        layoutStatus = self.takeLayoutStatus()
        if layoutStatus:
            self.pacmanWorld.info()
        else:
            self.starting()
            self.pacmanWorld.loadLayout()
            self.sound_player.playSoundAtChannel(0, 'siren_sound')

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
            self.drawGameWindow(layoutStatus)
            self.updateDisplay()
            self.clock.tick(self.fps)
        self.stopGame()

    def starting(self):
        self.window.blit(self.startingImage, (0, 0))
        readyMessage = self.font.render("READY!", True, self.colors["red"])
        self.window.blit(readyMessage, (407, 240))
        self.sound_player.playSound('beginning_sound')
        self.sound_player.takePauseForSomeTime(4_500)

    def updateDisplay(self):
        pygame.display.update()

    def stopGame(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    logger.print_cyan("[*] Game is loading ...")
    gameInstance = Game()
    logger.print_green("[*] Game loaded ...")
    gameInstance.startGame()
