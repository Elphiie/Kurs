from ctypes import resize
from random import randint
from turtle import width
import pyglet
from pyglet import shapes, clock, sprite, image, resource
from pyglet.gl import *


#main settings
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

batch = pyglet.graphics.Batch()


dot_rng_pos_x = randint(0, game_window.width)
dot_rng_pos_y = randint(0, game_window.height)

rng_color = [randint(25, 255), randint(25, 255), randint(25, 255)]


dot = shapes.Circle(dot_rng_pos_x, dot_rng_pos_y, 5, color=rng_color, batch = main_batch)

def foods(num, batch = None):
    new_food = []
    for nums in range(0, num):
        food_pos_x = randint(0, 800)
        food_pos_y = randint(0, 600)
        ball = pyglet.sprite.Sprite(ball_img, food_pos_x, food_pos_y, batch=batch)
        new_food.append(ball)
    return new_food

def get_food(batch = None):
    food_pos_x = randint(0, game_window.width-10)
    food_pos_y = randint(0, game_window.height-10)
    gen_food = shapes.Circle(food_pos_x, food_pos_y, 3, color=(255, 0, 0), batch = batch)
    return gen_food

all_food = [get_food() for i in range(50)]

@game_window.event
def rng_move(dt):
    global x_i, y_i
    x_i = randint(0, 10)
    y_i = randint(0, 10)

    if x_i == 1:
        dot.x += 1
            
    elif x_i == 2:
        dot.x -= 1
    
    else:
        dot.x += 0


    if y_i == 1:
        dot.y += 1

    elif y_i == 2:
        dot.y -= 1

    else:
        dot.y += 0


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


@game_window.event
def update(dt):
    game_window.clear()
    batch.draw()

clock.schedule_interval(update, 5)


if __name__ == "__main__":
    # Start it up!

    # Update the game 120 times per second
    clock.schedule_interval(rng_move, 1/120)

    # Tell pyglet to do its thing
    pyglet.app.run()