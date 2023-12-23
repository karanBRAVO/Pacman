import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

pygame.mixer.init()


class WindowVar:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.pink = (255, 0, 255)
        self.aqua = (0, 255, 255)
        self.font = pygame.font.SysFont('monospace', 11, True, False)
        self.winWidth = 750
        self.winHeight = 350
        self.fps = 60
        self.assets = {
            'beginning_sound': "img/pacmanAssets/pacman_beginning.wav",
            'siren_sound': "img/pacmanAssets/pacman_siren.mp3",
            'chomp_sound': "img/pacmanAssets/pacman_chomp_new.wav",
            'eatFruit_sound': "img/pacmanAssets/pacman_eatfruit.wav",
            'eatGhost_sound': "img/pacmanAssets/pacman_eatghost.wav",
            'death_sound': "img/pacmanAssets/pacman_death.wav",
            'intermission_sound': "img/pacmanAssets/pacman_intermission.wav",
            'extraPac_sound': "img/pacmanAssets/pacman_extrapac.wav",
        }
        self.caption = 'Pacman'
        self.window = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption(self.caption)


class GameVariables(WindowVar):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.playerRect = pygame.Rect(430, 261, 18, 18)

        self.playerRightImg = {
            'pr': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanRight.png"), (self.playerRect.width, self.playerRect.height)),
            'pr1': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanRight1.png"), (self.playerRect.width, self.playerRect.height)),
            'pr2': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanRight2.png"), (self.playerRect.width, self.playerRect.height)),
            'pr3': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanRight3.png"), (self.playerRect.width, self.playerRect.height)),
            'pr4': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanRight4.png"), (self.playerRect.width, self.playerRect.height)),
            'pr5': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanRight5.png"), (self.playerRect.width, self.playerRect.height)),
            'pl': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft.png"), (self.playerRect.width, self.playerRect.height)),
            'pl1': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft1.png"), (self.playerRect.width, self.playerRect.height)),
            'pl2': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft2.png"), (self.playerRect.width, self.playerRect.height)),
            'pl3': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft3.png"), (self.playerRect.width, self.playerRect.height)),
            'pl4': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft4.png"), (self.playerRect.width, self.playerRect.height)),
            'pl5': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft5.png"), (self.playerRect.width, self.playerRect.height)),
        }
        self.playerLeftImg = {
            'pl': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft.png"), (self.playerRect.width, self.playerRect.height)),
            'pl1': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft1.png"), (self.playerRect.width, self.playerRect.height)),
            'pl2': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft2.png"), (self.playerRect.width, self.playerRect.height)),
            'pl3': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft3.png"), (self.playerRect.width, self.playerRect.height)),
            'pl4': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft4.png"), (self.playerRect.width, self.playerRect.height)),
            'pl5': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanLeft5.png"), (self.playerRect.width, self.playerRect.height)),
        }
        self.playerUpImg = {
            'pu': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanUp.png"), (self.playerRect.width, self.playerRect.height)),
            'pu1': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanUp1.png"), (self.playerRect.width, self.playerRect.height)),
            'pu2': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanUp2.png"), (self.playerRect.width, self.playerRect.height)),
            'pu3': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanUp3.png"), (self.playerRect.width, self.playerRect.height)),
            'pu4': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanUp4.png"), (self.playerRect.width, self.playerRect.height)),
            'pu5': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanUp5.png"), (self.playerRect.width, self.playerRect.height)),
        }
        self.playerDownImg = {
            'pd': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanDown.png"), (self.playerRect.width, self.playerRect.height)),
            'pd1': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanDown1.png"), (self.playerRect.width, self.playerRect.height)),
            'pd2': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanDown2.png"), (self.playerRect.width, self.playerRect.height)),
            'pd3': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanDown3.png"), (self.playerRect.width, self.playerRect.height)),
            'pd4': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanDown4.png"), (self.playerRect.width, self.playerRect.height)),
            'pd5': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanDown5.png"), (self.playerRect.width, self.playerRect.height)),
        }
        self.moveLeft = False
        self.pacmanMoveLeftImgLst = [self.playerLeftImg['pl'], self.playerLeftImg['pl1'], self.playerLeftImg['pl2'], self.playerLeftImg['pl3'], self.playerLeftImg['pl4'],
                                     self.playerLeftImg['pl5']]
        self.moveRight = False
        self.pacmanMoveRightImgLst = [self.playerRightImg['pr'], self.playerRightImg['pr1'], self.playerRightImg['pr2'], self.playerRightImg['pr3'], self.playerRightImg['pr4'],
                                      self.playerRightImg['pr5']]
        self.moveUp = False
        self.pacmanMoveUpImgLst = [self.playerUpImg['pu'], self.playerUpImg['pu1'], self.playerUpImg['pu2'], self.playerUpImg['pu3'], self.playerUpImg['pu4'],
                                   self.playerUpImg['pu5']]
        self.moveDown = False
        self.pacmanMoveDownImgLst = [self.playerDownImg['pd'], self.playerDownImg['pd1'], self.playerDownImg['pd2'], self.playerDownImg['pd3'], self.playerDownImg['pd4'],
                                     self.playerDownImg['pd5']]
        self.walkCount = 0

        self.playerVel = 1

        self.topRect = pygame.Rect(10, 0, self.winWidth - 20, 10)

        self.leftTopRect = pygame.Rect(0, 10, 10, 60)

        self.obstacle1TopLeft_left = pygame.Rect(30, 30, 10, 20)
        self.obstacle1TopLeft_right = pygame.Rect(90, 30, 10, 20)
        self.obstacle1TopLeft_top = pygame.Rect(40, 30, 50, 10)
        self.obstacle1TopLeft_bottom = pygame.Rect(40, 40, 50, 10)

        self.obstacle2TopLeft_left = pygame.Rect(210, 30, 10, 30)
        self.obstacle2TopLeft_right = pygame.Rect(360, 30, 10, 30)
        self.obstacle2TopLeft_top = pygame.Rect(220, 30, 140, 10)
        self.obstacle2TopLeft_bottom = pygame.Rect(220, 40, 140, 20)

        self.obstacle3TopLeft_left = pygame.Rect(390, 30, 10, 50)
        self.obstacle3TopLeft_right = pygame.Rect(470, 30, 10, 50)
        self.obstacle3TopLeft_top = pygame.Rect(400, 30, 70, 20)
        self.obstacle3TopLeft_bottom = pygame.Rect(400, 50, 70, 30)

        self.obstacle2TopRight_top = pygame.Rect(
            self.winWidth - 200, 30, 50, 20)
        self.obstacle2TopRight_left = pygame.Rect(
            self.winWidth - 210, 30, 10, 50)
        self.obstacle2TopRight_right = pygame.Rect(
            self.winWidth - 150, 30, 10, 50)
        self.obstacle2TopRight_bottom = pygame.Rect(
            self.winWidth - 200, 50, 50, 30)

        self.obstacle1TopRight_top = pygame.Rect(
            self.winWidth - 110, 30, 70, 10)
        self.obstacle1TopRight_left = pygame.Rect(
            self.winWidth - 120, 30, 10, 10)
        self.obstacle1TopRight_right = pygame.Rect(
            self.winWidth - 40, 30, 10, 10)
        self.obstacle1TopRight_bottom = pygame.Rect(
            self.winWidth - 120, 40, 90, 10)

        self.WordGTop = pygame.Rect(130, 30, 50, 50)
        self.WordGTopInside = pygame.Rect(130, 80, 50, 10)
        self.WordGLeft = pygame.Rect(120, 30, 10, 250)
        self.WordGLeftInside = pygame.Rect(130, 90, 10, 130)
        self.WordGCurveTop = pygame.Rect(170, 110, 10, 70)
        self.WordGCurveLeft = pygame.Rect(160, 110, 10, 80)
        self.WordGCurveBottom = pygame.Rect(170, 180, 10, 10)
        self.WordGRight1 = pygame.Rect(180, 30, 10, 60)
        self.WordGRight2 = pygame.Rect(180, 110, 10, 170)
        self.WordGRight2Inside = pygame.Rect(170, 190, 10, 30)
        self.WordGBottomInside = pygame.Rect(130, 220, 50, 10)
        self.WordGBottom = pygame.Rect(130, 230, 50, 50)

        self.WordO1Top = pygame.Rect(230, 80, 30, 20)
        self.WordO1Left = pygame.Rect(210, 80, 20, 200)
        self.WordO1Right = pygame.Rect(260, 80, 20, 200)
        self.WordO1Bottom = pygame.Rect(230, 260, 30, 20)

        self.WordO2Top = pygame.Rect(320, 80, 30, 20)
        self.WordO2Left = pygame.Rect(300, 80, 20, 200)
        self.WordO2Right = pygame.Rect(350, 80, 20, 200)
        self.WordO2Bottom = pygame.Rect(320, 260, 30, 20)

        self.enemyContainerTop1_G = pygame.Rect(400, 100, 20, 10)
        self.enemyContainerTop1Inside_G = pygame.Rect(400, 110, 20, 10)
        self.enemyContainerTop2_G = pygame.Rect(450, 100, 20, 10)
        self.enemyContainerTop2Inside_G = pygame.Rect(450, 110, 20, 10)
        self.enemyContainerLeft_G = pygame.Rect(390, 100, 10, 160)
        self.enemyContainerLeftInside_G = pygame.Rect(400, 120, 10, 120)
        self.enemyContainerRight_G = pygame.Rect(470, 100, 10, 160)
        self.enemyContainerRightInside_G = pygame.Rect(460, 120, 10, 120)
        self.enemyContainerBottomInside_G = pygame.Rect(400, 240, 70, 10)
        self.enemyContainerBottom_G = pygame.Rect(400, 250, 70, 10)
        self.obstacle_GTopLeft = pygame.Rect(390, 280, 10, 20)
        self.obstacle_G = pygame.Rect(400, 280, 70, 10)
        self.obstacle_GTopBottom = pygame.Rect(400, 290, 70, 10)
        self.obstacle_GTopRight = pygame.Rect(470, 280, 10, 20)
        self.obstacle_GLeft_top = pygame.Rect(380, 320, 20, 10)
        self.obstacle_GLeft_left = pygame.Rect(380, 330, 10, 10)
        self.obstacle_GLeft_right = pygame.Rect(390, 330, 10, 10)
        self.obstacle_GRight_top = pygame.Rect(470, 320, 20, 10)
        self.obstacle_GRight_left = pygame.Rect(470, 330, 10, 10)
        self.obstacle_GRight_right = pygame.Rect(480, 330, 10, 10)
        self.obstacle_GBottomLeft = pygame.Rect(420, 300, 20, 10)
        self.obstacle_GBottom = pygame.Rect(420, 310, 30, 10)
        self.obstacle_GBottomRight = pygame.Rect(440, 300, 10, 10)

        self.WordLTop = pygame.Rect(500, 30, 20, 10)
        self.WordLLeft = pygame.Rect(500, 40, 10, 230)
        self.WordLRight = pygame.Rect(510, 40, 10, 230)
        self.WordLBottom = pygame.Rect(500, 270, 20, 10)

        self.WordETop = pygame.Rect(550, 100, 70, 10)
        self.WordELeft = pygame.Rect(540, 100, 10, 180)
        self.WordEMidTop = pygame.Rect(580, 170, 40, 10)
        self.WordEMidBottom = pygame.Rect(580, 200, 40, 10)
        self.WordEMidLeft = pygame.Rect(570, 170, 10, 40)
        self.WordERight1 = pygame.Rect(620, 100, 10, 80)
        self.WordERight2 = pygame.Rect(620, 200, 10, 80)
        self.WordEBottom = pygame.Rect(550, 260, 70, 20)

        self.leftMidTop1Rect = pygame.Rect(10, 70, 80, 10)
        self.leftMidTop2Rect = pygame.Rect(90, 70, 10, 40)
        self.leftMidTop3Rect = pygame.Rect(0, 100, 90, 10)
        self.leftMidTop4Rect = pygame.Rect(0, 130, 90, 10)
        self.leftMidTop5Rect = pygame.Rect(90, 130, 10, 40)
        self.leftMidTop6Rect = pygame.Rect(0, 160, 90, 10)
        self.leftMidBottom6Rect = pygame.Rect(0, self.winHeight - 170, 90, 10)
        self.leftMidBottom5Rect = pygame.Rect(90, self.winHeight - 170, 10, 40)
        self.leftMidBottom4Rect = pygame.Rect(0, self.winHeight - 140, 90, 10)
        self.leftMidBottom3Rect = pygame.Rect(0, self.winHeight - 110, 90, 10)
        self.leftMidBottom2Rect = pygame.Rect(90, self.winHeight - 110, 10, 40)
        self.leftMidBottom1Rect = pygame.Rect(10, self.winHeight - 80, 80, 10)
        self.leftBottomRect = pygame.Rect(0, self.winHeight - 70, 10, 60)

        self.rightTopRect = pygame.Rect(self.winWidth - 10, 10, 10, 60)

        self.rightMidTop1Rect = pygame.Rect(self.winWidth - 90, 70, 80, 10)
        self.rightMidTop2Rect = pygame.Rect(self.winWidth - 100, 70, 10, 40)
        self.rightMidTop3Rect = pygame.Rect(self.winWidth - 90, 100, 90, 10)
        self.rightMidTop4Rect = pygame.Rect(self.winWidth - 90, 130, 90, 10)
        self.rightMidTop5Rect = pygame.Rect(self.winWidth - 100, 130, 10, 40)
        self.rightMidTop6Rect = pygame.Rect(self.winWidth - 90, 160, 90, 10)
        self.rightMidBottom6Rect = pygame.Rect(
            self.winWidth - 90, self.winHeight - 170, 90, 10)
        self.rightMidBottom5Rect = pygame.Rect(
            self.winWidth - 100, self.winHeight - 170, 10, 40)
        self.rightMidBottom4Rect = pygame.Rect(
            self.winWidth - 90, self.winHeight - 140, 90, 10)
        self.rightMidBottom3Rect = pygame.Rect(
            self.winWidth - 90, self.winHeight - 110, 90, 10)
        self.rightMidBottom2Rect = pygame.Rect(
            self.winWidth - 100, self.winHeight - 110, 10, 40)
        self.rightMidBottom1Rect = pygame.Rect(
            self.winWidth - 90, self.winHeight - 80, 80, 10)

        self.obstacle1BottomLeft_top = pygame.Rect(
            30, self.winHeight - 50, 80, 10)
        self.obstacle1BottomLeft_left = pygame.Rect(
            30, self.winHeight - 40, 10, 10)
        self.obstacle1BottomLeft_right = pygame.Rect(
            100, self.winHeight - 40, 10, 10)
        self.obstacle1BottomLeft_bottom = pygame.Rect(
            40, self.winHeight - 40, 60, 10)

        self.obstacle2BottomLeft_top = pygame.Rect(
            140, self.winHeight - 50, 60, 10)
        self.obstacle2BottomLeft_left = pygame.Rect(
            130, self.winHeight - 50, 10, 20)
        self.obstacle2BottomLeft_right = pygame.Rect(
            200, self.winHeight - 50, 10, 20)
        self.obstacle2BottomLeft_bottom = pygame.Rect(
            140, self.winHeight - 40, 60, 10)

        self.obstacle3BottomLeft_top = pygame.Rect(
            230, self.winHeight - 50, 20, 10)
        self.obstacle3BottomLeft_left = pygame.Rect(
            230, self.winHeight - 40, 10, 30)
        self.obstacle3BottomLeft_right = pygame.Rect(
            240, self.winHeight - 40, 10, 30)

        self.obstacle4BottomLeft_top = pygame.Rect(
            280, self.winHeight - 50, 70, 10)
        self.obstacle4BottomLeft_left = pygame.Rect(
            270, self.winHeight - 50, 10, 20)
        self.obstacle4BottomLeft_right = pygame.Rect(
            350, self.winHeight - 50, 10, 20)
        self.obstacle4BottomLeft_bottom = pygame.Rect(
            280, self.winHeight - 40, 70, 10)

        self.obstacle2BottomRight_top = pygame.Rect(
            self.winWidth - 230, self.winHeight - 50, 90, 10)
        self.obstacle2BottomRight_left = pygame.Rect(
            self.winWidth - 240, self.winHeight - 50, 10, 20)
        self.obstacle2BottomRight_right = pygame.Rect(
            self.winWidth - 140, self.winHeight - 50, 10, 20)
        self.obstacle2BottomRight_bottom = pygame.Rect(
            self.winWidth - 230, self.winHeight - 40, 90, 10)

        self.obstacle1BottomRight_top = pygame.Rect(
            self.winWidth - 100, self.winHeight - 50, 60, 10)
        self.obstacle1BottomRight_left = pygame.Rect(
            self.winWidth - 110, self.winHeight - 50, 10, 20)
        self.obstacle1BottomRight_right = pygame.Rect(
            self.winWidth - 40, self.winHeight - 50, 10, 20)
        self.obstacle1BottomRight_bottom = pygame.Rect(
            self.winWidth - 100, self.winHeight - 40, 60, 10)

        self.rightBottomRect = pygame.Rect(
            self.winWidth - 10, self.winHeight - 70, 10, 60)

        self.bottomRect = pygame.Rect(
            10, self.winHeight - 10, self.winWidth - 20, 10)

        self.obs_top = [self.topRect,
                        self.obstacle1TopLeft_top,
                        self.obstacle2TopLeft_top,
                        self.obstacle3TopLeft_top,
                        self.obstacle2TopRight_top,
                        self.obstacle1TopRight_top,
                        self.WordGTop,
                        self.WordGTopInside,
                        self.WordGCurveTop,
                        self.WordO1Top,
                        self.WordO2Top,
                        self.enemyContainerTop1_G,
                        self.enemyContainerTop1Inside_G,
                        self.enemyContainerTop2_G,
                        self.enemyContainerTop2Inside_G,
                        self.obstacle_GLeft_top,
                        self.obstacle_GRight_top,
                        self.WordLTop,
                        self.WordETop,
                        self.WordEMidTop,
                        self.leftMidTop1Rect,
                        self.leftMidTop2Rect,
                        self.leftMidTop3Rect,
                        self.leftMidTop4Rect,
                        self.leftMidTop5Rect,
                        self.leftMidTop6Rect,
                        self.rightTopRect,
                        self.rightMidTop1Rect,
                        self.rightMidTop2Rect,
                        self.rightMidTop3Rect,
                        self.rightMidTop4Rect,
                        self.rightMidTop5Rect,
                        self.rightMidTop6Rect,
                        self.obstacle1BottomLeft_top,
                        self.obstacle2BottomLeft_top,
                        self.obstacle3BottomLeft_top,
                        self.obstacle4BottomLeft_top,
                        self.obstacle2BottomRight_top,
                        self.obstacle1BottomRight_top]
        self.obs_bottom = [self.obstacle1TopLeft_bottom,
                           self.obstacle2TopLeft_bottom,
                           self.obstacle3TopLeft_bottom,
                           self.obstacle2TopRight_bottom,
                           self.obstacle1TopRight_bottom,
                           self.WordGBottom,
                           self.WordO1Bottom,
                           self.WordO2Bottom,
                           self.enemyContainerBottom_G,
                           self.obstacle_GTopBottom,
                           self.WordLBottom,
                           self.WordEBottom,
                           self.leftMidBottom6Rect,
                           self.leftMidBottom5Rect,
                           self.leftMidBottom4Rect,
                           self.leftMidBottom3Rect,
                           self.leftMidBottom2Rect,
                           self.leftMidBottom1Rect,
                           self.leftBottomRect,
                           self.rightMidBottom6Rect,
                           self.rightMidBottom5Rect,
                           self.rightMidBottom4Rect,
                           self.rightMidBottom3Rect,
                           self.rightMidBottom2Rect,
                           self.rightMidBottom1Rect,
                           self.obstacle1BottomLeft_bottom,
                           self.obstacle2BottomLeft_bottom,
                           self.obstacle4BottomLeft_bottom,
                           self.obstacle2BottomRight_bottom,
                           self.obstacle1BottomRight_bottom,
                           self.bottomRect]
        self.obs_right = [self.obstacle1TopLeft_right,
                          self.obstacle2TopLeft_right,
                          self.obstacle3TopLeft_right,
                          self.obstacle2TopRight_right,
                          self.obstacle1TopRight_right,
                          self.WordGRight1,
                          self.WordGRight2,
                          self.WordO1Right,
                          self.WordO2Right,
                          self.enemyContainerRight_G,
                          self.obstacle_GTopRight,
                          self.obstacle_GLeft_right,
                          self.obstacle_GRight_right,
                          self.obstacle_GBottomRight,
                          self.WordLRight,
                          self.WordERight1,
                          self.WordERight2,
                          self.obstacle1BottomLeft_right,
                          self.obstacle2BottomLeft_right,
                          self.obstacle3BottomLeft_right,
                          self.obstacle4BottomLeft_right,
                          self.obstacle2BottomRight_right,
                          self.obstacle1BottomRight_right,
                          self.rightBottomRect]
        self.obs_left = [self.leftTopRect,
                         self.obstacle1TopLeft_left,
                         self.obstacle2TopLeft_left,
                         self.obstacle3TopLeft_left,
                         self.obstacle2TopRight_left,
                         self.obstacle1TopRight_left,
                         self.WordGLeft,
                         self.WordGLeftInside,
                         self.WordGCurveLeft,
                         self.WordO1Left,
                         self.WordO2Left,
                         self.enemyContainerLeft_G,
                         self.enemyContainerLeftInside_G,
                         self.obstacle_GTopLeft,
                         self.obstacle_GLeft_left,
                         self.obstacle_GRight_left,
                         self.obstacle_GBottomLeft,
                         self.WordLLeft,
                         self.WordELeft,
                         self.obstacle1BottomLeft_left,
                         self.obstacle2BottomLeft_left,
                         self.obstacle3BottomLeft_left,
                         self.obstacle4BottomLeft_left,
                         self.obstacle2BottomRight_left,
                         self.obstacle1BottomRight_left]
        self.layout_name_lst = [self.topRect,
                                self.leftTopRect,

                                self.obstacle1TopLeft_top,
                                self.obstacle1TopLeft_left,
                                self.obstacle1TopLeft_right,
                                self.obstacle1TopLeft_bottom,

                                self.obstacle2TopLeft_top,
                                self.obstacle2TopLeft_left,
                                self.obstacle2TopLeft_right,
                                self.obstacle2TopLeft_bottom,

                                self.obstacle3TopLeft_top,
                                self.obstacle3TopLeft_left,
                                self.obstacle3TopLeft_right,
                                self.obstacle3TopLeft_bottom,

                                self.obstacle2TopRight_top,
                                self.obstacle2TopRight_left,
                                self.obstacle2TopRight_right,
                                self.obstacle2TopRight_bottom,

                                self.obstacle1TopRight_top,
                                self.obstacle1TopRight_left,
                                self.obstacle1TopRight_right,
                                self.obstacle1TopRight_bottom,

                                self.WordGTop,
                                self.WordGTopInside,
                                self.WordGLeft,
                                self.WordGLeftInside,
                                self.WordGCurveTop,
                                self.WordGCurveLeft,
                                self.WordGCurveBottom,
                                self.WordGRight1,
                                self.WordGRight2,
                                self.WordGRight2Inside,
                                self.WordGBottom,
                                self.WordGBottomInside,

                                self.WordO1Top,
                                self.WordO1Left,
                                self.WordO1Right,
                                self.WordO1Bottom,
                                self.WordO2Top,
                                self.WordO2Left,
                                self.WordO2Right,
                                self.WordO2Bottom,

                                self.enemyContainerTop1_G,
                                self.enemyContainerTop1Inside_G,
                                self.enemyContainerTop2_G,
                                self.enemyContainerTop2Inside_G,
                                self.enemyContainerLeft_G,
                                self.enemyContainerLeftInside_G,
                                self.enemyContainerRight_G,
                                self.enemyContainerRightInside_G,
                                self.enemyContainerBottom_G,
                                self.enemyContainerBottomInside_G,
                                self.obstacle_GTopLeft,
                                self.obstacle_G,
                                self.obstacle_GTopBottom,
                                self.obstacle_GTopRight,
                                self.obstacle_GLeft_top,
                                self.obstacle_GLeft_left,
                                self.obstacle_GLeft_right,
                                self.obstacle_GRight_top,
                                self.obstacle_GRight_left,
                                self.obstacle_GRight_right,
                                self.obstacle_GBottomLeft,
                                self.obstacle_GBottom,
                                self.obstacle_GBottomRight,

                                self.WordLTop,
                                self.WordLLeft,
                                self.WordLRight,
                                self.WordLBottom,

                                self.WordETop,
                                self.WordELeft,
                                self.WordEMidTop,
                                self.WordEMidBottom,
                                self.WordEMidLeft,
                                self.WordERight1,
                                self.WordERight2,
                                self.WordEBottom,

                                self.leftMidTop1Rect,
                                self.leftMidTop2Rect,
                                self.leftMidTop3Rect,
                                self.leftMidTop4Rect,
                                self.leftMidTop5Rect,
                                self.leftMidTop6Rect,
                                self.leftMidBottom6Rect,
                                self.leftMidBottom5Rect,
                                self.leftMidBottom4Rect,
                                self.leftMidBottom3Rect,
                                self.leftMidBottom2Rect,
                                self.leftMidBottom1Rect,
                                self.leftBottomRect,

                                self.rightTopRect,
                                self.rightMidTop1Rect,
                                self.rightMidTop2Rect,
                                self.rightMidTop3Rect,
                                self.rightMidTop4Rect,
                                self.rightMidTop5Rect,
                                self.rightMidTop6Rect,
                                self.rightMidBottom6Rect,
                                self.rightMidBottom5Rect,
                                self.rightMidBottom4Rect,
                                self.rightMidBottom3Rect,
                                self.rightMidBottom2Rect,
                                self.rightMidBottom1Rect,

                                self.obstacle1BottomLeft_top,
                                self.obstacle1BottomLeft_left,
                                self.obstacle1BottomLeft_right,
                                self.obstacle1BottomLeft_bottom,
                                self.obstacle2BottomLeft_top,
                                self.obstacle2BottomLeft_left,
                                self.obstacle2BottomLeft_right,
                                self.obstacle2BottomLeft_bottom,
                                self.obstacle3BottomLeft_top,
                                self.obstacle3BottomLeft_left,
                                self.obstacle3BottomLeft_right,
                                self.obstacle4BottomLeft_top,
                                self.obstacle4BottomLeft_left,
                                self.obstacle4BottomLeft_right,
                                self.obstacle4BottomLeft_bottom,
                                self.obstacle2BottomRight_top,
                                self.obstacle2BottomRight_left,
                                self.obstacle2BottomRight_right,
                                self.obstacle2BottomRight_bottom,
                                self.obstacle1BottomRight_top,
                                self.obstacle1BottomRight_left,
                                self.obstacle1BottomRight_right,
                                self.obstacle1BottomRight_bottom,

                                self.rightBottomRect,
                                self.bottomRect]

        self.ghostSize = 18
        self.ghostVel = 1
        self.redGhostRect = pygame.Rect(
            self.enemyContainerBottomInside_G.x + 10, 261, self.ghostSize, self.ghostSize)
        self.blueGhostRect = pygame.Rect(self.enemyContainerTop1Inside_G.x + 10,
                                         self.enemyContainerTop1Inside_G.y + 25, self.ghostSize, self.ghostSize)
        self.orangeGhostRect = pygame.Rect(self.enemyContainerTop2Inside_G.x - 15,
                                           self.enemyContainerTop2Inside_G.y + 25, self.ghostSize, self.ghostSize)
        self.pinkGhostRect = pygame.Rect(self.enemyContainerBottomInside_G.x + 35,
                                         self.enemyContainerBottomInside_G.y - 25, self.ghostSize, self.ghostSize)
        self.ghostImg = {
            'redRight': pygame.transform.scale(pygame.image.load("img/pacmanAssets/redGhostright.png"), (self.ghostSize, self.ghostSize)),
            'redLeft': pygame.transform.scale(pygame.image.load("img/pacmanAssets/redGhostleft.png"), (self.ghostSize, self.ghostSize)),
            'orangeRight': pygame.transform.scale(pygame.image.load("img/pacmanAssets/orangeGhostright.png"), (self.ghostSize, self.ghostSize)),
            'orangeLeft': pygame.transform.scale(pygame.image.load("img/pacmanAssets/orangeGhostleft.png"), (self.ghostSize, self.ghostSize)),
            'blueRight': pygame.transform.scale(pygame.image.load("img/pacmanAssets/blueGhostright.png"), (self.ghostSize, self.ghostSize)),
            'blueLeft': pygame.transform.scale(pygame.image.load("img/pacmanAssets/blueGhostleft.png"), (self.ghostSize, self.ghostSize)),
            'pinkRight': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pinkGhostright.png"), (self.ghostSize, self.ghostSize)),
            'pinkLeft': pygame.transform.scale(pygame.image.load("img/pacmanAssets/pinkGhostleft.png"), (self.ghostSize, self.ghostSize)),
        }


