
import math
from random import randint
import pyglet
from pyglet import shapes, clock, sprite, image, resource, app, text
from pyglet.gl import *


#main settings
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

batch = pyglet.graphics.Batch()

score_draw = True
score_now = score_best = 0
score_now_label = text.Label()
score_best_label = text.Label( anchor_x='right' )

time_sum = 0
time_min = 1/60*0.9



def score( s=0 ):
    global score_draw, score_now, score_best
    
    score_draw = True
    score_now = max( 0, score_now+s )
    score_best = max( score_now, score_best )

    return score_now
dot = []
enemy = []
def create_obj(radius, r, g, b):
    x = randint(0, game_window.width-10)
    y = randint(0, game_window.height-10)
    return shapes.Circle(x, y, radius, color=[r, g, b], batch=main_batch)

#the being
def life():
    global dot_life
    r = randint(50, 125)
    g = randint(75, 255)
    b = randint(75, 255)

    dots = create_obj(7, r, g, b)

    for d in dot:
        dot_life = randint(40, 100)
        dot_life -= time_sum

        if dot_life < 1:
            dot.remove(d)

    return dots

def enemies():
    r = randint(100, 255)
    g = randint(75, 200)
    b = randint(50, 75)

    enemy = create_obj(8, r, g, b)
    return enemy


#to store the food generated
all_food = []
#the dot



#food generator
def get_food():
    gen_food = create_obj(3, 255, 20, 20)
    return gen_food

class Movement:
    #just to check movement. rendunant code. remove or eddit
    def rng_move():
    
       

        for d in dot:
            x_i = randint(0, 3)
            y_i = randint(0, 3)

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

        for do in dot:
            t = None
            t_d = float('inf')
            if t == None:
                for e in all_food:
                    d = math.dist( (do.x, do.y), (e.x, e.y) )

                    if d < t_d:
                        t_d = d
                        t = e

            if t:

                if t_d > 1:
                    try:
                        if t.x < do.x:
                            do.x -= math.pi / math.atan(t.x)
                        if t.y < do.y:
                            do.y -= math.pi / math.atan(t.y)
                        if t.x > do.x:
                            do.x += math.pi / math.atan(t.x)
                        if t.y > do.y:
                            do.y += math.pi / math.atan(t.y)
                    except:
                        len(dot) < 1
    
                if t_d < 7:
                    try:
                        all_food.remove(t)
                        do.dot_life += 40
                        score( s = 1)
                    except:
                        len(all_food) < 1

            else:
                pass

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

#spawns food if the number of food is less than n
def spawn_food(dt):
    if len(all_food) < 50:
        all_food.append(get_food())

def spawn_life(dt):
    if len(dot) < 16:
        dot.append(life())

    if len(dot) > 3 and len(enemy) < 2:
        enemy.append(enemies())

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
    clock.schedule_interval(spawn_life, 1)
    #spawns the food at random intervals
    clock.schedule_interval(spawn_food, 1/3)
    # Tell pyglet to do its thing
    app.run()