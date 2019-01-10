from typing import List, Any

from Player import Player
from pg_engine import *
from Controller import *  # new import
from EMG import *  # new import
from Player import *
from Enemy import *
from Animation import *


####################################################################################################################
class Game:
    gameObjects = []  # type: List[GameObject]
    player = ...  # type: Player

    ####################################################################################################################
    def __init__(self):
        self.start()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    self.running = False

            self.update()
            pygame.display.update()
            pygame.time.delay(16)  # 60 FPS
        pygame.quit()

    ####################################################################################################################
    def start(self):
        self.player = Player(160, 240, 480, 480)
        self.player.set_animation(
            Animation(pygame.image.load("moon.png"), 5, 6, start_no=16, end_no=30, speed=48, is_turn=False))
        self.gameObjects.append(self.player)

        player1 = Player(480, 240, 480, 480)
        player1.set_animation(
            Animation(pygame.image.load("moon.png"), 5, 6, start_no=16, end_no=30, speed=48, is_turn=True))
        self.gameObjects.append(player1)

    ####################################################################################################################
    def update(self):
        # 画面初期化
        screen.fill(pygame.color.THECOLORS['black'])
        for g in self.gameObjects:
            g.update(screen)


####################################################################################################################
if __name__ == '__main__':
    g = Game()
