import pygame


class Enemy:
    def __init__(self, x: float, y: float, width: float, height: float, image: pygame.Surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed_x = 0
        self.speed_y = 0
        self.animation = False
        self.split_x = 0
        self.split_y = 0
        self.size_x = 0
        self.size_y = 0
        self.anim_no = 0
        self.max_anim = 0

    def set_animation(self, split_x: int, split_y: int):
        self.animation = True
        self.split_x = split_x
        self.split_y = split_y
        self.size_x = self.width / split_x
        self.size_y = self.height / split_y
        self.max_anim = split_x * split_y

    def move(self, speed_x: float, speed_y: float):
        self.x += speed_x
        self.y += speed_y

    def update(self, screen: pygame.Surface):
        if self.animation:
            screen.blit(self.image, [self.x, self.y],
                        [int(self.size_x * self.anim_no), 0, int(self.size_x), int(self.size_y)])
            self.anim_no += 1
            if self.anim_no >= self.max_anim:
                self.anim_no = 0
        else:
            screen.blit(self.image, [self.x, self.y])
