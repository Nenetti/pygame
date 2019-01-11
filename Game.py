from typing import List, Any

from Player import Player
import pygame
from Controller import *  # new import
from EMG import *  # new import
from Player import *
from Enemy import *
from Animation import *
from FPS import *
from BackGround import *

####################################################################################################################
class Game:
    screen = ...  # type: pygame.Surface
    gameObjects = []  # type: List[GameObject]

    ####################################################################################################################
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([640, 480])
        self.start()
        self.running = True
        fps = FPS()

        while self.running:
            fps.start()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    self.running = False

            self.update()
            pygame.display.update()

            fps.end()
            pygame.time.delay(int(FRAME_RATE - fps.get_time() * 1000))  # 60 FPS
        pygame.quit()

    ####################################################################################################################
    def start(self):

        background1 = BackGround(-self.screen.get_width(), 0, self.screen.get_width(), self.screen.get_height(), 1000,
                                pygame.image.load("image/back1.png"))
        self.gameObjects.append(background1)
        background2 = BackGround(0, 0, self.screen.get_width(), self.screen.get_height(), 1000,
                                 pygame.image.load("image/back1.png"))
        self.gameObjects.append(background2)
        background3 = BackGround(self.screen.get_width(), 0, self.screen.get_width(), self.screen.get_height(), 1000,
                                 pygame.image.load("image/back1.png"))
        self.gameObjects.append(background3)


        player = Player(160, 240, 480, 480)
        # player.set_animation(
        #    ImageAnimation(pygame.image.load("image/player_a.png"), 10, 3, start_no=2, end_no=7, speed=72, is_turn=True))
        player.set_animation(
            ImageAnimation(pygame.image.load("image/action0.png"),
                           split_x=6, split_y=1, frame=Player.ACTION0_FRAME, is_turn=False, is_loop=True))

        player.action1 = ImageAnimation(
            pygame.image.load("image/action1.png"), split_x=12, split_y=1, frame=Player.ACTION1_FRAME, is_loop=False)

        player.action2 = ImageAnimation(
            pygame.image.load("image/action2_1.png"), split_x=13, split_y=1, frame=Player.ACTION2_FRAME, is_loop=False)

        # player.set_animation(RotateAnimation(pygame.image.load("image/t.png"), 360, frame=1000, is_loop=False))
        # player.set_image(pygame.image.load("image/magic.png"))
        self.gameObjects.append(player)




    ####################################################################################################################
    def update(self):
        # 画面初期化
        self.screen.fill(pygame.color.THECOLORS['white'])

        #background = pygame.transform.scale(pygame.image.load("image/back1.png"), (self.screen.get_width(),
        #                                                                           self.screen.get_height()))

        #self.screen.blit(background, (0, 0))

        for g in self.gameObjects:
            g.update(self.screen)


####################################################################################################################
if __name__ == '__main__':
    g = Game()
