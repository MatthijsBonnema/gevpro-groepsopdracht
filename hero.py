#!/usr/bin/python3
# File: hero.py
# Author: Tomer Gabay
# Date: 3/11/15
# Info:

from random import randrange


class Hero:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.arrows = 4
        self.path = []
        self.spawn()

    def __str__(self):
        return "Name: {} Position:{} Gold:{} Arrows:{} Steps: {}".format(self.name, self.position, self.gold, self.arrows, len(self.path))

    def spawn(self):
        self.xCor = randrange(1, 6)
        self.yCor = randrange(1, 5)
        self.updateposition()

    def setwumpuspos(self, poswumpus):
        self.poswumpus = poswumpus

    def respawn(self):
        self.xCor = randrange(1, 6)
        self.yCor = randrange(1, 5)
        if (self.xCor, self.yCor) != self.poswumpus:
            self.updateposition()
        else:
            self.respawn()


    def getposition(self):
        return self.xCor, self.yCor

    def getname(self):
        return self.name

    def getgold(self):
        return self.gold

    def getarrows(self):
        return self.arrows

    def foundgold(self):
        self.gold += 1
        return self.gold
        
    def shoot(self):
        self.arrows -= 1
        return self.arrows

    def move(self, moveto):
        if moveto == "up":
            self.moveup()
            return True
        elif moveto == "down":
            self.movedown()
            return True
        elif moveto == "left":
            self.moveleft()
            return True
        elif moveto == "right":
            self.moveright()
            return True
        else:
            return False
        
    def moveup(self):
        self.yCor -= 1  # due to inverted coordinates of UI
        if self.yCor < 1:
            self.yCor = 4
        print("debug")
        self.updateposition()
        
    def moveright(self):
        self.xCor += 1
        if self.xCor > 5:
            self.xCor = 1
        self.updateposition()
        
    def movedown(self):
        self.yCor += 1  # due to inverted coordinates of UI
        if self.yCor > 4:
            self.yCor = 1
        self.updateposition()
    
    def moveleft(self): 
        self.xCor -= 1
        if self.xCor < 1:
            self.xCor = 5
        self.updateposition()
        
    def updateposition(self):
        self.position = (self.xCor, self.yCor)
        self.path.append(self.position)
        return self.position
    
    def getpath(self):
        return self.path
