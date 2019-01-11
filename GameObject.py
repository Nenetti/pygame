import pygame
from Animation import *


class GameObject:
    def __init__(self, x: float, y: float, width: float, height: float, image: pygame.Surface = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed_x = 0
        self.speed_y = 0
        self.animation = None
        self.is_animation = False

    def set_animation(self, animation: Animation):
        self.is_animation = True
        self.animation = animation
        self.width = animation.width
        self.height = animation.height

    def set_image(self, image: pygame.Surface):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.animation = None
        self.is_animation = False

    def move(self, speed_x: float, speed_y: float):
        self.x += speed_x
        self.y += speed_y

    def update(self, screen: pygame.Surface):
        if self.is_animation:
            self.animation.update(screen, self.x - self.width / 2, self.y - self.height / 2)
        else:
            if self.image is not None:
                screen.blit(self.image, [self.x - self.width / 2, self.y - self.height / 2])
