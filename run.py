#!/usr/bin/python3
# File: run.py.py
# Author: Matthijs Bonnema
# Date: 3/11/15
# Info: 

import sys
from room_generator import RoomGenerator
from hero import Hero


def main():
    name = input("Welcome Hunter!\nBefore we start the Journey, what is your name?\n")

    hunter = Hero(name)
    spawnHunter = hunter.getposition()

    # wumpus = Wumpus(spawnHunter)

    spawnHunter = hunter.getposition()
    # spawnWumpus = wumpus.getposition()

    spawnWumpus = (1, 1)

    rooms = RoomGenerator(spawnHunter, spawnWumpus)



    print("Welcome {}".format(hunter.getname()))

    alive = True

    while alive:
        moveto = input("Please select your move Hunter. up, down, left or right?\n")
        move = hunter.move(moveto)
        if move == False:
            print("Not a valid input!")
        else:
            print("You moved {}!".format(moveto))


if __name__ == "__main__":
    main()