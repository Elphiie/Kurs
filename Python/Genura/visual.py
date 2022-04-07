from random import randint
import pyglet
from pyglet import shapes, sprite, clock
from time import sleep

window = pyglet.window.Window(960, 540)

batch = pyglet.graphics.Batch()

dot_rng_pos_x = randint(0, window.width)
dot_rng_pos_y = randint(0, window.height)




rng_color = [randint(0, 255), randint(0, 255), randint(0, 255)]



dot = shapes.Circle(dot_rng_pos_x, dot_rng_pos_y, 5, color=rng_color, batch = batch)

class Food:
    def foods(num_food):
        for i in range(num_food):
            food_pos_x = randint(0, window.width-10)
            food_pos_y = randint(0, window.height-10)
            gen_food = shapes.Circle(food_pos_x, food_pos_y, 3, color=(255, 0, 0), batch = None)
        return gen_food



@window.event
def rng_move(dt):
    
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

food = Food.foods(50)

@window.event
def on_draw():
    
    window.clear()
    batch.draw()
    food.draw()


pyglet.clock.schedule_interval(rng_move, 1/120)
pyglet.app.run()