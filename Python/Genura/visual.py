from glob import glob
import math
from random import randint
import os
import pyglet
from pyglet import shapes, clock, sprite, image, resource, app, text
from pyglet.gl import *


#main settings
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

batch = pyglet.graphics.Batch()

score_draw = True
score_now = score_best = 0
score_now_label = pyglet.text.Label()
score_best_label = pyglet.text.Label( anchor_x='right' )

time_sum = 0
time_min = 1/60*0.9



def score( s=0 ):
    global score_draw, score_now, score_best
    for d in dot:
        for ds in d:
            score_draw = True
            score_now = max( 0, score_now+s )
            score_best = max( score_now, score_best )

    return d, score_now

s=0
#the being
def life():
    global dot_life
    dot_rng_pos_x = randint(0, game_window.width)
    dot_rng_pos_y = randint(0, game_window.height)
    rng_color = [randint(25, 100), randint(50, 255), randint(50, 255)]

    dots = shapes.Circle(dot_rng_pos_x, dot_rng_pos_y, 7, color=rng_color, batch = main_batch)

    for d in dot:
        dot_life = randint(20, 60)
        dot_life -= time_sum

        if dot_life < 1:
            dot.remove(d)

    return dots

#to store the food generated
all_food = []
#the dot
dot = []
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
    
       

        for d in dot:
            x_i = randint(0, 10)
            y_i = randint(0, 10)

            try:
                if x_i == 1:
                    d.x += 1
                        
                elif x_i == 2:
                    d.x -= 1
                
                else:
                    d.x += 0


                if y_i == 1:
                    d.y += 1

                elif y_i == 2:
                    d.y -= 1

                else:
                    d.y += 0
            except:
                len(dot) < 1

    def hunt():
        global dot_life, score_best
        t = None
        t_d = float('inf')

        for do in dot:
            for e in all_food:
                d = math.dist( (do.x, do.y), (e.x, e.y) )


                if d < t_d:
                    t_d = d
                    t = e

            if t:

                if t_d > 1:
                    try:
                        if t.x < do.x:
                            do.x -= t.x / 80 / 2
                        if t.y < do.y:
                            do.y -= t.y / 60 / 2
                        if t.x > do.x:
                            do.x += t.x / 80 / 2
                        if t.y > do.y:
                            do.y += t.y / 60 / 2
                    except:
                        len(dot) < 1
    
                if t:
                    if t_d < 7:
                        try:
                            all_food.remove(t)
                            dot_life += 1
                            score( s = 1)
                        except:
                            len(all_food) < 1

    def border():
        for d in dot:
            try:
                if d.x > 795:
                    d.x -= 1

                if d.x < 5:
                    d.x += 1

                if d.y > 595:
                    d.y -= 1

                if d.y < 5:
                    d.y += 1
            except:
                len(dot) < 1
        
        

#gettin everything to show on screen
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

    if score_draw:
        snl = score_now_label
        snl.text = f'Score {score_now:08d}'
        snl.font_size = game_window.height//30
        snl.draw()

        sbl = score_best_label
        sbl.text = f'Best {score_best:08d}'
        sbl.font_size = game_window.height//30
        sbl.x = game_window.width
        sbl.draw()
#spawns food if the number of food is less than n
def spawn_food(dt):
    if len(all_food) < 5:
        all_food.append(Food.get_food())

    else:
        pass
def spawn_life(dt):
    if len(dot) < 3:
        dot.append(life())

def movement(dt):
    global time_sum, time_min
    Movement.border() 
    Movement.hunt()
    Movement.rng_move()
    time_sum += dt

if __name__ == "__main__":
    # Start it up!

    # Update the game 120 times per second

    clock.schedule_interval(movement, 1/60)
    clock.schedule_interval(spawn_life, randint(0, 10))
    #spawns the food at random intervals
    clock.schedule_interval(spawn_food, randint(0, 3))
    # Tell pyglet to do its thing
    app.run()