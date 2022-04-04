import argparse
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import random as rng
from time import sleep

plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams['figure.autolayout'] = True

x = rng.randint(-10, 10)
y = rng.randint(-10, 10)

plt.xlim(-11, 11)
plt.ylim(-11, 11)

plt.xticks(np.arange(-10, 11, step=1))
plt.yticks(np.arange(-10, 11, step=1))

plt.grid()

class Unit:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def spawn():

        plt.plot(
            x, y,
            marker='o',
            markersize=10,
            markeredgecolor='blue',
            markerfacecolor='red'
            )
        plt.show()
        

class Movement:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_x(self, x):
        num = 0
        while True:
            num = rng.randint(0, 1)

            if num == 1:
                x += 1
            else:
                x -= 1
            
            sleep(1)
                
    def move_y(self, y):
        num = 0
        while True:
            num = rng.randint(0, 1)

            if num == 1:
                y += 1
            else:
                y -= 1
            
            sleep(1.5)

class Life:
    
    unit = Unit.spawn

    movex = Movement.move_x

    movey = Movement.move_y

    def move(unit, movex, movey):
        unit = plt.plot(
            x=movex,
            y=movey
        )
        plt.show()

Unit.spawn()

sleep(4)

Life.move()
