import pygame
from random import randint


class Life:
    VEL = 4
    RADIUS = 10

    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.RADIUS)

    def move(self, up=True, left=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
        
        if left:
            self.x -= self.VEL
        else:
            self.x += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
