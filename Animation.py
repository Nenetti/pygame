import pygame
from Engine import *


class Animation:

    def __init__(self, image: pygame.Surface, split_x: int, split_y: int,
                 speed: int = 16, frame: int = 100, start_no: int = -1, end_no: int = -1, is_loop: bool = True, is_turn: bool = False):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.split_x = split_x
        self.split_y = split_y
        self.size_x = int(self.width / split_x)
        self.size_y = int(self.height / split_y)
        self.start_no = 0 if start_no == -1 else start_no
        self.end_no = split_x * split_y if end_no == -1 else end_no
        self.no = self.start_no
        self.no_increment = 1
        self.speed = speed
        self.frame = frame
        self.is_loop = is_loop
        self.is_turn = is_turn
        self.temp_speed = 0
        self.is_end = False

    def update(self, screen: pygame.Surface, x: int, y: int):
        if not self.is_end:
            self.calc_animation()
            _temp_x = int(self.no % self.split_x) * self.size_x
            _temp_y = int(self.no / self.split_x) * self.size_y
            screen.blit(self.image, [x, y],
                        [_temp_x, _temp_y, self.size_x, self.size_y])

    def calc_animation(self):
        self.temp_speed += Engine.FRAME_RATE
        if self.temp_speed > self.speed:
            self.temp_speed = 0
            self.no += self.no_increment
            if self.no <= self.start_no or self.no >= self.end_no:
                # リセット
                if self.is_loop:
                    # ループ
                    self.no_increment *= -1
                    if self.is_turn:
                        # 折り返し
                        self.no = self.start_no if self.no_increment > 0 else self.end_no - 1
                    else:
                        # 非 折り返し
                        self.no = self.start_no
                else:
                    self.is_end = True