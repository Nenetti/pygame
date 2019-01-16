import pygame
from Animation import *


class GameObject:
    def __init__(self, x: float, y: float, width: float, height: float, image: pygame.Surface = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_width = image.get_width() if image is not None else width
        self.image_height = image.get_height() if image is not None else height
        self.image = image
        self.speed_x = 0
        self.speed_y = 0
        self.animation = None
        self.is_animation = False
        self.is_move = False
        self.is_delete = False
        self.is_displayed = False

    def set_animation(self, animation: Animation):
        self.is_animation = True
        self.animation = animation
        self.image_width = animation.width
        self.image_height = animation.height

    def set_image(self, image: pygame.Surface):
        self.image = image
        self.image_width = image.get_width()
        self.image_height = image.get_height()
        self.animation = None
        self.is_animation = False

    def set_speed(self, speed_x: float, speed_y: float):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.is_move = True

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def update(self, screen: pygame.Surface):
        if self.is_animation:
            self.animation.update(screen, self.x - self.image_width / 2, self.y - self.image_height / 2)
        else:
            if self.image is not None:
                screen.blit(self.image, [self.x - self.image_width / 2, self.y - self.image_height / 2])

        if self.is_move:
            self.move()

        if (self.x + self.image_width / 2 > 0 and self.x - self.image_width / 2 < screen.get_width()) and (
                self.y + self.image_height / 2 > 0 and self.y - self.image_height / 2 < screen.get_height()):
            self.is_displayed = True
        elif self.is_displayed:
            self.is_delete = True
