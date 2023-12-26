import pygame
from assets.utils.assets_loader import load_ghostImages
from assets.utils.soundPlayer import SoundPlayer
from queue import Queue
import re


def get_ghosts(window, colors: dict, gridWidth: int, gridHeight: int, speeds: list = [0.25, 0.5, 0.25, 0.5]):
    ghostData = {
        "width": 10,
        "height": 10,
        "imagesDir": "./assets/images/ghosts",
    }
    ghosts = {
        "red": Ghost(window, colors, gridWidth, gridHeight, 430, 200, ghostData['width'], ghostData['height'], ghostData['imagesDir'], "red", speeds[0]),
        "blue": Ghost(window, colors, gridWidth, gridHeight, 420, 150, ghostData['width'], ghostData['height'], ghostData['imagesDir'], "blue", speeds[1]),
        "orange": Ghost(window, colors, gridWidth, gridHeight, 450, 230, ghostData['width'], ghostData['height'], ghostData['imagesDir'], "orange", speeds[2]),
        "pink": Ghost(window, colors, gridWidth, gridHeight, 410, 240, ghostData['width'], ghostData['height'], ghostData['imagesDir'], "pink", speeds[3]),
    }
    return ghosts


def drawAllGhosts(adjList: dict, parent: dict, visited: dict, player, ghosts: dict):
    for ghost in ghosts:
        ghosts[ghost].drawGhost(adjList, parent, visited, player, ghosts)


class Ghost():
    def __init__(self, window, colors: dict, gridWidth: int, gridHeight: int, x: int, y: int, width: int, height: int, ghostImagesDir: str, face: str = "red" or "blue" or "orange" or "pink", ghostSpeed: float = 0.0) -> None:
        self.window = window
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.colors = colors
        self.resetPosition = (x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.face = face
        self.pos = self.createRect(self.x, self.y, self.width, self.height)
        self.speed = ghostSpeed
        self.images = load_ghostImages(
            ghostImagesDir, self.width, self.height)[self.face]
        self.directions = {
            "right": (1, 0), "left": (-1, 0), "down": (0, 1), "up": (0, -1)}
        self.current_direction = None
        self.q = Queue(-1)
        self.task = []
        self.faceDirection = "right"
        self.sound_player = SoundPlayer()

    def reset(self, resetPosition: tuple = (0, 0)):
        self.faceDirection = "right"
        self.task.clear()
        self.current_direction = None
        self.x = resetPosition[0]
        self.y = resetPosition[1]
        self.pos.x = self.x
        self.pos.y = self.y

    def createTask(self, Parent: dict, start: str, end: str):
        while end and end != start:
            if end not in Parent:
                curr_node = self.getNode(end)
                rightNode = f"box_{curr_node[0] + self.gridWidth}_{curr_node[1]}"
                leftNode = f"box_{curr_node[0] - self.gridWidth}_{curr_node[1]}"
                downNode = f"box_{curr_node[0]}_{curr_node[1] + self.gridHeight}"
                upNode = f"box_{curr_node[0]}_{curr_node[1] - self.gridHeight}"
                if rightNode in Parent:
                    end = rightNode
                elif leftNode in Parent:
                    end = leftNode
                elif downNode in Parent:
                    end = downNode
                elif upNode in Parent:
                    end = upNode
            self.task = [end] + self.task
            end = Parent[end] if end in Parent else None

    def findParentsAndCreateTask(self, adjList: dict, parent: dict, visited: dict, startNode: str, endNode: str):
        # mark all not visited
        for node in visited:
            visited[node] = False

        self.q.put(startNode)
        visited[startNode] = True
        parent[startNode] = None

        while not self.q.empty():
            front = self.q.get()
            for neighbour in adjList[front]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    parent[neighbour] = front
                    self.q.put(neighbour)

        self.createTask(parent, startNode, endNode)

    def detectPlayerGhostCollision(self, player, ghosts):
        if self.pos.colliderect(player.pos):
            self.sound_player.playSound('extraPac_sound')
            self.sound_player.takePauseForSomeTime(1_100)
            player.reduceLifeCount()
            player.reset(player.resetPosition)
            for ghost in ghosts:
                ghosts[ghost].reset(ghosts[ghost].resetPosition)

    def move(self, adjList: dict, parent: dict, visited: dict, player):
        if len(self.task) > 0:
            box = self.task[0]
            node = self.getNode(box)

            if self.x != node[0]:
                if node[0] > self.x:
                    self.current_direction = self.directions["right"]
                    self.faceDirection = "right"
                elif node[0] < self.x:
                    self.current_direction = self.directions["left"]
                    self.faceDirection = "left"
            elif self.y != node[1]:
                if node[1] > self.y:
                    self.current_direction = self.directions["down"]
                    self.faceDirection = "right"
                elif node[1] < self.y:
                    self.current_direction = self.directions["up"]
                    self.faceDirection = "left"

            if (self.x != node[0] or self.y != node[1]) and self.current_direction:
                x_velocity = self.speed * self.current_direction[0]
                y_velocity = self.speed * self.current_direction[1]
                self.updatePosition(x_velocity, y_velocity)
            else:
                self.task.pop(0)
        else:
            startNode = f"box_{self.pos.x - (self.pos.x % self.pos.width)}_{self.pos.y - (self.pos.y % self.pos.height)}"
            endNode = f"box_{player.pos.x - (player.pos.x % player.pos.width)}_{player.pos.y - (player.pos.y % player.pos.height)}"

            self.findParentsAndCreateTask(
                adjList, parent, visited, startNode, endNode)

    def updatePosition(self, x, y):
        self.x += x
        self.y += y
        self.pos.x = self.x
        self.pos.y = self.y

    def drawGhost(self, adjList: dict, parent: dict, visited: dict, player, ghosts):
        # self.drawRect(self.colors[self.face], self.pos, 5)
        # self.showTask()

        self.window.blit(
            self.images[self.faceDirection], (self.pos.x, self.pos.y))
        self.move(adjList, parent, visited, player)
        self.detectPlayerGhostCollision(player, ghosts)

    def showTask(self):
        for box in self.task:
            node = self.getNode(box)
            self.drawRect(self.colors[self.face],
                          self.createRect(node[0], node[1], self.width, self.height))

    def getNode(self, box: str):
        node = re.findall(r'\d+', box)
        node = [int(num) for num in node]
        return node

    def drawRect(self, color, pos, width: int = 1):
        pygame.draw.rect(self.window, color, pos, width)

    def createRect(self, x: int, y: int, width: int, height: int):
        return pygame.Rect(x, y, width, height)
