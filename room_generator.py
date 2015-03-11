#!/usr/bin/python3
# File: room_generator.py
# Author: Matthijs Bonnema
# Date: 3/11/15
# Info: 

from random import randrange

class RoomGenerator():
    def __init__(self):
        self.rooms = []
        self.setrooms()
        self.chance = 20
        self.getrooms()

    def __str__(self):
        return str(self.getrooms())

    def setrooms(self):
        for y in range(1, 5):
            for x in range(1, 6):
                self.rooms.append([(x, y), None])
        return self.rooms

    def getrooms(self):
        for room in self.rooms:
            whatitem = randrange(0, 3)

            if randrange(0, 101) <= self.chance:
                if whatitem == 0:
                    room[1] = "bat"
                elif whatitem == 1:
                    room[1] = "gold"
                else:
                    room[1] = "pit"
        return self.rooms