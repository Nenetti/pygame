from GameObject import *
import pygame


class BackGround:
    animation = None  # type: TranslateAnimation

    def __init__(self, screen: pygame.Surface, sx, sy, frame, image: pygame.Surface):
        self.sx = sx
        self.sy = sy
        self.x1 = sx
        self.x2 = sx
        self.x3 = sx
        self.y1 = sy
        self.y2 = sy
        self.y3 = sy
        self.image = image
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.increment_x = (self.width * 3) / frame
        self.increment_y = (self.height * 3) / frame

    def update(self, screen: pygame.Surface):

        self.x1 -= self.increment_x * FRAME_RATE
        if self.x1 < -self.width:
            self.x1 += self.width

        self.x2 = self.x1 + self.width
        self.x3 = self.x2 + self.width

        screen.blit(self.image, (self.x1, self.y1))
        screen.blit(self.image, (self.x2, self.y2))
        screen.blit(self.image, (self.x3, self.y3))
