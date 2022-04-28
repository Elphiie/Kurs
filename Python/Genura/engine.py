import math
from random import randint
from objects import all_food
from main import dot

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

            
            if d < target_d:
                target, target_d = e, d

            if target.x > dot.x:
                dot.x += target.x / 800

            if target.y > dot.y:
                dot.y += target.y / 600
            
            if target.x < dot.x:
                dot.x -= target.x / 800
            
            if target.y < dot.y:
                dot.y -= target.y / 600