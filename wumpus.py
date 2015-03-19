#!/usr/bin/python3
# File: wumpus.py
# Author: Tomer Gabay
# Date: 03/11/15
# Info:

from random import randrange


class Wumpus:
    def __init__(self, heroPosition):
        self.heroXCor = heroPosition[0]
        self.heroYCor = heroPosition[1]
        self.spawn()
        
    def spawn(self):
        self.xCor = randrange(1, 6)
        self.yCor = randrange(1, 5)
        while abs(self.xCor - self.heroXCor) < 2:
            self.xCor = randrange(1, 6)
        while abs(self.yCor - self.heroYCor) < 2:
            self.yCor = randrange(1, 5)
        self.updateposition()
        
    def updateposition(self):
        self.position = (self.xCor, self.yCor)
    
    def hunt(self):
        """Makes Wumpus move towards hero in fastest way possible"""
        #calculates fastest route X-wise
        absXDistance = self.xCor - self.heroXCor  # abs for absolute
        
        if absXDistance > 0:
            relXDistance = abs(5 - self.xCor + self.heroXCor)  # rel for relative
        elif absXDistance < 0:
            relXDistance = abs(5 - self.heroXCor + self.xCor)
        else:
            relXDistance = 0
        absXDistance = abs(absXDistance)
        if absXDistance <= relXDistance:
            shortestXDistance = absXDistance
        else:
            shortestXDistance = relXDistance
            
        #calculates fastest route Y-wise
        absYDistance = self.yCor - self.heroYCor
        
        if absYDistance > 0:
            relYDistance = abs(4 - self.yCor + self.heroYCor)  # #####
        elif absYDistance < 0:
            relYDistance = abs(4 - self.heroYCor + self.yCor)  # #####
        else:
            relYDistance = 0
        absYDistance = abs(absYDistance)
        if absYDistance <= relYDistance:
            shortestYDistance = absYDistance
        else:
            shortestYDistance = relYDistance
        
        # movement of Wumpus
        if shortestXDistance >= shortestYDistance and shortestXDistance != 0:  # makes Wumpus move diagonal
            if self.xCor - self.heroXCor > 0:
                if relXDistance < absXDistance:
                    self.xCor = self.xCor + 1
                else:
                    self.xCor = self.xCor - 1
            else:
                if relXDistance < absXDistance:
                    self.xCor = self.xCor - 1
                else:
                    self.xCor = self.xCor + 1
        if shortestXDistance < shortestYDistance and shortestYDistance != 0:
            if self.yCor - self.heroYCor > 0:
                if relYDistance < absYDistance:
                    self.yCor = self.yCor + 1
                else:
                    self.yCor = self.yCor - 1
            else:
                if relYDistance < absYDistance:
                    self.yCor = self.yCor - 1
                else:
                    self.yCor = self.yCor + 1
                    
        #keep wumpus within map-range
        if self.xCor > 5: 
            self.xCor = 1
        if self.xCor < 1:
            self.xCor = 5
        if self.yCor > 4:
            self.yCor = 1
        if self.yCor < 1:
            self.yCor = 4
            
        self.updateposition()
        
    def getposition(self):
        return self.position
        
    def __str__(self):
        return "Wumpus at {}".format(self.position)
