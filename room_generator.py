#!/usr/bin/python3
# File: room_generator.py
# Author: Matthijs Bonnema
# Date: 3/11/15
# Info: 

from random import randrange


class RoomGenerator():
    """Creates a list with coordinates and possibly a bat, gold or a pit"""
    def __init__(self):
        self.rooms = []
        self.xrooms = 5  # + 1 due coordinates
        self.yrooms = 6   # + 1 due coordinates
        self.setrooms()
        self.chance = 20  # in %
        self.getrooms()

    def __str__(self):
        """returns a string with all the rooms + items"""
        return str(self.getrooms())

    def setchance(self, chance):
        """Set the chance for items"""
        self.chance = chance

    def getchance(self):
        """Returns the chance on items"""
        return self.chance

    def setxy(self, x, y):
        """Set the amount of rooms in x and y"""
        self.xrooms = x + 1  # + 1 due coordinates
        self.yrooms = y + 1  # + 1 due coordinates

    def getxy(self):
        """Returns the amount of rooms in x and y"""
        return self.xrooms - 1, self.yrooms - 1  # - 1 due coordinates

    def setrooms(self):
        """Creates a list with rooms"""
        for y in range(1, self.xrooms):
            for x in range(1, self.yrooms):
                self.rooms.append([(x, y), None])

    def getrooms(self):
        """Gives a bat, gold or a pit to the rooms"""
        for room in self.rooms:
            whatItem = randrange(0, 3)

            if randrange(0, 101) <= self.chance:
                if whatItem == 0:
                    room[1] = "bat"
                elif whatItem == 1:
                    room[1] = "gold"
                else:
                    room[1] = "pit"