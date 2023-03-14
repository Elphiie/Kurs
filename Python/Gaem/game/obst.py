import pygame
from random import randint

class Floor:
    VEL = 4
    WIDTH = randint(25, 100)
    HEIGHT = 10

    def __init__(self, color, x, y):
        self.x = 1280
        self.y = 650
        self.color = color

    
    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def scroll(self):
        self.x_vel = self.VEL
        self.x -= self.x_vel