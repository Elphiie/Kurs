from pickletools import pylong
from time import sleep
import pyglet
from pyglet import shapes, clock
from random import randint

event_loop = pyglet.app.EventLoop()

class Food:

    def foods(batch = None):
        new_food = []
        
        for i in range(50):
                food_pos_x = randint(0, 800)
                food_pos_y = randint(0, 600)
                gen_food = shapes.Circle(food_pos_x, food_pos_y, 3, color=(255, 30, 30), batch = batch)
                new_food.append(gen_food)
        return new_food

    pyglet.clock.schedule_interval(foods, 2)

event_loop.run