from Keyboard import *
import pygame
from GameObject import *


class Player(GameObject):
    def __init__(self, x: float, y: float, width: float, height: float, image: pygame.Surface = None):
        super().__init__(x, y, width, height, image)
        self.Controller = Keyboard()

    def update(self, screen: pygame.Surface):
        self.calc_speed(screen)
        super().update(screen)

    def calc_speed(self, screen: pygame.Surface):
        input = self.Controller.get_input()
        speed_x = 0
        speed_y = 0
        if input == Controller.Input.Left:
            speed_x = -5
            if self.x + speed_x < 0:
                speed_x = 0
        elif input == Controller.Input.Right:
            speed_x = 5
            if self.x + speed_x > screen.get_width():
                speed_x = 0
        self.x += speed_x
        self.y += speed_y
