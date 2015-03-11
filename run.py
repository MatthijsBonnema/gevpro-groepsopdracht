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
    spawn = hunter.getposition()
    rooms = RoomGenerator(spawn)

    print("Welcome {}".format(hunter.getname()))




if __name__ == "__main__":
    main()