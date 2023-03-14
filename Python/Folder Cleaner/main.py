import os

for root, dirs, files in os.walk("", topdown=False):
    for dir in dirs:
        if dir.startswith(dir):
            filepath = os.path.join(root, dir)  
            print (filepath)