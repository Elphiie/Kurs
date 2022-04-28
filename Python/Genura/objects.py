import pyglet
from random import randint
from pyglet import shapes

main_batch = pyglet.graphics.Batch()

class Setup:
    
    dot_rng_pos_x = randint(0, 769)
    dot_rng_pos_y = randint(0, 590)

#random color generator that won't generate red as our food is red
    rng_color = [randint(25, 50), randint(50, 255), randint(50, 255)]

#the being
    def life(batch=None):
        dot = shapes.Circle(Setup.dot_rng_pos_x, Setup.dot_rng_pos_y, 7, color=Setup.rng_color, batch=None)
        return dot

#to store the food generated
all_food = []
#the dot

#food generator
class Food():

    def get_food():
        food_pos_x = randint(0, 790)
        food_pos_y = randint(0, 590)
        gen_food = shapes.Circle(food_pos_x, food_pos_y, 3, color=(255, 0, 0), batch = main_batch)
        return gen_food
    