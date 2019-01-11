from GameObject import *
import pygame


class BackGround:
    animation = None  # type: TranslateAnimation

    def __init__(self, x, y, width, height, frame, image: pygame.Surface):
        self.x = x
        self.y = y
        self.frame = frame
        # _scale_x = width / image.get_width()
        # _scale_y = height / image.get_height()
        # _scale_ = _scale_x if _scale_x > _scale_y else _scale_y
        # self.image = pygame.transform.scale(image, (int(image.get_width() * _scale_), int(image.get_height() * _scale_)))
        self.image = pygame.transform.scale(image, (width, height))
        self.width = width
        self.height = height
        self.increment_x = self.width / frame
        self.increment_y = self.height / frame
        self.temp_frame = 0

    def update(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))
        print(self.x, self.y)
        self.x -= self.increment_x * FRAME_RATE
        if self.x <= -self.width:
            self.x = self.width
