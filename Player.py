from Keyboard import *
from GameObject import *
from Animation import *
import numpy as np


class Player(GameObject):
    normal_action = None  # type: Animation
    action1 = None  # type: Animation
    action2 = None  # type: Animation

    ACTION0_FRAME = 300
    ACTION1_FRAME = 500
    ACTION2_FRAME = 600

    translate = None  # type: TranslateAnimation

    def __init__(self, x: float, y: float, width: float, height: float, image: pygame.Surface = None):
        super().__init__(x, y, width, height, image)
        self.Controller = Keyboard()
        self.can_input = True

    def update(self, screen: pygame.Surface):
        self.read_imput()
        if not self.can_input and self.animation.is_end:
            self.animation = self.normal_action
            self.can_input = True
        if self.translate is not None:
            self.translate.update()
            self.x, self.y = self.translate.get_translate()
        super().update(screen)

    def set_animation(self, animation: Animation):
        super().set_animation(animation)
        self.normal_action = animation

    def read_imput(self):
        if self.can_input:
            input = self.Controller.get_input()
            if input == Controller.Input.Left:
                self.animation = self.action1
                self.translate = TranslateAnimation(self.x, self.y, Player.sliding_x, Player.sliding_y, Player.ACTION1_FRAME)
                self.animation.reset()
                self.can_input = False
            elif input == Controller.Input.Right:
                self.animation = self.action2
                self.translate = TranslateAnimation(self.x, self.y, Player.jump_x, Player.jump_y, Player.ACTION2_FRAME)
                self.animation.reset()
                self.can_input = False

    @staticmethod
    def jump_x(t):
        return 0

    @staticmethod
    def jump_y(t):
        return -100 * np.sin((t / Player.ACTION2_FRAME) * np.pi)

    @staticmethod
    def sliding_x(t):
        return 50 * np.sin((t / Player.ACTION1_FRAME) * np.pi)

    @staticmethod
    def sliding_y(t):
        return 0
