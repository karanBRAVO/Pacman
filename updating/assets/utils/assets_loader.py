import pygame


def get_player_images_lists(playerRightImg: dict, playerLeftImg: dict, playerDownImg: dict, playerUpImg: dict):
    pacmanMoveRightImgLst = [playerRightImg['pr'], playerRightImg['pr1'], playerRightImg['pr2'], playerRightImg['pr3'], playerRightImg['pr4'],
                             playerRightImg['pr5']]
    pacmanMoveLeftImgLst = [playerLeftImg['pl'], playerLeftImg['pl1'], playerLeftImg['pl2'], playerLeftImg['pl3'], playerLeftImg['pl4'],
                            playerLeftImg['pl5']]
    pacmanMoveDownImgLst = [playerDownImg['pd'], playerDownImg['pd1'], playerDownImg['pd2'], playerDownImg['pd3'], playerDownImg['pd4'],
                            playerDownImg['pd5']]
    pacmanMoveUpImgLst = [playerUpImg['pu'], playerUpImg['pu1'], playerUpImg['pu2'], playerUpImg['pu3'], playerUpImg['pu4'],
                          playerUpImg['pu5']]
    return {"right": pacmanMoveRightImgLst, "left": pacmanMoveLeftImgLst, "down": pacmanMoveDownImgLst, "up": pacmanMoveUpImgLst}


def load_playerImages(imageDir: str, width: int, height: int):
    playerRightImg = {
        'pr': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanRight.png"), (width, height)),
        'pr1': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanRight1.png"), (width, height)),
        'pr2': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanRight2.png"), (width, height)),
        'pr3': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanRight3.png"), (width, height)),
        'pr4': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanRight4.png"), (width, height)),
        'pr5': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanRight5.png"), (width, height)),
    }
    playerLeftImg = {
        'pl': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanLeft.png"), (width, height)),
        'pl1': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanLeft1.png"), (width, height)),
        'pl2': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanLeft2.png"), (width, height)),
        'pl3': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanLeft3.png"), (width, height)),
        'pl4': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanLeft4.png"), (width, height)),
        'pl5': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanLeft5.png"), (width, height)),
    }
    playerUpImg = {
        'pu': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanUp.png"), (width, height)),
        'pu1': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanUp1.png"), (width, height)),
        'pu2': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanUp2.png"), (width, height)),
        'pu3': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanUp3.png"), (width, height)),
        'pu4': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanUp4.png"), (width, height)),
        'pu5': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanUp5.png"), (width, height)),
    }
    playerDownImg = {
        'pd': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanDown.png"), (width, height)),
        'pd1': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanDown1.png"), (width, height)),
        'pd2': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanDown2.png"), (width, height)),
        'pd3': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanDown3.png"), (width, height)),
        'pd4': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanDown4.png"), (width, height)),
        'pd5': pygame.transform.scale(pygame.image.load(f"{imageDir}/pacmanDown5.png"), (width, height)),
    }

    return {"right": playerRightImg, "left": playerLeftImg, "down": playerDownImg, "up": playerUpImg}
