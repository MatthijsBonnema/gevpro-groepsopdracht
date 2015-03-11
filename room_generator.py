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
        self.setrooms()
        self.chance = 20  # in %
        self.getrooms()

    def __str__(self):
        return str(self.getrooms())

    def setrooms(self):
        """Creates a list with rooms"""
        for y in range(1, 5):
            for x in range(1, 6):
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