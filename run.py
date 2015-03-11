#!/usr/bin/python3
# File: run.py.py
# Author: Matthijs Bonnema
# Date: 3/11/15
# Info: 

import sys
from room_generator import RoomGenerator
from hero import Hero


def main():
    # name = input("What is your name?\n")
    name = "test"

    hunter = Hero(name)
    spawn = hunter.getposition()

    rooms = RoomGenerator(spawn)


if __name__ == "__main__":
    main()