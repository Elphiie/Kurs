import math
from random import randint
from turtle import width, window_width
import pyglet
from pyglet import shapes, clock, sprite, image, resource, app
from pyglet.gl import *


#main settings
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

batch = pyglet.graphics.Batch()

#object setup
#generate random x/y coordinates
class Setup:
    
    dot_rng_pos_x = randint(0, game_window.width)
    dot_rng_pos_y = randint(0, game_window.height)

#random color generator that won't generate red as our food is red
    rng_color = [randint(25, 50), randint(50, 255), randint(50, 255)]

#the being
    def life():
        dot = shapes.Circle(Setup.dot_rng_pos_x, Setup.dot_rng_pos_y, 7, color=Setup.rng_color, batch = main_batch)
        return dot

#to store the food generated
all_food = []
#the dot
dot = Setup.life()
#food generator
class Food():

    def get_food():
        food_pos_x = randint(0, game_window.width-10)
        food_pos_y = randint(0, game_window.height-10)
        gen_food = shapes.Circle(food_pos_x, food_pos_y, 3, color=(255, 0, 0), batch = main_batch)
        return gen_food

class Movement:
    #just to check movement. rendunant code. remove or eddit
    def rng_move():
    
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

    def hunt():
        t = None
        t_d = float('inf')

        for e in all_food:
            d = math.dist( (dot.x, dot.y), (e.x, e.y) )

            

            if d < t_d:
                t = e
                t_d = d


            if t:

                if t_d > 2:

                    tdx = math.atan((t.x))
                    tdy = math.atan((t.y))

                    dot.x += tdy
                    dot.y += tdx

            
            if t_d < 3:
                all_food.remove(t)

    def border():
        if dot.x > 795:
            dot.x -= 1

        if dot.x < 5:
            dot.x += 1

        if dot.y > 595:
            dot.y -= 1

        if dot.y < 5:
            dot.y += 1
        
        

#gettin everything to show on screen
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


#spawns food if the number of food is less than n
def spawn_food(dt):
    if len(all_food) < 2:
        all_food.append(Food.get_food())

    else:
        pass

def movement(dt):
    Movement.border() 
    Movement.hunt()

def respawn(dt):
     if dot == '':
        Setup.life()




if __name__ == "__main__":
    # Start it up!

    # Update the game 120 times per second

    clock.schedule_interval(movement, 1/120)
    clock.schedule_interval(respawn, 1/230)
    #spawns the food at random intervals
    clock.schedule_interval(spawn_food, randint(0, 3))
    # Tell pyglet to do its thing
    app.run()