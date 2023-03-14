import random

while True:
    dice1 = 0
    dice2 = 0

    throws = 0

    sides = int(input('How many sides?'))

    while throws < 10**7:
        dice1 += max(int(random.random()*sides)+1, int(random.random()*sides)+1)
        throws +=1

    average = dice1/throws

    print(average)