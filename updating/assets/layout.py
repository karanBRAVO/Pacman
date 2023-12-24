import pygame
import json
import sys
from assets.utils import logger


class Layout():
    def __init__(self, window, colors: dict, boxWidth: int, boxHeight: int, layoutDir: str, fileName: str) -> None:
        self.window = window
        self.colors = colors
        self.boxWidth = boxWidth
        self.boxHeight = boxHeight
        self.offset_x = self.boxWidth
        self.offset_y = self.boxHeight
        self.mouse_x = -1
        self.mouse_y = -1
        self.color = self.colors["aqua"]
        self.boxes = {}
        self.layoutDir = layoutDir
        self.fileName = fileName

    def loadLayout(self):
        try:
            with open(f"{self.layoutDir}/{self.fileName}", 'r') as f:
                boxData = json.load(f)
                for key in boxData:
                    color = boxData[key]["color"]
                    x, y = boxData[key]["pos"]
                    box = self.getRect(x, y, self.boxWidth, self.boxHeight)
                    color_box = [color, box]
                    self.boxes[key] = color_box
            f.close()
            logger.print_green(
                f"[+] Layout loaded from {self.layoutDir}/{self.fileName}")
        except Exception as e:
            logger.print_cyan(
                "[-] Unable to load layout from {self.layoutDir}/{self.fileName} | Create a new layout")

    def createLayout(self, mouseX, mouseY):
        keys = pygame.key.get_pressed()
        self.updateMousePositionCoordinates(mouseX, mouseY)

        self.createBoxes(keys)
        self.drawLayout()
        self.saveLayout(keys)

    def saveLayout(self, keys):
        if keys[pygame.K_LALT] and keys[pygame.K_LSHIFT] and keys[pygame.K_l]:
            with open(f"{self.layoutDir}/{self.fileName}", 'w') as f:
                boxData = {}
                for key in self.boxes:
                    color = self.boxes[key][0]
                    box = self.boxes[key][1]
                    boxData[key] = {
                        "color": color, "pos": [box.x, box.y]}
                json.dump(boxData, f)
            f.close()
            logger.print_magenta(
                f"[+] Layout saved to {self.layoutDir}/{self.fileName}")
            pygame.quit()
            sys.exit()

    def drawLayout(self):
        for color_box in list(self.boxes):
            color = self.boxes[color_box][0]
            box = self.boxes[color_box][1]
            self.drawRect(color, box)

    def createBoxes(self, keys):
        self.changePenColor(keys)

        if pygame.mouse.get_pressed(3)[0]:
            x = self.mouse_x - (self.mouse_x % self.offset_x)
            y = self.mouse_y - (self.mouse_y % self.offset_y)
            key = f"box_{x}_{y}"
            if keys[pygame.K_LCTRL]:
                if key in self.boxes:
                    self.boxes.pop(key)
            elif key not in self.boxes:
                box = self.getRect(x, y, self.boxWidth, self.boxHeight)
                color_box = [self.color, box]
                self.boxes[f"box_{x}_{y}"] = color_box

    def changePenColor(self, keys):
        if keys[pygame.K_q]:
            self.color = self.colors['aqua']
        elif keys[pygame.K_y]:
            self.color = self.colors['yellow']
        elif keys[pygame.K_g]:
            self.color = self.colors['green']

    def updateMousePositionCoordinates(self, mouseX, mouseY):
        self.mouse_x = mouseX
        self.mouse_y = mouseY

    def drawRect(self, color, box: pygame.Rect):
        pygame.draw.rect(self.window, color, box)

    def getRect(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)

    def info(self):
        logger.print_yellow("[*] Press Alt + Shift + l to save the layout")
        logger.print_yellow("[*] q -> aqua | y -> yellow | g -> green")