import time

global ctb

ctb = False

txts = ['Can the Elf touch the butt?\n', '''Elf touches butt c:\n''', 'Call da police\n', 'Error!: Input not recognized \n', 'Dumb human. Try again\n \n']
txt_add = []

def touch_butt(txt):
    global ctb
    print(txt[0])
    ctb_input = input('Yes or No?\n')
    if ctb_input.lower() == 'yes' or ctb_input.lower() == 'y':
        print(txt[1])
        time.sleep(3)
        ctb = True

    elif ctb_input.lower() == 'no' or ctb_input.lower() == 'n':
        ctb = False
        print(txt[2])
        print('\n')

    else:
        ctb = False
        print(txt[3])
        time.sleep(2)
        print(txt[4])

while ctb == False:
    touch_butt(txts)