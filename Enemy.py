import pygame


class Enemy:
    def __init__(self, x: float, y: float, width: float, height: float, image: pygame.Surface = None):
        super().__init__(x, y, width, height, image)