class Food(WindowVar):
    def __init__(self):
        super().__init__()
        self.foodPosLst = []
        for i in range(1, 73):  # top line
            self.food_i = pygame.Rect((i + 1) * 10, 20, 5, 5)
            self.foodPosLst.append(self.food_i)
        """ line 1 """
        self.food_73 = pygame.Rect(20, 30, 5, 5)
        self.food_74 = pygame.Rect(110, 30, 5, 5)
        self.food_75 = pygame.Rect(200, 30, 5, 5)
        self.food_76 = pygame.Rect(380, 30, 5, 5)
        self.food_77 = pygame.Rect(490, 30, 5, 5)
        self.food_78 = pygame.Rect(530, 30, 5, 5)
        self.food_79 = pygame.Rect(620, 30, 5, 5)
        self.food_80 = pygame.Rect(730, 30, 5, 5)
        """ line 2 """
        self.food_81 = pygame.Rect(20, 40, 5, 5)
        self.food_82 = pygame.Rect(110, 40, 5, 5)
        self.food_83 = pygame.Rect(200, 40, 5, 5)
        self.food_84 = pygame.Rect(380, 40, 5, 5)
        self.food_85 = pygame.Rect(490, 40, 5, 5)
        self.food_86 = pygame.Rect(530, 40, 5, 5)
        self.food_87 = pygame.Rect(620, 40, 5, 5)
        self.food_88 = pygame.Rect(730, 40, 5, 5)
        """ line 3 """
        self.food_89 = pygame.Rect(20, 50, 5, 5)
        self.food_90 = pygame.Rect(110, 50, 5, 5)
        self.food_91 = pygame.Rect(200, 50, 5, 5)
        self.food_92 = pygame.Rect(380, 50, 5, 5)
        self.food_93 = pygame.Rect(490, 50, 5, 5)
        self.food_94 = pygame.Rect(530, 50, 5, 5)
        self.food_95 = pygame.Rect(620, 50, 5, 5)
        self.food_96 = pygame.Rect(730, 50, 5, 5)
        """ line 4 """
        self.food_97 = pygame.Rect(20, 60, 5, 5)
        self.food_98 = pygame.Rect(30, 60, 5, 5)
        self.food_99 = pygame.Rect(40, 60, 5, 5)
        self.food_100 = pygame.Rect(50, 60, 5, 5)
        self.food_101 = pygame.Rect(60, 60, 5, 5)
        self.food_102 = pygame.Rect(70, 60, 5, 5)
        self.food_103 = pygame.Rect(80, 60, 5, 5)
        self.food_104 = pygame.Rect(90, 60, 5, 5)
        self.food_105 = pygame.Rect(100, 60, 5, 5)
        self.food_106 = pygame.Rect(110, 60, 5, 5)
        self.food_107 = pygame.Rect(200, 60, 5, 5)
        self.food_108 = pygame.Rect(380, 60, 5, 5)
        self.food_109 = pygame.Rect(490, 60, 5, 5)
        self.food_110 = pygame.Rect(530, 60, 5, 5)
        self.food_111 = pygame.Rect(620, 60, 5, 5)
        self.food_112 = pygame.Rect(630, 60, 5, 5)
        self.food_113 = pygame.Rect(640, 60, 5, 5)
        self.food_114 = pygame.Rect(650, 60, 5, 5)
        self.food_115 = pygame.Rect(660, 60, 5, 5)
        self.food_116 = pygame.Rect(670, 60, 5, 5)
        self.food_117 = pygame.Rect(680, 60, 5, 5)
        self.food_118 = pygame.Rect(690, 60, 5, 5)
        self.food_119 = pygame.Rect(700, 60, 5, 5)
        self.food_120 = pygame.Rect(710, 60, 5, 5)
        self.food_121 = pygame.Rect(720, 60, 5, 5)
        self.food_122 = pygame.Rect(730, 60, 5, 5)
        """ line 5 """
        self.food_123 = pygame.Rect(110, 70, 5, 5)
        self.food_124 = pygame.Rect(200, 70, 5, 5)
        self.food_125 = pygame.Rect(210, 70, 5, 5)
        self.food_126 = pygame.Rect(220, 70, 5, 5)
        self.food_127 = pygame.Rect(230, 70, 5, 5)
        self.food_128 = pygame.Rect(240, 70, 5, 5)
        self.food_129 = pygame.Rect(250, 70, 5, 5)
        self.food_130 = pygame.Rect(260, 70, 5, 5)
        self.food_131 = pygame.Rect(270, 70, 5, 5)
        self.food_132 = pygame.Rect(280, 70, 5, 5)
        self.food_133 = pygame.Rect(290, 70, 5, 5)
        self.food_134 = pygame.Rect(300, 70, 5, 5)
        self.food_135 = pygame.Rect(310, 70, 5, 5)
        self.food_136 = pygame.Rect(320, 70, 5, 5)
        self.food_137 = pygame.Rect(330, 70, 5, 5)
        self.food_138 = pygame.Rect(340, 70, 5, 5)
        self.food_139 = pygame.Rect(350, 70, 5, 5)
        self.food_140 = pygame.Rect(360, 70, 5, 5)
        self.food_141 = pygame.Rect(370, 70, 5, 5)
        self.food_142 = pygame.Rect(380, 70, 5, 5)
        self.food_143 = pygame.Rect(490, 70, 5, 5)
        self.food_144 = pygame.Rect(530, 70, 5, 5)
        self.food_145 = pygame.Rect(620, 70, 5, 5)
        self.food_146 = pygame.Rect(630, 70, 5, 5)
        self.food_147 = pygame.Rect(640, 70, 5, 5)
        """ line 5 """
        self.food_148 = pygame.Rect(110, 80, 5, 5)
        self.food_149 = pygame.Rect(200, 80, 5, 5)
        self.food_150 = pygame.Rect(290, 80, 5, 5)
        self.food_151 = pygame.Rect(380, 80, 5, 5)
        self.food_152 = pygame.Rect(490, 80, 5, 5)
        self.food_153 = pygame.Rect(530, 80, 5, 5)
        self.food_154 = pygame.Rect(620, 80, 5, 5)
        self.food_155 = pygame.Rect(630, 80, 5, 5)
        self.food_156 = pygame.Rect(640, 80, 5, 5)
        """ line 6 """
        self.food_157 = pygame.Rect(110, 90, 5, 5)
        self.food_158 = pygame.Rect(200, 90, 5, 5)
        self.food_159 = pygame.Rect(290, 90, 5, 5)
        self.food_160 = pygame.Rect(380, 90, 5, 5)
        self.food_161 = pygame.Rect(390, 90, 5, 5)
        self.food_162 = pygame.Rect(400, 90, 5, 5)
        self.food_163 = pygame.Rect(410, 90, 5, 5)
        self.food_164 = pygame.Rect(420, 90, 5, 5)
        self.food_165 = pygame.Rect(430, 90, 5, 5)
        self.food_166 = pygame.Rect(440, 90, 5, 5)
        self.food_167 = pygame.Rect(450, 90, 5, 5)
        self.food_168 = pygame.Rect(460, 90, 5, 5)
        self.food_169 = pygame.Rect(470, 90, 5, 5)
        self.food_170 = pygame.Rect(480, 90, 5, 5)
        self.food_171 = pygame.Rect(490, 90, 5, 5)
        self.food_172 = pygame.Rect(530, 90, 5, 5)
        self.food_173 = pygame.Rect(540, 90, 5, 5)
        self.food_174 = pygame.Rect(550, 90, 5, 5)
        self.food_175 = pygame.Rect(560, 90, 5, 5)
        self.food_176 = pygame.Rect(570, 90, 5, 5)
        self.food_177 = pygame.Rect(580, 90, 5, 5)
        self.food_178 = pygame.Rect(590, 90, 5, 5)
        self.food_179 = pygame.Rect(600, 90, 5, 5)
        self.food_180 = pygame.Rect(610, 90, 5, 5)
        self.food_181 = pygame.Rect(620, 90, 5, 5)
        self.food_182 = pygame.Rect(630, 90, 5, 5)
        self.food_183 = pygame.Rect(640, 90, 5, 5)
        """ line 7 """
        self.food_184 = pygame.Rect(110, 100, 5, 5)
        self.food_185 = pygame.Rect(150, 100, 5, 5)
        self.food_186 = pygame.Rect(160, 100, 5, 5)
        self.food_187 = pygame.Rect(170, 100, 5, 5)
        self.food_188 = pygame.Rect(180, 100, 5, 5)
        self.food_189 = pygame.Rect(190, 100, 5, 5)
        self.food_190 = pygame.Rect(200, 100, 5, 5)
        self.food_191 = pygame.Rect(290, 100, 5, 5)
        self.food_192 = pygame.Rect(380, 100, 5, 5)
        self.food_193 = pygame.Rect(490, 100, 5, 5)
        self.food_194 = pygame.Rect(530, 100, 5, 5)
        self.food_195 = pygame.Rect(640, 100, 5, 5)
        """ line 8 """
        self.food_196 = pygame.Rect(110, 110, 5, 5)
        self.food_197 = pygame.Rect(150, 110, 5, 5)
        self.food_198 = pygame.Rect(200, 110, 5, 5)
        self.food_199 = pygame.Rect(290, 110, 5, 5)
        self.food_200 = pygame.Rect(380, 110, 5, 5)
        self.food_201 = pygame.Rect(490, 110, 5, 5)
        self.food_202 = pygame.Rect(530, 110, 5, 5)
        self.food_203 = pygame.Rect(640, 110, 5, 5)
        """ line 9 """
        self.food_204 = pygame.Rect(20, 120, 5, 5)
        self.food_205 = pygame.Rect(30, 120, 5, 5)
        self.food_206 = pygame.Rect(40, 120, 5, 5)
        self.food_207 = pygame.Rect(50, 120, 5, 5)
        self.food_208 = pygame.Rect(60, 120, 5, 5)
        self.food_209 = pygame.Rect(70, 120, 5, 5)
        self.food_210 = pygame.Rect(80, 120, 5, 5)
        self.food_211 = pygame.Rect(90, 120, 5, 5)
        self.food_212 = pygame.Rect(100, 120, 5, 5)
        self.food_213 = pygame.Rect(110, 120, 5, 5)
        self.food_214 = pygame.Rect(150, 120, 5, 5)
        self.food_215 = pygame.Rect(200, 120, 5, 5)
        self.food_216 = pygame.Rect(290, 120, 5, 5)
        self.food_217 = pygame.Rect(380, 120, 5, 5)
        self.food_218 = pygame.Rect(490, 120, 5, 5)
        self.food_219 = pygame.Rect(530, 120, 5, 5)
        self.food_220 = pygame.Rect(640, 120, 5, 5)
        """ line 10 """
        self.food_221 = pygame.Rect(110, 130, 5, 5)
        self.food_222 = pygame.Rect(150, 130, 5, 5)
        self.food_223 = pygame.Rect(200, 130, 5, 5)
        self.food_224 = pygame.Rect(290, 130, 5, 5)
        self.food_225 = pygame.Rect(380, 130, 5, 5)
        self.food_226 = pygame.Rect(490, 130, 5, 5)
        self.food_227 = pygame.Rect(530, 130, 5, 5)
        self.food_228 = pygame.Rect(640, 130, 5, 5)
        """ line 11 """
        self.food_229 = pygame.Rect(110, 140, 5, 5)
        self.food_230 = pygame.Rect(150, 140, 5, 5)
        self.food_231 = pygame.Rect(200, 140, 5, 5)
        self.food_232 = pygame.Rect(290, 140, 5, 5)
        self.food_233 = pygame.Rect(380, 140, 5, 5)
        self.food_234 = pygame.Rect(490, 140, 5, 5)
        self.food_235 = pygame.Rect(530, 140, 5, 5)
        self.food_236 = pygame.Rect(640, 140, 5, 5)
        """ line 12 """
        self.food_237 = pygame.Rect(110, 150, 5, 5)
        self.food_238 = pygame.Rect(150, 150, 5, 5)
        self.food_239 = pygame.Rect(200, 150, 5, 5)
        self.food_240 = pygame.Rect(290, 150, 5, 5)
        self.food_241 = pygame.Rect(380, 150, 5, 5)
        self.food_242 = pygame.Rect(490, 150, 5, 5)
        self.food_243 = pygame.Rect(530, 150, 5, 5)
        self.food_244 = pygame.Rect(640, 150, 5, 5)
        """ line 13 """
        self.food_245 = pygame.Rect(110, 160, 5, 5)
        self.food_246 = pygame.Rect(150, 160, 5, 5)
        self.food_247 = pygame.Rect(200, 160, 5, 5)
        self.food_248 = pygame.Rect(290, 160, 5, 5)
        self.food_249 = pygame.Rect(380, 160, 5, 5)
        self.food_250 = pygame.Rect(490, 160, 5, 5)
        self.food_251 = pygame.Rect(530, 160, 5, 5)
        self.food_252 = pygame.Rect(640, 160, 5, 5)
        """ line 14 """
        self.food_253 = pygame.Rect(110, 170, 5, 5)
        self.food_254 = pygame.Rect(150, 170, 5, 5)
        self.food_255 = pygame.Rect(200, 170, 5, 5)
        self.food_256 = pygame.Rect(290, 170, 5, 5)
        self.food_257 = pygame.Rect(380, 170, 5, 5)
        self.food_258 = pygame.Rect(490, 170, 5, 5)
        self.food_259 = pygame.Rect(530, 170, 5, 5)
        self.food_260 = pygame.Rect(640, 170, 5, 5)
        """ line 15 """
        self.food_261 = pygame.Rect(110, 180, 5, 5)
        self.food_262 = pygame.Rect(150, 180, 5, 5)
        self.food_263 = pygame.Rect(200, 180, 5, 5)
        self.food_264 = pygame.Rect(290, 180, 5, 5)
        self.food_265 = pygame.Rect(380, 180, 5, 5)
        self.food_266 = pygame.Rect(490, 180, 5, 5)
        self.food_267 = pygame.Rect(530, 180, 5, 5)
        self.food_268 = pygame.Rect(640, 180, 5, 5)
        """ line 16 """
        self.food_269 = pygame.Rect(110, 190, 5, 5)
        self.food_270 = pygame.Rect(150, 190, 5, 5)
        self.food_271 = pygame.Rect(200, 190, 5, 5)
        self.food_272 = pygame.Rect(290, 190, 5, 5)
        self.food_273 = pygame.Rect(380, 190, 5, 5)
        self.food_274 = pygame.Rect(490, 190, 5, 5)
        self.food_275 = pygame.Rect(530, 190, 5, 5)
        self.food_276 = pygame.Rect(640, 190, 5, 5)
        """ line 17 """
        self.food_277 = pygame.Rect(110, 200, 5, 5)
        self.food_278 = pygame.Rect(150, 200, 5, 5)
        self.food_279 = pygame.Rect(160, 200, 5, 5)
        self.food_280 = pygame.Rect(200, 200, 5, 5)
        self.food_281 = pygame.Rect(290, 200, 5, 5)
        self.food_282 = pygame.Rect(380, 200, 5, 5)
        self.food_283 = pygame.Rect(490, 200, 5, 5)
        self.food_284 = pygame.Rect(530, 200, 5, 5)
        self.food_285 = pygame.Rect(640, 200, 5, 5)
        """ line 18 """
        self.food_286 = pygame.Rect(110, 210, 5, 5)
        self.food_287 = pygame.Rect(150, 210, 5, 5)
        self.food_288 = pygame.Rect(160, 210, 5, 5)
        self.food_289 = pygame.Rect(200, 210, 5, 5)
        self.food_290 = pygame.Rect(290, 210, 5, 5)
        self.food_291 = pygame.Rect(380, 210, 5, 5)
        self.food_292 = pygame.Rect(490, 210, 5, 5)
        self.food_293 = pygame.Rect(530, 210, 5, 5)
        self.food_294 = pygame.Rect(640, 210, 5, 5)
        """ line 19 """
        self.food_295 = pygame.Rect(110, 220, 5, 5)
        self.food_296 = pygame.Rect(200, 220, 5, 5)
        self.food_297 = pygame.Rect(290, 220, 5, 5)
        self.food_298 = pygame.Rect(380, 220, 5, 5)
        self.food_299 = pygame.Rect(490, 220, 5, 5)
        self.food_300 = pygame.Rect(530, 220, 5, 5)
        self.food_301 = pygame.Rect(640, 220, 5, 5)
        """ line 20 """
        self.food_302 = pygame.Rect(20, 230, 5, 5)
        self.food_303 = pygame.Rect(30, 230, 5, 5)
        self.food_304 = pygame.Rect(40, 230, 5, 5)
        self.food_305 = pygame.Rect(50, 230, 5, 5)
        self.food_306 = pygame.Rect(60, 230, 5, 5)
        self.food_307 = pygame.Rect(70, 230, 5, 5)
        self.food_308 = pygame.Rect(80, 230, 5, 5)
        self.food_309 = pygame.Rect(90, 230, 5, 5)
        self.food_310 = pygame.Rect(100, 230, 5, 5)
        self.food_311 = pygame.Rect(110, 230, 5, 5)
        self.food_312 = pygame.Rect(200, 230, 5, 5)
        self.food_313 = pygame.Rect(290, 230, 5, 5)
        self.food_314 = pygame.Rect(380, 230, 5, 5)
        self.food_315 = pygame.Rect(490, 230, 5, 5)
        self.food_316 = pygame.Rect(530, 230, 5, 5)
        self.food_317 = pygame.Rect(640, 230, 5, 5)
        self.food_318 = pygame.Rect(650, 230, 5, 5)
        self.food_319 = pygame.Rect(660, 230, 5, 5)
        self.food_320 = pygame.Rect(670, 230, 5, 5)
        self.food_321 = pygame.Rect(680, 230, 5, 5)
        self.food_322 = pygame.Rect(690, 230, 5, 5)
        self.food_323 = pygame.Rect(700, 230, 5, 5)
        self.food_324 = pygame.Rect(710, 230, 5, 5)
        self.food_325 = pygame.Rect(720, 230, 5, 5)
        self.food_326 = pygame.Rect(730, 230, 5, 5)
        """ line 21 """
        self.food_327 = pygame.Rect(110, 230, 5, 5)
        self.food_328 = pygame.Rect(200, 230, 5, 5)
        self.food_329 = pygame.Rect(290, 230, 5, 5)
        self.food_330 = pygame.Rect(380, 230, 5, 5)
        self.food_331 = pygame.Rect(490, 230, 5, 5)
        self.food_332 = pygame.Rect(530, 230, 5, 5)
        self.food_333 = pygame.Rect(640, 230, 5, 5)
        """ line 22 """
        self.food_334 = pygame.Rect(110, 240, 5, 5)
        self.food_335 = pygame.Rect(200, 240, 5, 5)
        self.food_336 = pygame.Rect(290, 240, 5, 5)
        self.food_337 = pygame.Rect(380, 240, 5, 5)
        self.food_338 = pygame.Rect(490, 240, 5, 5)
        self.food_339 = pygame.Rect(530, 240, 5, 5)
        self.food_340 = pygame.Rect(640, 240, 5, 5)
        """ line 23 """
        self.food_341 = pygame.Rect(110, 250, 5, 5)
        self.food_342 = pygame.Rect(200, 250, 5, 5)
        self.food_343 = pygame.Rect(290, 250, 5, 5)
        self.food_344 = pygame.Rect(380, 250, 5, 5)
        self.food_345 = pygame.Rect(490, 250, 5, 5)
        self.food_346 = pygame.Rect(530, 250, 5, 5)
        self.food_347 = pygame.Rect(640, 250, 5, 5)
        """ line 24 """
        self.food_348 = pygame.Rect(110, 260, 5, 5)
        self.food_349 = pygame.Rect(200, 260, 5, 5)
        self.food_350 = pygame.Rect(290, 260, 5, 5)
        self.food_351 = pygame.Rect(380, 260, 5, 5)
        self.food_352 = pygame.Rect(490, 260, 5, 5)
        self.food_353 = pygame.Rect(530, 260, 5, 5)
        self.food_354 = pygame.Rect(640, 260, 5, 5)
        """ line 25 """
        self.food_355 = pygame.Rect(110, 270, 5, 5)
        self.food_356 = pygame.Rect(200, 270, 5, 5)
        self.food_357 = pygame.Rect(290, 270, 5, 5)
        self.food_358 = pygame.Rect(380, 270, 5, 5)
        self.food_359 = pygame.Rect(390, 270, 5, 5)
        self.food_360 = pygame.Rect(400, 270, 5, 5)
        self.food_361 = pygame.Rect(410, 270, 5, 5)
        self.food_362 = pygame.Rect(420, 270, 5, 5)
        self.food_363 = pygame.Rect(430, 270, 5, 5)
        self.food_364 = pygame.Rect(440, 270, 5, 5)
        self.food_365 = pygame.Rect(450, 270, 5, 5)
        self.food_366 = pygame.Rect(460, 270, 5, 5)
        self.food_367 = pygame.Rect(470, 270, 5, 5)
        self.food_368 = pygame.Rect(480, 270, 5, 5)
        self.food_369 = pygame.Rect(490, 270, 5, 5)
        self.food_370 = pygame.Rect(530, 270, 5, 5)
        self.food_371 = pygame.Rect(640, 270, 5, 5)
        """ line 26 """
        self.food_372 = pygame.Rect(110, 280, 5, 5)
        self.food_373 = pygame.Rect(200, 280, 5, 5)
        self.food_374 = pygame.Rect(290, 280, 5, 5)
        self.food_375 = pygame.Rect(380, 280, 5, 5)
        self.food_376 = pygame.Rect(490, 280, 5, 5)
        self.food_377 = pygame.Rect(530, 280, 5, 5)
        self.food_378 = pygame.Rect(640, 280, 5, 5)
        """ line 27 """
        self.food_379 = pygame.Rect(20, 290, 5, 5)
        self.food_380 = pygame.Rect(30, 290, 5, 5)
        self.food_381 = pygame.Rect(40, 290, 5, 5)
        self.food_382 = pygame.Rect(50, 290, 5, 5)
        self.food_383 = pygame.Rect(60, 290, 5, 5)
        self.food_384 = pygame.Rect(70, 290, 5, 5)
        self.food_385 = pygame.Rect(80, 290, 5, 5)
        self.food_386 = pygame.Rect(90, 290, 5, 5)
        self.food_387 = pygame.Rect(100, 290, 5, 5)
        self.food_388 = pygame.Rect(110, 290, 5, 5)
        self.food_389 = pygame.Rect(120, 290, 5, 5)
        self.food_390 = pygame.Rect(130, 290, 5, 5)
        self.food_391 = pygame.Rect(130, 290, 5, 5)
        self.food_392 = pygame.Rect(140, 290, 5, 5)
        self.food_393 = pygame.Rect(150, 290, 5, 5)
        self.food_394 = pygame.Rect(160, 290, 5, 5)
        self.food_395 = pygame.Rect(170, 290, 5, 5)
        self.food_396 = pygame.Rect(180, 290, 5, 5)
        self.food_397 = pygame.Rect(190, 290, 5, 5)
        self.food_398 = pygame.Rect(200, 290, 5, 5)
        self.food_399 = pygame.Rect(210, 290, 5, 5)
        self.food_400 = pygame.Rect(220, 290, 5, 5)
        self.food_401 = pygame.Rect(230, 290, 5, 5)
        self.food_402 = pygame.Rect(240, 290, 5, 5)
        self.food_403 = pygame.Rect(250, 290, 5, 5)
        self.food_404 = pygame.Rect(260, 290, 5, 5)
        self.food_405 = pygame.Rect(270, 290, 5, 5)
        self.food_406 = pygame.Rect(280, 290, 5, 5)
        self.food_407 = pygame.Rect(290, 290, 5, 5)
        self.food_408 = pygame.Rect(300, 290, 5, 5)
        self.food_409 = pygame.Rect(310, 290, 5, 5)
        self.food_410 = pygame.Rect(320, 290, 5, 5)
        self.food_411 = pygame.Rect(330, 290, 5, 5)
        self.food_412 = pygame.Rect(340, 290, 5, 5)
        self.food_413 = pygame.Rect(350, 290, 5, 5)
        self.food_414 = pygame.Rect(360, 290, 5, 5)
        self.food_415 = pygame.Rect(370, 290, 5, 5)
        self.food_416 = pygame.Rect(380, 290, 5, 5)
        self.food_417 = pygame.Rect(490, 290, 5, 5)
        self.food_418 = pygame.Rect(500, 290, 5, 5)
        self.food_419 = pygame.Rect(510, 290, 5, 5)
        self.food_420 = pygame.Rect(520, 290, 5, 5)
        self.food_421 = pygame.Rect(530, 290, 5, 5)
        self.food_422 = pygame.Rect(540, 290, 5, 5)
        self.food_423 = pygame.Rect(550, 290, 5, 5)
        self.food_424 = pygame.Rect(560, 290, 5, 5)
        self.food_425 = pygame.Rect(570, 290, 5, 5)
        self.food_426 = pygame.Rect(580, 290, 5, 5)
        self.food_427 = pygame.Rect(590, 290, 5, 5)
        self.food_428 = pygame.Rect(600, 290, 5, 5)
        self.food_429 = pygame.Rect(610, 290, 5, 5)
        self.food_430 = pygame.Rect(620, 290, 5, 5)
        self.food_431 = pygame.Rect(620, 290, 5, 5)
        self.food_432 = pygame.Rect(630, 290, 5, 5)
        self.food_433 = pygame.Rect(640, 290, 5, 5)
        self.food_434 = pygame.Rect(650, 290, 5, 5)
        self.food_435 = pygame.Rect(660, 290, 5, 5)
        self.food_436 = pygame.Rect(670, 290, 5, 5)
        self.food_437 = pygame.Rect(680, 290, 5, 5)
        self.food_438 = pygame.Rect(690, 290, 5, 5)
        self.food_439 = pygame.Rect(700, 290, 5, 5)
        self.food_440 = pygame.Rect(710, 290, 5, 5)
        self.food_441 = pygame.Rect(720, 290, 5, 5)
        self.food_442 = pygame.Rect(730, 290, 5, 5)
        """ line 28 """
        self.food_443 = pygame.Rect(20, 300, 5, 5)
        self.food_444 = pygame.Rect(120, 300, 5, 5)
        self.food_445 = pygame.Rect(220, 300, 5, 5)
        self.food_446 = pygame.Rect(260, 300, 5, 5)
        self.food_447 = pygame.Rect(370, 300, 5, 5)
        self.food_448 = pygame.Rect(380, 300, 5, 5)
        self.food_449 = pygame.Rect(490, 300, 5, 5)
        self.food_450 = pygame.Rect(500, 300, 5, 5)
        self.food_451 = pygame.Rect(630, 300, 5, 5)
        self.food_452 = pygame.Rect(730, 300, 5, 5)
        """ line 29 """
        self.food_453 = pygame.Rect(20, 310, 5, 5)
        self.food_454 = pygame.Rect(120, 310, 5, 5)
        self.food_455 = pygame.Rect(220, 310, 5, 5)
        self.food_456 = pygame.Rect(260, 310, 5, 5)
        self.food_457 = pygame.Rect(370, 310, 5, 5)
        self.food_458 = pygame.Rect(380, 310, 5, 5)
        self.food_459 = pygame.Rect(390, 310, 5, 5)
        self.food_460 = pygame.Rect(400, 310, 5, 5)
        self.food_461 = pygame.Rect(410, 310, 5, 5)
        self.food_462 = pygame.Rect(460, 310, 5, 5)
        self.food_463 = pygame.Rect(470, 310, 5, 5)
        self.food_464 = pygame.Rect(480, 310, 5, 5)
        self.food_465 = pygame.Rect(490, 310, 5, 5)
        self.food_466 = pygame.Rect(500, 310, 5, 5)
        self.food_467 = pygame.Rect(630, 310, 5, 5)
        self.food_468 = pygame.Rect(730, 310, 5, 5)
        """ line 30 """
        self.food_469 = pygame.Rect(20, 320, 5, 5)
        self.food_470 = pygame.Rect(120, 320, 5, 5)
        self.food_471 = pygame.Rect(220, 320, 5, 5)
        self.food_472 = pygame.Rect(260, 320, 5, 5)
        self.food_473 = pygame.Rect(370, 320, 5, 5)
        self.food_474 = pygame.Rect(410, 320, 5, 5)
        self.food_475 = pygame.Rect(460, 320, 5, 5)
        self.food_476 = pygame.Rect(500, 320, 5, 5)
        self.food_477 = pygame.Rect(630, 320, 5, 5)
        self.food_478 = pygame.Rect(730, 320, 5, 5)
        """ line 31 """
        self.food_479 = pygame.Rect(20, 330, 5, 5)
        self.food_480 = pygame.Rect(30, 330, 5, 5)
        self.food_481 = pygame.Rect(40, 330, 5, 5)
        self.food_482 = pygame.Rect(50, 330, 5, 5)
        self.food_483 = pygame.Rect(60, 330, 5, 5)
        self.food_484 = pygame.Rect(70, 330, 5, 5)
        self.food_485 = pygame.Rect(80, 330, 5, 5)
        self.food_486 = pygame.Rect(90, 330, 5, 5)
        self.food_487 = pygame.Rect(100, 330, 5, 5)
        self.food_488 = pygame.Rect(110, 330, 5, 5)
        self.food_489 = pygame.Rect(120, 330, 5, 5)
        self.food_490 = pygame.Rect(130, 330, 5, 5)
        self.food_491 = pygame.Rect(140, 330, 5, 5)
        self.food_492 = pygame.Rect(150, 330, 5, 5)
        self.food_493 = pygame.Rect(160, 330, 5, 5)
        self.food_494 = pygame.Rect(170, 330, 5, 5)
        self.food_495 = pygame.Rect(180, 330, 5, 5)
        self.food_496 = pygame.Rect(190, 330, 5, 5)
        self.food_497 = pygame.Rect(200, 330, 5, 5)
        self.food_498 = pygame.Rect(220, 330, 5, 5)
        self.food_499 = pygame.Rect(260, 330, 5, 5)
        self.food_500 = pygame.Rect(270, 330, 5, 5)
        self.food_501 = pygame.Rect(280, 330, 5, 5)
        self.food_502 = pygame.Rect(290, 330, 5, 5)
        self.food_503 = pygame.Rect(300, 330, 5, 5)
        self.food_504 = pygame.Rect(310, 330, 5, 5)
        self.food_505 = pygame.Rect(320, 330, 5, 5)
        self.food_506 = pygame.Rect(330, 330, 5, 5)
        self.food_507 = pygame.Rect(340, 330, 5, 5)
        self.food_508 = pygame.Rect(350, 330, 5, 5)
        self.food_509 = pygame.Rect(360, 330, 5, 5)
        self.food_510 = pygame.Rect(370, 330, 5, 5)
        self.food_511 = pygame.Rect(410, 330, 5, 5)
        self.food_512 = pygame.Rect(420, 330, 5, 5)
        self.food_513 = pygame.Rect(430, 330, 5, 5)
        self.food_514 = pygame.Rect(440, 330, 5, 5)
        self.food_515 = pygame.Rect(450, 330, 5, 5)
        self.food_516 = pygame.Rect(460, 330, 5, 5)
        self.food_517 = pygame.Rect(500, 330, 5, 5)
        self.food_518 = pygame.Rect(510, 330, 5, 5)
        self.food_519 = pygame.Rect(520, 330, 5, 5)
        self.food_520 = pygame.Rect(530, 330, 5, 5)
        self.food_521 = pygame.Rect(540, 330, 5, 5)
        self.food_522 = pygame.Rect(550, 330, 5, 5)
        self.food_523 = pygame.Rect(560, 330, 5, 5)
        self.food_524 = pygame.Rect(570, 330, 5, 5)
        self.food_525 = pygame.Rect(580, 330, 5, 5)
        self.food_526 = pygame.Rect(590, 330, 5, 5)
        self.food_527 = pygame.Rect(600, 330, 5, 5)
        self.food_528 = pygame.Rect(610, 330, 5, 5)
        self.food_529 = pygame.Rect(620, 330, 5, 5)
        self.food_530 = pygame.Rect(630, 330, 5, 5)
        self.food_531 = pygame.Rect(640, 330, 5, 5)
        self.food_532 = pygame.Rect(650, 330, 5, 5)
        self.food_533 = pygame.Rect(660, 330, 5, 5)
        self.food_534 = pygame.Rect(670, 330, 5, 5)
        self.food_535 = pygame.Rect(680, 330, 5, 5)
        self.food_536 = pygame.Rect(690, 330, 5, 5)
        self.food_537 = pygame.Rect(700, 330, 5, 5)
        self.food_538 = pygame.Rect(710, 330, 5, 5)
        self.food_539 = pygame.Rect(720, 330, 5, 5)
        self.food_540 = pygame.Rect(730, 330, 5, 5)

        """ inside WordE """
        self.food_541 = pygame.Rect(590, 190, 5, 5)
        self.food_542 = pygame.Rect(600, 190, 5, 5)
        self.food_543 = pygame.Rect(610, 190, 5, 5)
        self.food_544 = pygame.Rect(620, 190, 5, 5)
        self.food_545 = pygame.Rect(630, 190, 5, 5)
        """ right corner RightMidTop"""
        self.food_546 = pygame.Rect(650, 120, 5, 5)
        self.food_547 = pygame.Rect(660, 120, 5, 5)
        self.food_548 = pygame.Rect(670, 120, 5, 5)
        self.food_549 = pygame.Rect(680, 120, 5, 5)
        self.food_550 = pygame.Rect(690, 120, 5, 5)
        self.food_551 = pygame.Rect(700, 120, 5, 5)
        self.food_552 = pygame.Rect(710, 120, 5, 5)
        self.food_553 = pygame.Rect(720, 120, 5, 5)
        self.food_554 = pygame.Rect(730, 120, 5, 5)
        """ I left this at bottom line 31"""
        self.food_555 = pygame.Rect(210, 330, 5, 5)

        self.line_2_and_3_and_4_foodItems = [self.food_73, self.food_74, self.food_75, self.food_76, self.food_77, self.food_78, self.food_79, self.food_80, self.food_81, self.food_82, self.food_83,
                                             self.food_84, self.food_85, self.food_86, self.food_87, self.food_88, self.food_89, self.food_90, self.food_91, self.food_92, self.food_93, self.food_94,
                                             self.food_95, self.food_96, self.food_97, self.food_98, self.food_99, self.food_100, self.food_101, self.food_102, self.food_103, self.food_104,
                                             self.food_105, self.food_106, self.food_107, self.food_108, self.food_109, self.food_110, self.food_111, self.food_112, self.food_113, self.food_114,
                                             self.food_115, self.food_116, self.food_117, self.food_118, self.food_119, self.food_120, self.food_121, self.food_122, self.food_123, self.food_124,
                                             self.food_125, self.food_126, self.food_127, self.food_128, self.food_129, self.food_130, self.food_131, self.food_132, self.food_133, self.food_134,
                                             self.food_135, self.food_136, self.food_137, self.food_138, self.food_139, self.food_140, self.food_141, self.food_142, self.food_143, self.food_144,
                                             self.food_145, self.food_146, self.food_147, self.food_148, self.food_149, self.food_150, self.food_151, self.food_152, self.food_153, self.food_154,
                                             self.food_155, self.food_156, self.food_157, self.food_158, self.food_159, self.food_160, self.food_161, self.food_162, self.food_163, self.food_164,
                                             self.food_165, self.food_166, self.food_167, self.food_168, self.food_169, self.food_170, self.food_171, self.food_172, self.food_173, self.food_174,
                                             self.food_175, self.food_176, self.food_177, self.food_178, self.food_179, self.food_180, self.food_181, self.food_182, self.food_183, self.food_184,
                                             self.food_185, self.food_186, self.food_187, self.food_188, self.food_189, self.food_190, self.food_191, self.food_192, self.food_193, self.food_194,
                                             self.food_195, self.food_196, self.food_197, self.food_198, self.food_199, self.food_200, self.food_201, self.food_202, self.food_203, self.food_204,
                                             self.food_205, self.food_206, self.food_207, self.food_208, self.food_209, self.food_210, self.food_211, self.food_212, self.food_213, self.food_214,
                                             self.food_215, self.food_216, self.food_217, self.food_218, self.food_219, self.food_220, self.food_221, self.food_222, self.food_223, self.food_224,
                                             self.food_225, self.food_226, self.food_227, self.food_228, self.food_229, self.food_230, self.food_230, self.food_231, self.food_232, self.food_233,
                                             self.food_234, self.food_235, self.food_236, self.food_237, self.food_238, self.food_239, self.food_240, self.food_241, self.food_242, self.food_243,
                                             self.food_244, self.food_245, self.food_246, self.food_247, self.food_248, self.food_249, self.food_250, self.food_251, self.food_252, self.food_253,
                                             self.food_254, self.food_255, self.food_256, self.food_257, self.food_258, self.food_259, self.food_260, self.food_261, self.food_262, self.food_263,
                                             self.food_264, self.food_265, self.food_266, self.food_267, self.food_268, self.food_269, self.food_270, self.food_271, self.food_272, self.food_273,
                                             self.food_274, self.food_275, self.food_276, self.food_277, self.food_278, self.food_279, self.food_280, self.food_281, self.food_282, self.food_283,
                                             self.food_284, self.food_285, self.food_286, self.food_287, self.food_288, self.food_289, self.food_290, self.food_291, self.food_292, self.food_293,
                                             self.food_294, self.food_295, self.food_296, self.food_297, self.food_298, self.food_299, self.food_300, self.food_301, self.food_302, self.food_303,
                                             self.food_304, self.food_305, self.food_306, self.food_307, self.food_308, self.food_309, self.food_310, self.food_311, self.food_312, self.food_313,
                                             self.food_314, self.food_315, self.food_316, self.food_317, self.food_318, self.food_319, self.food_320, self.food_321, self.food_322, self.food_323,
                                             self.food_324, self.food_325, self.food_326, self.food_326, self.food_327, self.food_328, self.food_329, self.food_331, self.food_332, self.food_333,
                                             self.food_334, self.food_335, self.food_336, self.food_337, self.food_338, self.food_339, self.food_340, self.food_341, self.food_342, self.food_343,
                                             self.food_344, self.food_345, self.food_346, self.food_347, self.food_348, self.food_349, self.food_350, self.food_351, self.food_352, self.food_353,
                                             self.food_354, self.food_355, self.food_356, self.food_357, self.food_358, self.food_359, self.food_360, self.food_361, self.food_362, self.food_363,
                                             self.food_364, self.food_365, self.food_366, self.food_367, self.food_368, self.food_369, self.food_370, self.food_371, self.food_372, self.food_373,
                                             self.food_374, self.food_375, self.food_376, self.food_377, self.food_378, self.food_379, self.food_380, self.food_381, self.food_382, self.food_383,
                                             self.food_384, self.food_385, self.food_386, self.food_387, self.food_388, self.food_389, self.food_390, self.food_391, self.food_392, self.food_393,
                                             self.food_394, self.food_395, self.food_396, self.food_397, self.food_398, self.food_399, self.food_400, self.food_401, self.food_402, self.food_403,
                                             self.food_404, self.food_405, self.food_406, self.food_407, self.food_408, self.food_409, self.food_410, self.food_411, self.food_412, self.food_413,
                                             self.food_414, self.food_415, self.food_416, self.food_417, self.food_418, self.food_419, self.food_420, self.food_421, self.food_422, self.food_423,
                                             self.food_424, self.food_425, self.food_426, self.food_427, self.food_428, self.food_429, self.food_430, self.food_431, self.food_432, self.food_433,
                                             self.food_434, self.food_435, self.food_436, self.food_437, self.food_438, self.food_439, self.food_440, self.food_441, self.food_442, self.food_443,
                                             self.food_444, self.food_445, self.food_446, self.food_447, self.food_448, self.food_449, self.food_450, self.food_451, self.food_452, self.food_453,
                                             self.food_454, self.food_455, self.food_456, self.food_457, self.food_458, self.food_459, self.food_460, self.food_461, self.food_462, self.food_463,
                                             self.food_464, self.food_465, self.food_466, self.food_467, self.food_468, self.food_469, self.food_470, self.food_471, self.food_472, self.food_473,
                                             self.food_474, self.food_475, self.food_476, self.food_477, self.food_478, self.food_479, self.food_480, self.food_481, self.food_482, self.food_483,
                                             self.food_484, self.food_485, self.food_486, self.food_487, self.food_488, self.food_489, self.food_490, self.food_491, self.food_492, self.food_493,
                                             self.food_494, self.food_495, self.food_496, self.food_497, self.food_498, self.food_499, self.food_500, self.food_501, self.food_502, self.food_503,
                                             self.food_504, self.food_505, self.food_506, self.food_507, self.food_508, self.food_509, self.food_510, self.food_511, self.food_512, self.food_513,
                                             self.food_514, self.food_515, self.food_516, self.food_517, self.food_518, self.food_519, self.food_520, self.food_521, self.food_522, self.food_523,
                                             self.food_524, self.food_525, self.food_526, self.food_527, self.food_528, self.food_529, self.food_530, self.food_531, self.food_532, self.food_533,
                                             self.food_534, self.food_535, self.food_536, self.food_537, self.food_538, self.food_539, self.food_540, self.food_541, self.food_542, self.food_543,
                                             self.food_544, self.food_545, self.food_546, self.food_547, self.food_548, self.food_549, self.food_550, self.food_551, self.food_552, self.food_553,
                                             self.food_554, self.food_555]
        for itemNum in range(0, len(self.line_2_and_3_and_4_foodItems)):
            self.foodPosLst.append(self.line_2_and_3_and_4_foodItems[itemNum])


