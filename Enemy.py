import pygame
from GameObject import *


class Enemy(GameObject):

    attack_type = 0

    def __init__(self, x: float, y: float, width: float, height: float, image: pygame.Surface = None):
        super().__init__(x, y, width, height, image)

    def set_attack_type(self, value):
        self.attack_type = value

    def update(self, screen: pygame.Surface):
        super().update(screen)
