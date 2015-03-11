#!/usr/bin/python3
# File: room_generator.py
# Author: Matthijs Bonnema
# Date: 3/11/15
# Info: 

# rooms = [((xCor, yCor), item), ((xCor, yCor), item), ((xCor, yCor), item), ..
#


import sys
from random import randrange

class RoomGenerator():
    def __init__(self):
        self.rooms = []
        self.getrooms()

    def __str__(self):
        return self.getrooms()

    def getrooms(self):


        for i in range(20):
            if randrange(0, 10) <= 1:
                print(randrange(0,10))



if __name__ == "__main__":
    RoomGenerator()