from .life import Life
from .food import Food

import pygame
import random
pygame.init()


class GameInformation:
    def __init__(self, score):
        self.score = score


class Game:
    """
    To use this class simply initialize and instance and call the .loop() method
    inside of a pygame event loop (i.e while loop). Inside of your event loop
    you can call the .draw() and .move_paddle() methods according to your use case.
    Use the information returned from .loop() to determine when to end the game by calling
    .reset().
    """
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.life = Life(
            10, self.window_height // 2 - Life.RADIUS // 2)
        self.food = Food(self.window_width // 2, self.window_height // 2)

        self.score = 0
        self.window = window

    def _draw_score(self):
        score_text = self.SCORE_FONT.render(
            f"{self.score}", 1, self.WHITE)
        self.window.blit(score_text, (self.window_width //
                                           4 - score_text.get_width()//2, 20))




    def draw(self, draw_score=True):
        self.window.fill(self.BLACK)

        if draw_score:
            self._draw_score()

        for live in [self.life]:
            live.draw(self.window)

        self.food.draw(self.window)


    def move_paddle(self, left=True, up=True):
        """
        Move the left or right paddle.

        :returns: boolean indicating if paddle movement is valid. 
                  Movement is invalid if it causes paddle to go 
                  off the screen
        """
        if left:
            if up and self.life.y - Life.VEL < 0:
                return False
            if not up and self.life.y + Life.RADIUS > self.window_height:
                return False
            self.life.move(up)

        return True

    
    def loop(self):
        """
        Executes a single game loop.

        :returns: GameInformation instance stating score 
                  and hits of each paddle.
        """


        if self.food.x and self.food.y < self.life.x and self.life.y:
            self.food.reset()
            self.life += 1

        game_info = GameInformation(
            self.score)

        return game_info

    
    def reset(self):
        """Resets the entire game."""
        self.food.reset()
        self.life.reset()
        self.score = 0