class GameWindow(GameVariables, Food):
    def __init__(self):
        super().__init__()
        self.run = True
        self.t = 0

    def drawGrid(self):
        for i in range(0, self.winWidth, 10):
            pygame.draw.line(self.window, self.red, (i, 0),
                             (i, self.winHeight), 1)
        for j in range(0, self.winHeight, 10):
            pygame.draw.line(self.window, self.red,
                             (0, j), (self.winWidth, j), 1)

    def drawPlayer(self):
        # self.window.blit(pygame.transform.scale(pygame.image.load("img/pacmanAssets/pacmanRight.png"), (self.playerRect.width, self.playerRect.height)), (self.playerRect.x, self.playerRect.y))
        # pygame.draw.circle(self.window, self.yellow, (self.playerRect.x + (self.playerRect.width // 2), self.playerRect.y + (self.playerRect.height // 2)), self.playerRect.width // 2)
        # pygame.draw.rect(self.window, self.green, self.playerRect, 1)

        if self.moveLeft:
            self.playerRect.x -= self.playerVel
            if self.walkCount >= 18:
                self.walkCount = 0
            self.window.blit(
                self.pacmanMoveLeftImgLst[self.walkCount // 3], (self.playerRect.x, self.playerRect.y))
            self.walkCount += 1
        elif self.moveRight:
            self.playerRect.x += self.playerVel
            if self.walkCount >= 18:
                self.walkCount = 0
            self.window.blit(
                self.pacmanMoveRightImgLst[self.walkCount // 3], (self.playerRect.x, self.playerRect.y))
            self.walkCount += 1
        elif self.moveUp:
            self.playerRect.y -= self.playerVel
            if self.walkCount >= 18:
                self.walkCount = 0
            self.window.blit(
                self.pacmanMoveUpImgLst[self.walkCount // 3], (self.playerRect.x, self.playerRect.y))
            self.walkCount += 1
        elif self.moveDown:
            self.playerRect.y += self.playerVel
            if self.walkCount >= 18:
                self.walkCount = 0
            self.window.blit(
                self.pacmanMoveDownImgLst[self.walkCount // 3], (self.playerRect.x, self.playerRect.y))
            self.walkCount += 1
        elif not (self.moveUp and self.moveDown and self.moveRight and self.moveLeft):
            self.window.blit(
                self.pacmanMoveRightImgLst[0], (self.playerRect.x, self.playerRect.y))

    def drawGhost(self):
        self.window.blit(self.ghostImg['redRight'],
                         (self.redGhostRect.x, self.redGhostRect.y))
        pygame.draw.rect(self.window, self.red, (self.redGhostRect.x,
                         self.redGhostRect.y, self.ghostSize, self.ghostSize))
        self.window.blit(
            self.ghostImg['orangeRight'], (self.orangeGhostRect.x, self.orangeGhostRect.y))
        self.window.blit(self.ghostImg['blueRight'],
                         (self.blueGhostRect.x, self.blueGhostRect.y))
        self.window.blit(self.ghostImg['pinkRight'],
                         (self.pinkGhostRect.x, self.pinkGhostRect.y))

    def drawLayout(self):
        pygame.draw.rect(self.window, self.aqua, self.topRect)

        pygame.draw.rect(self.window, self.aqua, self.leftTopRect)

        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopLeft_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopLeft_left)
        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopLeft_right)
        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopLeft_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopLeft_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopLeft_left)
        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopLeft_right)
        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopLeft_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle3TopLeft_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle3TopLeft_left)
        pygame.draw.rect(self.window, self.aqua, self.obstacle3TopLeft_right)
        pygame.draw.rect(self.window, self.aqua, self.obstacle3TopLeft_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopRight_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopRight_left)
        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopRight_right)
        pygame.draw.rect(self.window, self.aqua, self.obstacle2TopRight_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopRight_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopRight_left)
        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopRight_right)
        pygame.draw.rect(self.window, self.aqua, self.obstacle1TopRight_bottom)

        pygame.draw.rect(self.window, self.yellow, self.WordGTop)
        pygame.draw.rect(self.window, self.yellow, self.WordGTopInside)
        pygame.draw.rect(self.window, self.green, self.WordGLeft)
        pygame.draw.rect(self.window, self.yellow, self.WordGLeftInside)
        pygame.draw.rect(self.window, self.yellow, self.WordGCurveTop)
        pygame.draw.rect(self.window, self.yellow, self.WordGCurveLeft)
        pygame.draw.rect(self.window, self.yellow, self.WordGCurveBottom)
        pygame.draw.rect(self.window, self.green, self.WordGRight1)
        pygame.draw.rect(self.window, self.green, self.WordGRight2)
        pygame.draw.rect(self.window, self.yellow, self.WordGRight2Inside)
        pygame.draw.rect(self.window, self.yellow, self.WordGBottomInside)
        pygame.draw.rect(self.window, self.yellow, self.WordGBottom)

        pygame.draw.rect(self.window, self.yellow, self.WordO1Top)
        pygame.draw.rect(self.window, self.green, self.WordO1Left)
        pygame.draw.rect(self.window, self.yellow,
                         (self.WordO1Left.x + 30, self.WordO1Top.y + 90, 10, 20))
        pygame.draw.rect(self.window, self.green, self.WordO1Right)
        pygame.draw.rect(self.window, self.yellow, self.WordO1Bottom)

        pygame.draw.rect(self.window, self.yellow, self.WordO2Top)
        pygame.draw.rect(self.window, self.green, self.WordO2Left)
        pygame.draw.rect(self.window, self.yellow,
                         (self.WordO2Left.x + 30, self.WordO2Top.y + 90, 10, 20))
        pygame.draw.rect(self.window, self.green, self.WordO2Right)
        pygame.draw.rect(self.window, self.yellow, self.WordO2Bottom)

        pygame.draw.rect(self.window, self.green, self.enemyContainerTop1_G)
        pygame.draw.rect(self.window, self.green,
                         self.enemyContainerTop1Inside_G)
        pygame.draw.line(self.window, self.white, (self.enemyContainerTop1Inside_G.x + self.enemyContainerTop1Inside_G.width, self.enemyContainerTop1Inside_G.y +
                                                   self.enemyContainerTop1Inside_G.height),
                         (self.enemyContainerTop2Inside_G.x, self.enemyContainerTop2Inside_G.y + self.enemyContainerTop2Inside_G.height))
        pygame.draw.rect(self.window, self.green, self.enemyContainerTop2_G)
        pygame.draw.rect(self.window, self.green,
                         self.enemyContainerTop2Inside_G)
        pygame.draw.rect(self.window, self.yellow, self.enemyContainerLeft_G)
        pygame.draw.rect(self.window, self.green,
                         self.enemyContainerLeftInside_G)
        pygame.draw.rect(self.window, self.yellow, self.enemyContainerRight_G)
        pygame.draw.rect(self.window, self.green,
                         self.enemyContainerRightInside_G)
        pygame.draw.rect(self.window, self.green,
                         self.enemyContainerBottomInside_G)
        pygame.draw.rect(self.window, self.green, self.enemyContainerBottom_G)
        pygame.draw.rect(self.window, self.yellow, self.obstacle_GTopLeft)
        pygame.draw.rect(self.window, self.yellow, self.obstacle_G)
        pygame.draw.rect(self.window, self.yellow, self.obstacle_GTopBottom)
        pygame.draw.rect(self.window, self.yellow, self.obstacle_GTopRight)
        pygame.draw.rect(self.window, self.green, self.obstacle_GLeft_top)
        pygame.draw.rect(self.window, self.green, self.obstacle_GLeft_left)
        pygame.draw.rect(self.window, self.green, self.obstacle_GLeft_right)
        pygame.draw.rect(self.window, self.green, self.obstacle_GRight_top)
        pygame.draw.rect(self.window, self.green, self.obstacle_GRight_left)
        pygame.draw.rect(self.window, self.green, self.obstacle_GRight_right)
        pygame.draw.rect(self.window, self.green, self.obstacle_GBottomLeft)
        pygame.draw.rect(self.window, self.green, self.obstacle_GBottom)
        pygame.draw.rect(self.window, self.green, self.obstacle_GBottomRight)

        pygame.draw.rect(self.window, self.green, self.WordLTop)
        pygame.draw.rect(self.window, self.green, self.WordLLeft)
        pygame.draw.rect(self.window, self.yellow, self.WordLRight)
        pygame.draw.rect(self.window, self.yellow, self.WordLBottom)

        pygame.draw.rect(self.window, self.green, self.WordETop)
        pygame.draw.rect(self.window, self.green,
                         (self.WordEMidLeft.x, self.WordETop.y + 30, 30, 20))
        pygame.draw.rect(self.window, self.yellow, self.WordELeft)
        pygame.draw.rect(self.window, self.green, self.WordEMidTop)
        pygame.draw.rect(self.window, self.green, self.WordEMidBottom)
        pygame.draw.rect(self.window, self.yellow, self.WordEMidLeft)
        pygame.draw.rect(self.window, self.yellow, self.WordERight1)
        pygame.draw.rect(self.window, self.yellow, self.WordERight2)
        pygame.draw.rect(self.window, self.green, self.WordEBottom)

        pygame.draw.rect(self.window, self.aqua, self.leftMidTop1Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidTop2Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidTop3Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidTop4Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidTop5Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidTop6Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidBottom6Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidBottom5Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidBottom4Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidBottom3Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidBottom2Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftMidBottom1Rect)
        pygame.draw.rect(self.window, self.aqua, self.leftBottomRect)

        pygame.draw.rect(self.window, self.aqua, self.rightTopRect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidTop1Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidTop2Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidTop3Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidTop4Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidTop5Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidTop6Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidBottom6Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidBottom5Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidBottom4Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidBottom3Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidBottom2Rect)
        pygame.draw.rect(self.window, self.aqua, self.rightMidBottom1Rect)

        pygame.draw.rect(self.window, self.aqua, self.obstacle1BottomLeft_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle1BottomLeft_left)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle1BottomLeft_right)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle1BottomLeft_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle2BottomLeft_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle2BottomLeft_left)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle2BottomLeft_right)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle2BottomLeft_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle3BottomLeft_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle3BottomLeft_left)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle3BottomLeft_right)

        pygame.draw.rect(self.window, self.aqua, self.obstacle4BottomLeft_top)
        pygame.draw.rect(self.window, self.aqua, self.obstacle4BottomLeft_left)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle4BottomLeft_right)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle4BottomLeft_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle2BottomRight_top)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle2BottomRight_left)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle2BottomRight_right)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle2BottomRight_bottom)

        pygame.draw.rect(self.window, self.aqua, self.obstacle1BottomRight_top)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle1BottomRight_left)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle1BottomRight_right)
        pygame.draw.rect(self.window, self.aqua,
                         self.obstacle1BottomRight_bottom)

        pygame.draw.rect(self.window, self.aqua, self.rightBottomRect)

        pygame.draw.rect(self.window, self.aqua, self.bottomRect)

    def writeNamesOfObjects(self):
        messageLst = ["topRect",
                      "leftTopRect",
                      "obstacle1TopLeft_top",
                      "obstacle1TopLeft_left",
                      "obstacle1TopLeft_right",
                      "obstacle1TopLeft_bottom",
                      "obstacle2TopLeft_top",
                      "obstacle2TopLeft_left",
                      "obstacle2TopLeft_right",
                      "obstacle2TopLeft_bottom",
                      "obstacle3TopLeft_top",
                      "obstacle3TopLeft_left",
                      "obstacle3TopLeft_right",
                      "obstacle3TopLeft_bottom",
                      "obstacle2TopRight_top",
                      "obstacle2TopRight_left",
                      "obstacle2TopRight_right",
                      "obstacle2TopRight_bottom",
                      "obstacle1TopRight_top",
                      "obstacle1TopRight_left",
                      "obstacle1TopRight_right",
                      "obstacle1TopRight_bottom",
                      "WordGTop",
                      "WordGTopInside",
                      "WordGLeft",
                      "WordGLeftInside",
                      "WordGCurveTop",
                      "WordGCurveLeft",
                      "WordGCurveBottom",
                      "WordGRight1",
                      "WordGRight2",
                      "WordGRight2Inside",
                      "WordGBottom",
                      "WordGBottomInside",
                      "WordO1Top",
                      "WordO1Left",
                      "WordO1Right",
                      "WordO1Bottom",
                      "WordO2Top",
                      "WordO2Left",
                      "WordO2Right",
                      "WordO2Bottom",
                      "enemyContainerTop1_G",
                      "enemyContainerTop1Inside_G",
                      "enemyContainerTop2_G",
                      "enemyContainerTop2Inside_G",
                      "enemyContainerLeft_G",
                      "enemyContainerLeftInside_G",
                      "enemyContainerRight_G",
                      "enemyContainerRightInside_G",
                      "enemyContainerBottom_G",
                      "enemyContainerBottomInside_G",
                      "obstacle_GTopLeft",
                      "obstacle_G",
                      "obstacle_GTopBottom",
                      "obstacle_GTopRight",
                      "obstacle_GLeft_top",
                      "obstacle_GLeft_left",
                      "obstacle_GLeft_right",
                      "obstacle_GRight_top",
                      "obstacle_GRight_left",
                      "obstacle_GRight_right",
                      "obstacle_GBottomLeft",
                      "obstacle_GBottom",
                      "obstacle_GBottomRight",
                      "wordLTop",
                      "wordLLeft",
                      "wordLRight",
                      "wordLBottom",
                      "wordEtop",
                      "wordELeft",
                      "wordEMidTop",
                      "wordEMidBottom",
                      "wordEMidLeft",
                      "wordEMidRight1",
                      "wordEMidRight1",
                      "wordEMidRight2",
                      "wordEBottom",
                      "leftMidTop1Rect",
                      "leftMidTop2Rect",
                      "leftMidTop3Rect",
                      "leftMidTop4Rect",
                      "leftMidTop5Rect",
                      "leftMidTop6Rect",
                      "leftMidBottom6Rect",
                      "leftMidBottom5Rect",
                      "leftMidBottom4Rect",
                      "leftMidBottom3Rect",
                      "leftMidBottom2Rect",
                      "leftMidBottom1Rect",
                      "leftBottomRect",
                      "rightTopRect",
                      "rightMidTop1Rect",
                      "rightMidTop2Rect",
                      "rightMidTop3Rect",
                      "rightMidTop4Rect",
                      "rightMidTop5Rect",
                      "rightMidTop6Rect",
                      "rightMidBottom6Rect",
                      "rightMidBottom5Rect",
                      "rightMidBottom4Rect",
                      "rightMidBottom3Rect",
                      "rightMidBottom2Rect",
                      "rightMidBottom1Rect",
                      "obstacle1BottomLeft_top",
                      "obstacle1BottomLeft_left",
                      "obstacle1BottomLeft_right",
                      "obstacle1BottomLeft_bottom",
                      "obstacle2BottomLeft_top",
                      "obstacle2BottomLeft_left",
                      "obstacle2BottomLeft_right",
                      "obstacle2BottomLeft_bottom",
                      "obstacle3BottomLeft_top",
                      "obstacle3BottomLeft_left",
                      "obstacle3BottomLeft_right",
                      "obstacle4BottomLeft_top",
                      "obstacle4BottomLeft_left",
                      "obstacle4BottomLeft_right",
                      "obstacle4BottomLeft_bottom",
                      "obstacle2BottomRight_top",
                      "obstacle2BottomRight_left",
                      "obstacle2BottomRight_right",
                      "obstacle2BottomRight_bottom",
                      "obstacle1BottomRight_top",
                      "obstacle1BottomRight_left",
                      "obstacle1BottomRight_right",
                      "obstacle1BottomRight_bottom",
                      "rightBottomRect",
                      "bottomRect"]
        messagePosLst = [(self.topRect.x, self.topRect.y),
                         (self.leftTopRect.x, self.leftTopRect.y),
                         (self.obstacle1TopLeft_top.x,
                          self.obstacle1TopLeft_top.y),
                         (self.obstacle1TopLeft_left.x,
                          self.obstacle1TopLeft_left.y),
                         (self.obstacle1TopLeft_right.x,
                          self.obstacle1TopLeft_right.y),
                         (self.obstacle1TopLeft_bottom.x,
                          self.obstacle1TopLeft_bottom.y),
                         (self.obstacle2TopLeft_top.x,
                          self.obstacle2TopLeft_top.y),
                         (self.obstacle2TopLeft_left.x,
                          self.obstacle2TopLeft_left.y),
                         (self.obstacle2TopLeft_right.x,
                          self.obstacle2TopLeft_right.y),
                         (self.obstacle2TopLeft_bottom.x,
                          self.obstacle2TopLeft_bottom.y),
                         (self.obstacle3TopLeft_top.x,
                          self.obstacle3TopLeft_top.y),
                         (self.obstacle3TopLeft_left.x,
                          self.obstacle3TopLeft_left.y),
                         (self.obstacle3TopLeft_right.x,
                          self.obstacle3TopLeft_right.y),
                         (self.obstacle3TopLeft_bottom.x,
                          self.obstacle3TopLeft_bottom.y),
                         (self.obstacle2TopRight_top.x,
                          self.obstacle2TopRight_top.y),
                         (self.obstacle2TopRight_left.x,
                          self.obstacle2TopRight_left.y),
                         (self.obstacle2TopRight_right.x,
                          self.obstacle2TopRight_right.y),
                         (self.obstacle2TopRight_bottom.x,
                          self.obstacle2TopRight_bottom.y),
                         (self.obstacle1TopRight_top.x,
                          self.obstacle1TopRight_top.y),
                         (self.obstacle1TopRight_left.x,
                          self.obstacle1TopRight_left.y),
                         (self.obstacle1TopRight_right.x,
                          self.obstacle1TopRight_right.y),
                         (self.obstacle1TopRight_bottom.x,
                          self.obstacle1TopRight_bottom.y),
                         (self.WordGTop.x, self.WordGTop.y),
                         (self.WordGTopInside.x, self.WordGTopInside.y),
                         (self.WordGLeft.x, self.WordGLeft.y),
                         (self.WordGLeftInside.x, self.WordGLeftInside.y),
                         (self.WordGCurveTop.x, self.WordGCurveTop.y),
                         (self.WordGCurveLeft.x, self.WordGCurveLeft.y),
                         (self.WordGCurveBottom.x, self.WordGCurveBottom.y),
                         (self.WordGRight1.x, self.WordGRight1.y),
                         (self.WordGRight2.x, self.WordGRight2.y),
                         (self.WordGRight2Inside.x, self.WordGRight2Inside.y),
                         (self.WordGBottom.x, self.WordGBottom.y),
                         (self.WordGBottomInside.x, self.WordGBottomInside.y),
                         (self.WordO1Top.x, self.WordO1Top.y),
                         (self.WordO1Left.x, self.WordO1Left.y),
                         (self.WordO1Right.x, self.WordO1Right.y),
                         (self.WordO1Bottom.x, self.WordO1Bottom.y),
                         (self.WordO2Top.x, self.WordO2Top.y),
                         (self.WordO2Left.x, self.WordO2Left.y),
                         (self.WordO2Right.x, self.WordO2Right.y),
                         (self.WordO2Bottom.x, self.WordO2Bottom.y),
                         (self.enemyContainerTop1_G.x,
                          self.enemyContainerTop1_G.y),
                         (self.enemyContainerTop1Inside_G.x,
                          self.enemyContainerTop1Inside_G.y),
                         (self.enemyContainerTop2_G.x,
                          self.enemyContainerTop2_G.y),
                         (self.enemyContainerTop2Inside_G.x,
                          self.enemyContainerTop2Inside_G.y),
                         (self.enemyContainerLeft_G.x,
                          self.enemyContainerLeft_G.y),
                         (self.enemyContainerLeftInside_G.x,
                          self.enemyContainerLeftInside_G.y),
                         (self.enemyContainerRight_G.x,
                          self.enemyContainerRight_G.y),
                         (self.enemyContainerRightInside_G.x,
                          self.enemyContainerRightInside_G.y),
                         (self.enemyContainerBottom_G.x,
                          self.enemyContainerBottom_G.y),
                         (self.enemyContainerBottomInside_G.x,
                          self.enemyContainerBottomInside_G.y),
                         (self.obstacle_GTopLeft.x, self.obstacle_GTopLeft.y),
                         (self.obstacle_G.x, self.obstacle_G.y),
                         (self.obstacle_GTopBottom.x, self.obstacle_GTopBottom.y),
                         (self.obstacle_GTopRight.x, self.obstacle_GTopRight.y),
                         (self.obstacle_GLeft_top.x, self.obstacle_GLeft_top.y),
                         (self.obstacle_GLeft_left.x, self.obstacle_GLeft_left.y),
                         (self.obstacle_GLeft_right.x,
                          self.obstacle_GLeft_right.y),
                         (self.obstacle_GRight_top.x, self.obstacle_GRight_top.y),
                         (self.obstacle_GRight_left.x,
                          self.obstacle_GRight_left.y),
                         (self.obstacle_GRight_right.x,
                          self.obstacle_GRight_right.y),
                         (self.obstacle_GBottomLeft.x,
                          self.obstacle_GBottomLeft.y),
                         (self.obstacle_GBottom.x, self.obstacle_GBottom.y),
                         (self.obstacle_GBottomRight.x,
                          self.obstacle_GBottomRight.y),
                         (self.WordLTop.x, self.WordLTop.y),
                         (self.WordLLeft.x, self.WordLLeft.y),
                         (self.WordLRight.x, self.WordLRight.y),
                         (self.WordLBottom.x, self.WordLBottom.y),
                         (self.WordETop.x, self.WordETop.y),
                         (self.WordELeft.x, self.WordELeft.y),
                         (self.WordEMidTop.x, self.WordEMidTop.y),
                         (self.WordEMidBottom.x, self.WordEMidBottom.y),
                         (self.WordEMidLeft.x, self.WordEMidLeft.y),
                         (self.WordERight1.x, self.WordERight1.y),
                         (self.WordERight2.x, self.WordERight2.y),
                         (self.WordEBottom.x, self.WordEBottom.y),
                         (self.leftMidTop1Rect.x, self.leftMidTop1Rect.y),
                         (self.leftMidTop2Rect.x, self.leftMidTop2Rect.y),
                         (self.leftMidTop3Rect.x, self.leftMidTop3Rect.y),
                         (self.leftMidTop4Rect.x, self.leftMidTop4Rect.y),
                         (self.leftMidTop5Rect.x, self.leftMidTop5Rect.y),
                         (self.leftMidTop6Rect.x, self.leftMidTop6Rect.y),
                         (self.leftMidBottom6Rect.x, self.leftMidBottom6Rect.y),
                         (self.leftMidBottom5Rect.x, self.leftMidBottom5Rect.y),
                         (self.leftMidBottom4Rect.x, self.leftMidBottom4Rect.y),
                         (self.leftMidBottom3Rect.x, self.leftMidBottom3Rect.y),
                         (self.leftMidBottom2Rect.x, self.leftMidBottom2Rect.y),
                         (self.leftMidBottom1Rect.x, self.leftMidBottom1Rect.y),
                         (self.leftBottomRect.x, self.leftBottomRect.y),
                         (self.rightTopRect.x, self.rightTopRect.y),
                         (self.rightMidTop1Rect.x, self.rightMidTop1Rect.y),
                         (self.rightMidTop2Rect.x, self.rightMidTop2Rect.y),
                         (self.rightMidTop3Rect.x, self.rightMidTop3Rect.y),
                         (self.rightMidTop4Rect.x, self.rightMidTop4Rect.y),
                         (self.rightMidTop5Rect.x, self.rightMidTop5Rect.y),
                         (self.rightMidTop6Rect.x, self.rightMidTop6Rect.y),
                         (self.rightMidBottom6Rect.x, self.rightMidBottom6Rect.y),
                         (self.rightMidBottom5Rect.x, self.rightMidBottom5Rect.y),
                         (self.rightMidBottom4Rect.x, self.rightMidBottom4Rect.y),
                         (self.rightMidBottom3Rect.x, self.rightMidBottom3Rect.y),
                         (self.rightMidBottom2Rect.x, self.rightMidBottom2Rect.y),
                         (self.rightMidBottom1Rect.x, self.rightMidBottom1Rect.y),
                         (self.obstacle1BottomLeft_top.x,
                          self.obstacle1BottomLeft_top.y),
                         (self.obstacle1BottomLeft_left.x,
                          self.obstacle1BottomLeft_left.y),
                         (self.obstacle1BottomLeft_right.x,
                          self.obstacle1BottomLeft_right.y),
                         (self.obstacle1BottomLeft_bottom.x,
                          self.obstacle1BottomLeft_bottom.y),
                         (self.obstacle2BottomLeft_top.x,
                          self.obstacle2BottomLeft_top.y),
                         (self.obstacle2BottomLeft_left.x,
                          self.obstacle2BottomLeft_left.y),
                         (self.obstacle2BottomLeft_right.x,
                          self.obstacle2BottomLeft_right.y),
                         (self.obstacle2BottomLeft_bottom.x,
                          self.obstacle2BottomLeft_bottom.y),
                         (self.obstacle3BottomLeft_top.x,
                          self.obstacle3BottomLeft_top.y),
                         (self.obstacle3BottomLeft_left.x,
                          self.obstacle3BottomLeft_left.y),
                         (self.obstacle3BottomLeft_right.x,
                          self.obstacle3BottomLeft_right.y),
                         (self.obstacle4BottomLeft_top.x,
                          self.obstacle4BottomLeft_top.y),
                         (self.obstacle4BottomLeft_left.x,
                          self.obstacle4BottomLeft_left.y),
                         (self.obstacle4BottomLeft_right.x,
                          self.obstacle4BottomLeft_right.y),
                         (self.obstacle4BottomLeft_bottom.x,
                          self.obstacle4BottomLeft_bottom.y),
                         (self.obstacle2BottomRight_top.x,
                          self.obstacle2BottomRight_top.y),
                         (self.obstacle2BottomRight_left.x,
                          self.obstacle2BottomRight_left.y),
                         (self.obstacle2BottomRight_right.x,
                          self.obstacle2BottomRight_right.y),
                         (self.obstacle2BottomRight_bottom.x,
                          self.obstacle2BottomRight_bottom.y),
                         (self.obstacle1BottomRight_top.x,
                          self.obstacle1BottomRight_top.y),
                         (self.obstacle1BottomRight_left.x,
                          self.obstacle1BottomRight_left.y),
                         (self.obstacle1BottomRight_right.x,
                          self.obstacle1BottomRight_right.y),
                         (self.obstacle1BottomRight_bottom.x,
                          self.obstacle1BottomRight_bottom.y),
                         (self.rightBottomRect.x, self.rightBottomRect.y),
                         (self.bottomRect.x, self.bottomRect.y)]
        for message, messagePos in zip(messageLst, messagePosLst):
            msg = self.font.render(message, True, self.pink)
            self.window.blit(msg, messagePos)

    def playerMovement_logic(self):
        if self.playerRect.x <= 0:
            self.playerRect.x = 757
        if self.playerRect.x >= 758:
            self.playerRect.x = 0

        if self.playerRect.colliderect(self.topRect):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.leftTopRect) or self.playerRect.colliderect(self.leftBottomRect):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.rightTopRect) or self.playerRect.colliderect(self.rightBottomRect):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.bottomRect):
            self.playerRect.y -= self.playerVel

        if self.playerRect.colliderect(self.obstacle1TopLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1TopLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1TopLeft_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle1TopLeft_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.leftMidTop1Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.leftMidTop2Rect):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.leftMidTop3Rect):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.leftMidTop4Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.leftMidTop5Rect):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.leftMidTop6Rect):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.leftMidBottom6Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.leftMidBottom5Rect):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.leftMidBottom4Rect):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.leftMidBottom3Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.leftMidBottom2Rect):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.leftMidBottom1Rect):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.rightMidTop1Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.rightMidTop2Rect):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.rightMidTop3Rect):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.rightMidTop4Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.rightMidTop5Rect):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.rightMidTop6Rect):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.rightMidBottom6Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.rightMidBottom5Rect):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.rightMidBottom4Rect):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.rightMidBottom3Rect):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.rightMidBottom2Rect):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.rightMidBottom1Rect):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle2TopLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2TopLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2TopLeft_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle2TopLeft_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle3TopLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle3TopLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle3TopLeft_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle3TopLeft_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle2TopRight_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2TopRight_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2TopRight_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle2TopRight_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle1TopRight_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1TopRight_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1TopRight_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle1TopRight_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle1BottomLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1BottomLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1BottomLeft_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle1BottomLeft_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle2BottomLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2BottomLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2BottomLeft_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle2BottomLeft_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle3BottomLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle3BottomLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle3BottomLeft_right):
            self.playerRect.x += self.playerVel

        if self.playerRect.colliderect(self.obstacle4BottomLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle4BottomLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle4BottomLeft_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle4BottomLeft_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle2BottomRight_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2BottomRight_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle2BottomRight_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle2BottomRight_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.obstacle1BottomRight_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1BottomRight_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle1BottomRight_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle1BottomRight_bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.WordGTop):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.WordGTopInside):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.WordGLeft):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.WordGLeftInside):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.WordGRight1) or self.playerRect.colliderect(self.WordGRight2):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.WordGRight2Inside):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.WordGCurveTop):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.WordGCurveLeft):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.WordGCurveBottom):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.WordGBottomInside):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.WordGBottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.WordO1Top) or self.playerRect.colliderect(self.WordO2Top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.WordO1Left) or self.playerRect.colliderect(self.WordO2Left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.WordO1Right) or self.playerRect.colliderect(self.WordO2Right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.WordO1Bottom) or self.playerRect.colliderect(self.WordO2Bottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.enemyContainerTop1_G) or self.playerRect.colliderect(self.enemyContainerTop2_G):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.enemyContainerTop1Inside_G) or self.playerRect.colliderect(self.enemyContainerTop2Inside_G):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.enemyContainerLeft_G):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.enemyContainerLeftInside_G):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.enemyContainerRight_G):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.enemyContainerRightInside_G):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.enemyContainerBottomInside_G):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.enemyContainerBottom_G):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.obstacle_GTopLeft):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle_G):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle_GTopBottom):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.obstacle_GTopRight):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle_GBottomLeft):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle_GBottom):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.obstacle_GBottomRight):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle_GLeft_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle_GLeft_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle_GLeft_right):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.obstacle_GRight_top):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.obstacle_GRight_left):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.obstacle_GRight_right):
            self.playerRect.x += self.playerVel

        if self.playerRect.colliderect(self.WordLTop):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.WordLLeft):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.WordLRight):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.WordLBottom):
            self.playerRect.y += self.playerVel

        if self.playerRect.colliderect(self.WordETop):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.WordELeft):
            self.playerRect.x -= self.playerVel
        if self.playerRect.colliderect(self.WordEMidTop):
            self.playerRect.y += self.playerVel
        if self.playerRect.colliderect(self.WordEMidLeft):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.WordEMidBottom):
            self.playerRect.y -= self.playerVel
        if self.playerRect.colliderect(self.WordERight1):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.WordERight2):
            self.playerRect.x += self.playerVel
        if self.playerRect.colliderect(self.WordEBottom):
            self.playerRect.y += self.playerVel

    def ghostMovement_logic(self):
        if 0 <= self.redGhostRect.x <= self.winWidth:
            if self.t == 0:
                self.redGhostRect.x -= self.ghostVel
            for name in self.obs_right:
                if self.redGhostRect.colliderect(name):
                    self.t = 1
                    self.redGhostRect.y += self.ghostVel
            for name in self.obs_left:
                if self.redGhostRect.colliderect(name):
                    self.redGhostRect.y -= self.ghostVel
            for name in self.obs_bottom:
                if self.redGhostRect.colliderect(name):
                    self.redGhostRect.x -= self.ghostVel
            for name in self.obs_top:
                if self.redGhostRect.colliderect(name):
                    self.redGhostRect.x += self.ghostVel

    def updateScore(self):
        self.score += 10
        # max score = 5540

    def showScore(self):
        scoreMsg = self.font.render(
            f"score: {self.score - 20}", True, self.blue)
        self.window.blit(scoreMsg, (self.obstacle2TopLeft_top.x,
                         self.obstacle2TopLeft_top.y + 10))

    def drawFood(self):
        for foodPos in self.foodPosLst:
            pygame.draw.circle(self.window, self.white,
                               (foodPos.x, foodPos.y), foodPos.width // 2)

    def playerEatFood_logic(self):
        for foodItems in self.foodPosLst:
            if self.playerRect.colliderect(foodItems):
                if self.score > 20:
                    foodEatSound = pygame.mixer.Sound(
                        self.assets['chomp_sound'])
                    pygame.mixer.Channel(1).play(foodEatSound, 0)
                    foodEatSound.set_volume(0.9)
                self.foodPosLst.pop(self.foodPosLst.index(foodItems))
                self.updateScore()

    def win_logic(self):
        if len(self.foodPosLst) == 0:
            font1 = pygame.font.SysFont('monospace', 16, True, False)
            win_msg = font1.render("YOU WON!", True, self.red)
            self.window.blit(
                win_msg, (self.enemyContainerBottomInside_G.x, self.enemyContainerBottomInside_G.y))

    def drawGame(self):
        self.window.fill(self.black)
        # self.drawGrid()
        self.drawLayout()
        self.showScore()
        self.drawPlayer()
        self.playerEatFood_logic()
        self.drawFood()
        self.win_logic()
        self.drawGhost()
        # self.writeNamesOfObjects()
        self.playerMovement_logic()
        self.ghostMovement_logic()

    def gameLoop(self):
        self.window.blit(pygame.image.load("img/pacmanAssets/bg.png"), (0, 0))
        font1 = pygame.font.SysFont('monospace', 16, True, False)
        get_ready_msg = font1.render("READY!", True, self.red)
        self.window.blit(get_ready_msg, (self.enemyContainerBottomInside_G.x +
                         7, self.enemyContainerBottomInside_G.y))
        pygame.mixer.music.load(self.assets['beginning_sound'])
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(4_000)
        siren_bg_sound = pygame.mixer.Sound(self.assets['siren_sound'])
        pygame.mixer.Channel(0).play(siren_bg_sound, -1)
        siren_bg_sound.set_volume(0.4)
        while self.run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN and (event.key == K_ESCAPE):
                    self.run = False

                if event.type == pygame.KEYDOWN and (event.key == K_LEFT):
                    self.moveLeft = True
                    self.moveRight = False
                    self.moveUp = False
                    self.moveDown = False
                elif event.type == pygame.KEYDOWN and (event.key == K_RIGHT):
                    self.moveLeft = False
                    self.moveRight = True
                    self.moveUp = False
                    self.moveDown = False
                elif event.type == pygame.KEYDOWN and (event.key == K_UP):
                    self.moveLeft = False
                    self.moveRight = False
                    self.moveUp = True
                    self.moveDown = False
                elif event.type == pygame.KEYDOWN and (event.key == K_DOWN):
                    self.moveLeft = False
                    self.moveRight = False
                    self.moveUp = False
                    self.moveDown = True

            self.drawGame()
            pygame.display.update()
            clock.tick(self.fps)
        pygame.quit()


game = GameWindow()

game.gameLoop()
