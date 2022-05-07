
from glob import glob
import math
from random import randint
from unittest import main
from click import pass_obj
import pyglet
from pyglet import shapes, clock, sprite, image, resource, app, text
from pyglet.gl import *

#main settings
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

dot = []

class CreateObj:
    

    def __init__(self, x, y, radius, segments, color, **kargs):
        self._radius = radius 
        self._segments = segments
        self._x = x
        self._y = y
        self._color = color
        self.group = pyglet.shapes.Circle
#the being
    def obj(self):
        x = self._x
        y = self._y
        radius = self._radius
        color = self._color
        
        pyglet.shapes.Circle(x, y, radius, color, batch=main_batch)
        

def create_life():
    d_x = randint(0, game_window.width)
    d_y = randint(0, game_window.height)
    d_rng_color = [randint(25, 100), randint(50, 255), randint(50, 255)]

    life=CreateObj(d_x, d_y, 7, 1, d_rng_color)

    return life

main_batch.draw()

#gettin everything to show on screen
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    print(dot)



def spawn_life(dt):
    print(len(dot))
    if len(dot) < 10:
        dot.append(create_life())
if __name__ == "__main__":
    # Start it up!

    # Update the game 120 times per second
    clock.schedule_interval(spawn_life, 1)
    #spawns the food at random intervals
    # Tell pyglet to do its thing
    app.run()