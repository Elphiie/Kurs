from faulthandler import dump_traceback
from tracemalloc import start
import pygame
from .life import Life
from .food import Food
from random import randint
import math
import time


pygame.init()

class GameInformation:
    def __init__(self, score_1, score_2, dur, fps):
        self.score_1 = score_1
        self.score_2 = score_2
        self.dur = dur
        self.fps = fps

class Game:
    """
    To use this class simply initialize and instance and call the .loop() method
    inside of a pygame event loop (i.e while loop). Inside of your event loop
    you can call the .draw() and .move_Life() methods according to your use case.
    Use the information returned from .loop() to determine when to end the game by calling
    .reset().
    """
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    start_time = time.time()
    clock = pygame.time.Clock()

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.life_1 = Life(
            self.window_width - 10 - Life.WIDTH, self.window_height // 2 - Life.HEIGHT//2)
        self.life_2 = Life(
            self.window_width - 10 - Life.WIDTH, self.window_height // 2 - Life.HEIGHT//2)
        self.food = Food(self.window_width // 2, self.window_height // 2)
        

        self.score_1 = 0
        self.score_2 = 0
        self.dur = 0
        self.fps = 0
        self.window = window


    def _draw_score(self):
        left_score_text = self.SCORE_FONT.render(
            f"{self.score_1}", 1, self.WHITE)
        right_score_text = self.SCORE_FONT.render(
            f"{self.score_2}", 1, self.WHITE)
        time_text = self.SCORE_FONT.render(
            f"{self.dur}", 1, self.YELLOW)
        fps_text = self.SCORE_FONT.render(
            f"{self.fps}", 1, self.YELLOW)
            
        self.window.blit(left_score_text, (self.window_width //
                                           4 - left_score_text.get_width()//2, 20))
        self.window.blit(right_score_text, (self.window_width * (3/4) -
                                            right_score_text.get_width()//2, 20))
        self.window.blit(time_text, (self.window_width * (1/3) -
                                            time_text.get_width()//2, 20))
        self.window.blit(fps_text, (self.window_width * -(1/3) -
                                            fps_text.get_width()//2, 20,
                                    self.window_height - 50, 15))

    def _handle_collision(self):
        food = self.food
        life1 = self.life_1
        life2 = self.life_2
        d = math.dist((life1.x, life1.y), (life2.x, life2.y))

        if life1.y + Life.HEIGHT >= self.window_height:

            self.score_1 -= 1
            life1.reset()
        elif life1.y - Life.HEIGHT <= 20:
            self.score_1 -= 1
            life1.reset()
        elif life1.x + Life.WIDTH >= self.window_width:
            self.score_1 -= 1
            life1.reset()
        elif life1.x - Life.WIDTH <= 20:
            self.score_1 -= 1
            life1.reset()


        if life2.y + Life.HEIGHT >= self.window_height:
            self.score_2 -= 1
            life2.reset()
        elif life2.y - Life.HEIGHT <= 20:
            self.score_2 -= 1
            life2.reset()
        elif life2.x + Life.WIDTH >= self.window_width:
            self.score_2 -= 1
            life2.reset()
        elif life2.x - Life.WIDTH <= 20:
            self.score_2 -= 1
            life2.reset()


        if d < Life.HEIGHT or d < Life.WIDTH:
            self.life_1.VEL *= -1
            self.life_2.VEL *= -1
        else:
            self.life_1.VEL = 4
            self.life_2.VEL = 4
        


    def draw(self, draw_score=True):
        self.window.fill(self.BLACK)
        if draw_score:
            self._draw_score()

        self.life_1.draw(self.window)
        self.life_2.draw(self.window)


        
        self.food.draw(self.window)





    def move_life(self, left=True, up=True, right=True, down=True, cum=True):
        """
        Move the left or right Life.

        :returns: boolean indicating if Life movement is valid. 
                  Movement is invalid if it causes Life to go 
                  off the screen
        """
        if cum:
            if up:
                if up and self.life_1.y - Life.VEL < 0:
                    return False
                if not up and self.life_1.y + Life.HEIGHT > self.window_height:
                    return False
                self.life_1.move_up(up)

            if down:
                if down and self.life_1.y - Life.VEL < 0:
                    return False
                if not down and self.life_1.y - Life.HEIGHT <= 20:
                    return False
                self.life_1.move_down(down)

            if left:
                if left and self.life_1.x - Life.VEL < 0:
                    return False
                if not left and self.life_1.x - Life.WIDTH <= 20:
                    return False
                self.life_1.move_left(left)

            if right:
                if right and self.life_1.x - Life.VEL < 0:
                    return False
                if not right and self.life_1.x + Life.WIDTH > self.window_width:
                    return False
                self.life_1.move_right(right)
            if not up and not down and not left and not right:
                self.score_1 -= 1

        else:
            if up:
                if up and self.life_2.y - Life.VEL < 0:
                    return False
                if not up and self.life_2.y + Life.HEIGHT > self.window_height:
                    return False
                self.life_2.move_up(up)

            if down:
                if down and self.life_2.y - Life.VEL < 0:
                    return False
                if not down and self.life_2.y - Life.HEIGHT <= 20:
                    return False
                self.life_2.move_down(down)

            if self.life_1.x_vel and self.life_1.y_vel < 4:
                self.score_1 -= 1

            if left:
                if left and self.life_2.x - Life.VEL < 0:
                    return False
                if not left and self.life_2.x - Life.WIDTH <= 20:
                    return False
                self.life_2.move_left(left)

            if right:
                if right and self.life_2.x - Life.VEL < 0:
                    return False
                if not right and self.life_2.x + Life.WIDTH > self.window_width:
                    return False
                self.life_2.move_right(right)
            if not up and not down and not left and not right:
                self.score_2 -= 1

            if self.life_2.x_vel and self.life_2.y_vel < 4:
                self.score_2 -= 1    
        


        return True



    def loop(self):
        """
        Executes a single game loop.

        :returns: GameInformation instance stating score 
                  and hits of each Life.
        """     
        self.life_1.move_up()
        self.life_1.move_down()
        self.life_1.move_left()
        self.life_1.move_right()

        self.life_2.move_up()
        self.life_2.move_down()
        self.life_2.move_left()
        self.life_2.move_right()

        self._handle_collision()
        
        for lif in [self.life_1]:
            d = math.dist((lif.x, lif.y), (self.food.x, self.food.y))

            if d <= self.food.RADIUS * 2 + self.life_1.WIDTH:
                self.food.reset()
                self.score_1 += 25
                

        for lif in [self.life_2]:
            d = math.dist((lif.x, lif.y), (self.food.x, self.food.y))

            if d <= self.food.RADIUS * 2 + self.life_2.WIDTH:
                self.score_2 += 25
                self.food.reset()
        

        game_info = GameInformation(
            self.score_1, self.score_2, self.dur, self.fps)


        return game_info

    def reset(self):
        """Resets the entire game."""
        self.food.reset()
        self.life_1.reset()
        self.life_2.reset()
        self.score_1 = 0
        self.score_2 = 0