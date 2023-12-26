import pygame
from assets.utils.soundPlayer import SoundPlayer


class Score():
    def __init__(self, window, color: tuple = (255, 0, 0), x: int = 1, scorePos: tuple = (0, 0)) -> None:
        self.window = window
        self.score = 0
        self.font = pygame.font.SysFont('monospace', 11, True, False)
        self.color = color
        self.x = x
        self.scorePos = scorePos
        self.sound_player = SoundPlayer()

    def showScore(self, player: pygame.Rect, food: dict):
        score = self.font.render(f"score: {self.score}", True, self.color)
        self.window.blit(score, self.scorePos)
        self.updateScore(player, food)

    def updateScore(self, player: pygame.Rect, food: dict):
        isColliding = self.detectCollision(food, player)
        if isColliding[1]:
            self.score += self.x
            self.sound_player.playSound('eatFruit_sound')
            food.pop(isColliding[0])

    def detectCollision(self, food: dict, player: pygame.Rect):
        for _ in list(food):
            if player.colliderect(food[_]):
                return (_, True)
        return ("", False)
