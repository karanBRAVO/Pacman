import pygame
from assets.utils.assets_loader import get_player_images_lists, load_playerImages
from assets.utils import logger


class Player():
    def __init__(self, window, colors: dict, x: int, y: int, width: int, height: int, playerSpeed: int, playerImageDir: str) -> None:
        self.info()
        self.window = window
        self.colors = colors
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = self.createRect(self.x, self.y, self.width, self.height)
        self.directions = {"right": (1, 0),
                           "left": (-1, 0),
                           "down": (0, 1),
                           "up": (0, -1)}
        imageDicts = load_playerImages(playerImageDir, self.width, self.height)
        self.imageLists = get_player_images_lists(
            imageDicts["right"], imageDicts["left"], imageDicts["down"], imageDicts["up"])
        self.playerSpeed = playerSpeed
        self.playerDirection = None
        self.walkCount = 0
        self.playerImgList = self.imageLists["right"]

    def getDirection(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.playerDirection = self.directions["right"]
            self.playerImgList = self.imageLists["right"]
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.playerDirection = self.directions["left"]
            self.playerImgList = self.imageLists["left"]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.playerDirection = self.directions["down"]
            self.playerImgList = self.imageLists["down"]
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.playerDirection = self.directions["up"]
            self.playerImgList = self.imageLists["up"]

    def move(self):
        self.getDirection()

        if self.playerDirection:
            x_velocity = self.playerSpeed * self.playerDirection[0]
            y_velocity = self.playerSpeed * self.playerDirection[1]
            self.updatePosition(x_velocity, y_velocity)
        self.animate(self.playerImgList)

    def updatePosition(self, x: int, y: int):
        self.x += x
        self.y += y
        self.pos.x = self.x
        self.pos.y = self.y

    def drawFace(self):
        self.drawRect()
        self.move()

    def animate(self, imageList: []):
        if self.walkCount >= 18:
            self.walkCount = 0
        self.window.blit(imageList[self.walkCount //
                         3], (self.pos.x, self.pos.y))
        if self.playerDirection:
            self.walkCount += 1

    def drawRect(self):
        pygame.draw.rect(self.window, self.colors["red"], self.pos)

    def createRect(self, x: int, y: int, width: int, height: int):
        return pygame.Rect(x, y, width, height)

    def info(self):
        logger.print_magenta("[*] Use the arrow key or [w|a|s|d] keys")
