#!/usr/bin/python3
# File: run.py.py
# Author: Matthijs Bonnema
# Date: 3/11/15
# Info: 

import sys
from room_generator import RoomGenerator
from hero import Hero
from wumpus import Wumpus


def main():
    name = input("Welcome Hunter!\nBefore we start the Journey, what is your name?\n")

    hunter = Hero(name)
    spawnHunter = hunter.getposition()
    spawnHunter = hunter.getposition()

    wumpus = Wumpus(spawnHunter)
    spawnWumpus = wumpus.getposition()



    rooms = RoomGenerator(spawnHunter, spawnWumpus)



    print("Welcome {}\n".format(hunter.getname()))

    alive = True

    while alive:

        items = []

        # check if something is near
        xCor, yCor = hunter.getposition()

        if hunter.getposition()[0] == 1:
            positionCheck = [(xCor, yCor + 1), (xCor, 5), (xCor + 1, yCor), (xCor - 1, yCor)]
            positionCheckWumpus = [(xCor, yCor + 1), (xCor, 5), (xCor + 1, yCor), (xCor - 1, yCor)]
        elif hunter.getposition()[0] == 5:
            positionCheck = [(xCor, yCor + 1), (xCor, yCor - 1), (1, yCor), (xCor - 1, yCor)]
            positionCheckWumpus = [(xCor, yCor + 1), (xCor, yCor - 1), (1, yCor), (xCor - 1, yCor)]
        elif hunter.getposition()[1] == 1:
            positionCheck = [(xCor, yCor + 1), (xCor, 4), (xCor + 1, yCor), (xCor - 1, yCor)]
            positionCheckWumpus = [(xCor, yCor + 1), (xCor, 4), (xCor + 1, yCor), (xCor - 1, yCor)]
        elif hunter.getposition()[1] == 4:
            positionCheck = [(xCor, 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]
            positionCheckWumpus = [(xCor, 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]
        else:
            positionCheck = [(xCor, yCor + 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]
            positionCheckWumpus = [(xCor, yCor + 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]

        turn = False

        if wumpus.getposition() in positionCheckWumpus:
            print("Wumpy is nearby :O")

        for coordinates in rooms.showrooms():
            if coordinates[0] in positionCheck:
                items.append(coordinates[1])
        if "gold" in items:
            print("There is gold near you!\n")
        if "bat" in items:
            print("Bats nearby\n")
        if "pit" in items:
            print("I feel a draft\n")

        notTurn = True

        while notTurn:
            action = input("Do you want to move or shoot?\n")
            if action.lower() == "move" or action.lower() == "shoot":
                notTurn = False
            else:
                print("Not a valid input, use move or shoot test")


        if action.lower() == "move":
            moveto = input("\nPlease select your move Hunter. up, down, left or right?\n")
            move = hunter.move(moveto)

            print("debug1")

            if not move:  # if move == False
                print("Not a valid input!\n")
            else:
                print("You moved {}!\n".format(moveto))

                for room in rooms.showrooms():
                    if hunter.getposition() == room[0]:
                        if room[1] == "pit":
                            print("You stepped on a {}\n".format(room[1]))
                            print("You died!\n")
                            # alive = False
                        elif room[1] == "gold":
                            print("You stepped on a {}\n".format(room[1]))
                            hunter.foundgold()
                        elif room[1] == "bat":
                            print("You stepped on a {}\nThe bat took you, and dropped you in a random room!".format(room[1]))
                            hunter.setwumpuspos(wumpus.getposition())
                            hunter.respawn()
        elif action.lower() == "shoot":
            print("pew pew pew")

        if alive:
            if hunter.getposition() == wumpus.getposition():
                print("You have been eaten by Wumpy")
                alive = False
            if alive:
                wumpus.hunt()

                if hunter.getposition() == wumpus.getposition():
                    print("You have been eaten by Wumpy")
                    alive = False
        print(wumpus.getposition())
        print(hunter.getposition())


    print("You found {} gold".format(hunter.getgold()))
    print("You had {} arrows left".format(hunter.getarrows()))


if __name__ == "__main__":
    main()