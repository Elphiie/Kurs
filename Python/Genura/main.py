import math
from random import randint
import pyglet
from pyglet import clock, app
from pyglet.gl import *
from objects import Setup, Food, all_food


#main settings
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

batch = pyglet.graphics.Batch()

dot = Setup.life(batch=main_batch)

#gettin everything to show on screen
@game_window.event
def on_draw():
    
    game_window.clear()
    main_batch.draw()

#spawns food if the number of food is less than n
def spawn_food(dt):
    if len(all_food) < 50:
        all_food.append(Food.get_food())

    else:
        pass
    





if __name__ == "__main__":
    # Start it up!

    # Update the game 120 times per second


    #spawns the food at random intervals
    clock.schedule_interval(spawn_food, randint(10, 20))
    # Tell pyglet to do its thing
    app.run()