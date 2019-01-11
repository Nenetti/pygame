import pygame
from FPS import *


class Animation:

    def __init__(self, image: pygame):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

    def update(self, screen: pygame.Surface, x: int, y: int):
        pass


class ImageAnimation(Animation):

    def __init__(self, image: pygame.Surface, split_x: int, split_y: int,
                 speed: int = 16, frame: int = 100, start_no: int = -1, end_no: int = -1, is_loop: bool = True,
                 is_turn: bool = False, is_reverse = False):
        super().__init__(image)
        self.split_x = split_x
        self.split_y = split_y
        self.width = int(self.width / split_x)
        self.height = int(self.height / split_y)
        self.start_no = 0 if start_no == -1 else start_no
        self.end_no = split_x * split_y if end_no == -1 else end_no
        self.no = self.end_no if is_reverse else self.start_no
        self.no_increment = -1 if is_reverse else 1
        self.speed = speed
        self.frame = frame
        self.is_loop = is_loop
        self.is_turn = is_turn
        self.is_reverse = is_reverse
        self.temp_speed = 0
        self.is_end = False

    def update(self, screen: pygame.Surface, x: int, y: int):
        if not self.is_end:
            self.calc_animation()
            print(self.no)
            _temp_x = int(self.no % self.split_x) * self.width
            _temp_y = int(self.no / self.split_x) * self.height
        screen.blit(self.image, [x, y],
                    [_temp_x, _temp_y, self.width, self.height])

    def calc_animation(self):
        self.temp_speed += FRAME_RATE
        if self.temp_speed > self.speed:
            self.temp_speed = 0
            self.no += self.no_increment
            if self.no < self.start_no or self.no > self.end_no:
                # リセット
                if self.is_loop:
                    # ループ
                    self.no_increment *= -1
                    if self.is_turn:
                        # 折り返し
                        self.no = self.start_no+1 if self.no_increment > 0 else self.end_no - 1
                    else:
                        # 非 折り返し
                        self.no = self.start_no
                else:
                    self.is_end = True

    def reset(self):
        self.no = self.start_no
        self.no_increment = 1


class RotateAnimation(Animation):

    def __init__(self, image: pygame.Surface,
                 angle: float, frame: int = 1000, is_loop: bool = False, is_turn: bool = False):
        super().__init__(image)
        self.angle = angle
        self.frame = frame
        self.is_loop = is_loop
        self.is_turn = is_turn
        self.temp_angle = 0
        self.angle_increment = angle / frame
        self.is_end = False
        self.temp_image = None
        self.temp_rect = None

    def update(self, screen: pygame.Surface, x: int, y: int):
        if not self.is_end:
            self.calc_animation()
            image = pygame.transform.rotate(self.image, self.temp_angle)
            rect = image.get_rect()
            rect.center = (x + self.width / 2, y + self.height / 2)
            screen.blit(image, rect)
        else:
            self.temp_rect.center = (x + self.width / 2, y + self.height / 2)
            screen.blit(self.temp_image, self.temp_rect)

    def calc_animation(self):
        self.temp_angle += self.angle_increment * FRAME_RATE
        if self.temp_angle >= self.angle:
            if self.is_loop:
                self.temp_angle = 0
            else:
                self.temp_angle = self.angle
                self.temp_image = pygame.transform.rotate(self.image, self.temp_angle)
                self.temp_rect = self.temp_image.get_rect()
                self.is_end = True
