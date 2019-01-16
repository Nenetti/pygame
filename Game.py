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
import random


####################################################################################################################
class Game:
    screen = ...  # type: pygame.Surface
    player = []  # type: player
    gameObjects = []  # type: List[GameObject]
    enemies = []  # type: List[GameObject]
    score = 0
    sysfont = None
    life_image = None

    ####################################################################################################################
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([640, 480])
        self.sysfont = pygame.font.SysFont(None, 60)
        self.life_image = pygame.image.load("image/heart.png")

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
            delay = int(FRAME_RATE - fps.get_time() * 1000)
            if delay < 0:
                delay = 0
            pygame.time.delay(delay)  # 60 FPS
        pygame.quit()

    ####################################################################################################################
    def start(self):

        background1 = BackGround(self.screen, 0, 0, 2880,
                                 pygame.image.load("image/back2.png"))
        self.gameObjects.append(background1)

        field = BackGround(self.screen, 0, 288, 2880,
                           pygame.image.load("image/field.png"))
        self.gameObjects.append(field)

        self.player = Player(160, 330, 0, 0)
        self.player.set_animation(
            ImageAnimation(pygame.image.load("image/action0.png"),
                           split_x=6, split_y=1, frame=Player.ACTION0_FRAME, is_turn=False, is_loop=True))

        self.player.action1 = ImageAnimation(
            pygame.image.load("image/action1.png"), split_x=12, split_y=1, frame=Player.ACTION1_FRAME, is_loop=False)

        self.player.action2 = ImageAnimation(
            pygame.image.load("image/action2_1.png"), split_x=13, split_y=1, frame=Player.ACTION2_FRAME, is_loop=False)

        self.player.action3 = ImageAnimation(
            pygame.image.load("image/action3_1.png"), split_x=7, split_y=1, frame=Player.ACTION3_FRAME, is_loop=False)

    # #########################################################################################################################
    def update(self):
        # 画面初期化
        if self.player.life > 0:
            self.screen.fill(pygame.color.THECOLORS['white'])

            deletes = []

            for g in self.gameObjects:
                g.update(self.screen)
            for e in self.enemies:
                e.update(self.screen)
                if e.is_delete:
                    deletes.append(e)

            for d in deletes:
                self.enemies.remove(d)

            for e in self.enemies:
                if self.calc_hit(self.player, e):
                    if self.player.action == 3 and e.attack_type == 3:
                        e.is_delete = True
                    else:
                        if self.player.action != e.attack_type:
                            if not self.player.is_invincible:
                                self.player.add_damage()
                                self.screen.fill(pygame.color.THECOLORS['red'])

            self.player.update(self.screen)
            self.respawn(self.enemies)

            self.score += 1
            self.screen.blit(self.sysfont.render(str(self.score) + "m", False, (255, 255, 255)), (0, 0))

            for i in range(self.player.life):
                self.screen.blit(self.life_image, [self.screen.get_width() - (i + 1) * 50, 0])
        else:
            self.screen.fill(pygame.color.THECOLORS['black'])
            self.screen.blit(self.sysfont.render("GAME OVER", False, (255, 255, 255)), (150, 200))
            self.screen.blit(self.sysfont.render("Score " + str(self.score) + "m", False, (255, 255, 255)), (150, 300))

    def calc_hit(self, obj1: gameObjects, obj2: gameObjects):
        dx = abs(obj1.x - obj2.x)
        dwx = obj1.width / 2 + obj2.width / 2
        dy = abs(obj1.y - obj2.y)
        dwy = obj1.height / 2 + obj2.height / 2
        if dx < dwx and dy < dwy:
            return True
        return False

    def respawn(self, enemies):
        if len(enemies) < 2:
            sx = 640
            width = 400 - int(self.score / 10)
            if width < 300:
                width = 300
            if len(enemies) == 1:
                sx = enemies[0].x + width
                if sx < 640:
                    sx = 640
            rand = random.randint(1, 8)
            if rand <= 4:
                enemy = Enemy(random.randint(sx, sx + width), 290, 64, 192, pygame.image.load("image/obj2.png"))
                enemy.set_speed(-10, 0)
                enemy.set_attack_type(1)
                enemies.append(enemy)
            if 4 < rand <= 8:
                enemy = Enemy(random.randint(sx, sx + width), 290, 64, 128, pygame.image.load("image/obj1.png"))
                enemy.set_speed(-10, 0)
                enemy.set_attack_type(2)
                enemies.append(enemy)
            if 8 < rand:
                enemy = Enemy(random.randint(sx, sx + width), 290, 64, 192, pygame.image.load("image/obj3.png"))
                enemy.set_speed(-10, 0)
                enemy.set_attack_type(3)
                enemies.append(enemy)


####################################################################################################################
if __name__ == '__main__':
    g = Game()
