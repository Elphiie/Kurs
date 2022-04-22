from ctypes import resize
import math
from random import randint
from re import A
from turtle import width
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
if dot.x > 799 or dot.y > 599:
    dot.delete()
#food generator
class Food():

    def get_food():
        food_pos_x = randint(0, game_window.width-10)
        food_pos_y = randint(0, game_window.height-10)
        gen_food = shapes.Circle(food_pos_x, food_pos_y, 3, color=(255, 0, 0), batch = main_batch)
        return gen_food

global x_i, y_i
class Movement:
    global x_i, y_i
    #just to check movement. rendunant code. remove or eddit
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

    def hunt(dt):
        target = None
        target_d = float( 'inf' )

        for e in list( all_food ):
            d = math.dist( (dot.x, dot.y), (e.x, e.y) )

            
            if d > 0:
                
        
        
            
            


        

        
#just to check movement. rendunant code. remove or eddit

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
    

def respawn(dt):
     if dot == None:
        Setup.life()




if __name__ == "__main__":
    # Start it up!

    # Update the game 120 times per second

    clock.schedule_interval(Movement.hunt, 1/130)
    clock.schedule_interval(respawn, 1/130)
    #spawns the food at random intervals
    clock.schedule_interval(spawn_food, randint(0, 5))
    # Tell pyglet to do its thing
    app.run()