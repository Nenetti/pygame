import pygame
from FPS import *


class Animation:

    def __init__(self):
        self.is_end = False

    def update(self, screen: pygame.Surface, x: int, y: int):
        pass

    def reset(self):
        self.is_end = False


class ImageAnimation(Animation):

    def __init__(self, image: pygame.Surface, split_x: int = 1, split_y: int = 1,
                 speed: int = 16, frame: int = -1, start_no: int = -1, end_no: int = -1, is_loop: bool = True,
                 is_turn: bool = False, is_reverse: bool = False):
        super().__init__()
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.split_x = split_x
        self.split_y = split_y
        self.width = int(self.width / split_x)
        self.height = int(self.height / split_y)
        self.start_no = 0 if start_no == -1 else start_no
        self.end_no = split_x * split_y - 1 if end_no == -1 else end_no
        self.no = self.end_no if is_reverse else self.start_no
        self.no_increment = -1 if is_reverse else 1
        self.speed = speed
        self.frame = frame
        if not self.frame == -1:
            self.speed = self.frame / (self.end_no - self.start_no + 1)
        self.is_loop = is_loop
        self.is_turn = is_turn
        self.is_reverse = is_reverse
        self.temp_speed = 0
        self.temp_x = 0
        self.temp_y = 0

    def update(self, screen: pygame.Surface, x: int, y: int):
        if not self.is_end:
            self.calc_animation()
            self.temp_x = int(self.no % self.split_x) * self.width
            self.temp_y = int(self.no / self.split_x) * self.height
        screen.blit(self.image, [x, y],
                    [self.temp_x, self.temp_y, self.width, self.height])

    def calc_animation(self):
        self.temp_speed += FRAME_RATE
        if self.temp_speed > self.speed:
            self.temp_speed = 0
            self.no += self.no_increment
            if self.no < self.start_no or self.no > self.end_no:
                # リセット
                if self.is_loop:
                    # ループ
                    if self.is_turn:
                        # 折り返し
                        self.no_increment *= -1
                        self.no = self.start_no + 1 if self.no_increment > 0 else self.end_no - 1
                    else:
                        # 非 折り返し
                        self.no = self.start_no
                else:
                    self.no = self.end_no
                    self.is_end = True

    def reset(self):
        super().reset()
        self.no = self.start_no
        self.no_increment = 1


class RotateAnimation(Animation):

    def __init__(self, image: pygame.Surface,
                 angle: float, frame: int = 1000, is_loop: bool = False, is_turn: bool = False):
        super().__init__()
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.angle = angle
        self.frame = frame
        self.is_loop = is_loop
        self.is_turn = is_turn
        self.temp_angle = 0
        self.angle_increment = angle / frame
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


class TranslateAnimation(Animation):

    def __init__(self, sx, sy, func_x, func_y, frame: float, is_loop=False):
        super().__init__()
        self.func_x = func_x
        self.func_y = func_y
        self.frame = frame
        self.t = 0
        self.x = 0
        self.y = 0
        self.sx = sx
        self.sy = sy
        self.is_loop = is_loop

    def update(self):
        if not self.is_end:
            self.t += FRAME_RATE
            self.x = self.sx + self.func_x(self.t)
            self.y = self.sy + self.func_y(self.t)
            self.calc_animation()

    def calc_animation(self):
        if self.t >= self.frame:
            if self.is_loop:
                self.t = 0
            else:
                #のちほど修正
                self.x = self.sx
                self.y = self.sy
                self.is_end = True

    def get_translate(self):
        return self.x, self.y
