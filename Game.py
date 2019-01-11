from typing import List, Any

from Player import Player
import pygame
from Controller import *  # new import
from EMG import *  # new import
from Player import *
from Enemy import *
from Animation import *
from FPS import *


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
            pygame.time.delay(int(FRAME_RATE - fps.get_time()*1000))  # 60 FPS
        pygame.quit()

    ####################################################################################################################
    def start(self):

        player = Player(160, 240, 480, 480)
        player.set_animation(
            ImageAnimation(pygame.image.load("image/dash.png"), 6, 1, start_no=0, end_no=5, speed=72, is_turn=True))

        #player.set_animation(RotateAnimation(pygame.image.load("image/t.png"), 360, frame=1000, is_loop=False))
        #player.set_image(pygame.image.load("image/magic.png"))
        self.gameObjects.append(player)

        #obj = GameObject(320, 240, 1, 1)
        #obj.set_animation(
        #    ImageAnimation(pygame.image.load("image/moon.png"), 5, 6, start_no=16, end_no=30, speed=16, is_turn=True))
        #obj.set_animation(
        #    RotateAnimation(pygame.image.load("image/t.png"), 360, is_loop=True))

        #self.gameObjects.append(obj)

    ####################################################################################################################
    def update(self):
        # 画面初期化
        self.screen.fill(pygame.color.THECOLORS['white'])
        for g in self.gameObjects:
            g.update(self.screen)


####################################################################################################################
if __name__ == '__main__':
    g = Game()
