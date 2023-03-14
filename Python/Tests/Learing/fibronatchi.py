from time import sleep
import matplotlib
from matplotlib import figure


def fibro(n):
    start_num = n
    num = 1
    prev_num = start_num
    while True: 
        if start_num == 0:
            start_num +=  1
        else:
            pass
        
        while start_num == 0:
            first_seq = start_num + num
        
        num += prev_num + num

        print(num)
        sleep(0.5)
        
    
fibro(0 )

    