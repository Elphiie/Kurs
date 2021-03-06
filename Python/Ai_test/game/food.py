from turtle import window_width
import pygame
from random import randint
class Food:
    RADIUS = 20

    def __init__(self, x, y):
        self.x = randint(25, 1255)
        self.y = randint(75, 645)

    def draw(self, win):
        pygame.draw.circle(
            win, (255, 50, 50), (self.x, self.y), self.RADIUS)

    def reset(self):
        self.x = randint(25, 1255)
        self.y = randint(75, 645)