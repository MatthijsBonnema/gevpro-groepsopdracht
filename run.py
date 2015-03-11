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



    print("Welcome {}\n".format(hunter.getname()))

    alive = True

    while alive:

        items = []

        # check if something is near
        xCor, yCor = hunter.getposition()
        positioncheck = [(xCor, yCor + 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]

        for coordinates in rooms.showrooms():
            if coordinates[0] in positioncheck:
                items.append(coordinates[1])
        if "gold" in items:
            print("There is gold near you!\n")
        if "bat" in items:
            print("Bats nearby\n")
        if "pit" in items:
            print("I feel a draft\n")

        action = input("Do you want to move or shoot?\n")

        if action.lower() == "move":
            moveto = input("\nPlease select your move Hunter. up, down, left or right?\n")
            move = hunter.move(moveto)

            if move == False:
                print("Not a valid input!\n")
            else:
                print("You moved {}!\n".format(moveto))
                for room in rooms.showrooms():
                    if hunter.getposition() == room[0]:
                        if room[1] == "pit":
                            print("You stepped on a {}\n".format(room[1]))
                            alive = False
                        elif room[1] == "gold":
                            print("You stepped on a {}\n".format(room[1]))
                            hunter.foundgold()
                        elif room[1] == "bat":
                            print("You stepped on a {}\n".format(room[1]))
                            alive = False
        elif action.lower() == "shoot":
            continue  # add shoot action
        else:
            print("Not a valid input, use move or shoot")

    print("You died!\n")
    print("You found {} gold".format(hunter.getgold()))
    print("You had {} arrows left".format(hunter.getarrows()))


if __name__ == "__main__":
    main()