import pygame
from assets.utils.assets_loader import get_player_images_lists, load_playerImages
from assets.utils import logger


class Player():
    def __init__(self, window, windowWidth, windowHeight, colors: dict, x: int, y: int, width: int, height: int, playerSpeed: int, playerImageDir: str, lifePos: tuple = (0, 0)) -> None:
        self.info()
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.colors = colors
        self.resetPosition = (x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = self.createRect(self.x, self.y, self.width, self.height)
        self.wh = 2
        self.right = self.createRect(
            self.pos.right - self.wh, self.y + self.wh, self.wh, self.height - 2 * self.wh)
        self.left = self.createRect(
            self.pos.left, self.y + self.wh, self.wh, self.height - 2 * self.wh)
        self.down = self.createRect(
            self.x + self.wh, self.pos.bottom - self.wh, self.width - 2 * self.wh, self.wh)
        self.up = self.createRect(
            self.x + self.wh, self.y, self.width - 2 * self.wh, self.wh)
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
        self.canMove = {
            "right": True,
            "left": True,
            "down": True,
            "up": True,
        }
        self.font = pygame.font.SysFont('monospace', 11, True, False)
        self.lifeCount = 3
        self.lifePos = lifePos

    def reset(self, resetPosition: tuple = (0, 0)):
        self.x = resetPosition[0]
        self.y = resetPosition[1]
        self.updateRects()
        self.walkCount = 0
        self.playerDirection = None
        self.playerImgList = self.imageLists["right"]

    def showLifeCount(self):
        life = self.font.render(
            f"life: {self.lifeCount}", True, self.colors["blue"])
        self.window.blit(life, self.lifePos)

    def checkLose(self):
        if self.lifeCount == 0:
            return True
        return False

    def checkWin(self, food: dict):
        if not food:
            return True
        return False

    def reduceLifeCount(self):
        self.lifeCount -= 1

    def getDirection(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.canMove["right"]:
            self.playerDirection = self.directions["right"]
            self.playerImgList = self.imageLists["right"]
            self.resetCanMove()
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.canMove["left"]:
            self.playerDirection = self.directions["left"]
            self.playerImgList = self.imageLists["left"]
            self.resetCanMove()
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.canMove["down"]:
            self.playerDirection = self.directions["down"]
            self.playerImgList = self.imageLists["down"]
            self.resetCanMove()
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and self.canMove["up"]:
            self.playerDirection = self.directions["up"]
            self.playerImgList = self.imageLists["up"]
            self.resetCanMove()

    def resetCanMove(self):
        self.canMove["right"] = True
        self.canMove["left"] = True
        self.canMove["down"] = True
        self.canMove["up"] = True

    def moveIn3Directions(self, d1: str, d2: str, d3: str):
        self.canMove[d1] = True
        self.canMove[d2] = True
        self.canMove[d3] = True

    def move(self):
        self.getDirection()

        if self.playerDirection:
            x_velocity = self.playerSpeed * self.playerDirection[0]
            y_velocity = self.playerSpeed * self.playerDirection[1]
            self.updatePosition(x_velocity, y_velocity)
        self.animate(self.playerImgList)
        self.detectGameOffsets()
        self.updateRects()

    def stopMoving(self, direction: str):
        self.playerDirection = None
        self.canMove[direction] = False

    def detectGameOffsets(self):
        def changePos(x: int, y: int):
            self.x = x
            self.y = y

        if self.x + self.width < 0:
            changePos(self.windowWidth, self.y)

        elif self.x > self.windowWidth:
            changePos(0, self.y)

        elif self.y + self.height < 0:
            changePos(self.x, self.windowHeight)

        elif self.y > self.windowHeight:
            changePos(self.x, 0)

    def updatePosition(self, x: int, y: int):
        self.x += x
        self.y += y

    def updateRects(self):
        self.pos.x = self.x
        self.pos.y = self.y
        self.right.x = self.pos.right - self.wh
        self.right.y = self.y + self.wh
        self.left.x = self.pos.left
        self.left.y = self.y + self.wh
        self.down.x = self.x + self.wh
        self.down.y = self.pos.bottom - self.wh
        self.up.x = self.x + self.wh
        self.up.y = self.y

    def drawFace(self):
        # self.drawRect(self.colors["red"], self.pos)
        # self.drawRect(self.colors["red"], self.right)
        # self.drawRect(self.colors["blue"], self.left)
        # self.drawRect(self.colors["green"], self.down)
        # self.drawRect(self.colors["yellow"], self.up)
        self.move()

    def animate(self, imageList: []):
        if self.walkCount >= 18:
            self.walkCount = 0
        self.window.blit(imageList[self.walkCount //
                         3], (self.pos.x, self.pos.y))
        if self.playerDirection:
            self.walkCount += 1

    def drawRect(self, color, pos):
        pygame.draw.rect(self.window, color, pos)

    def createRect(self, x: int, y: int, width: int, height: int):
        return pygame.Rect(x, y, width, height)

    def info(self):
        logger.print_magenta("[*] Use the arrow key or [w|a|s|d] keys")
