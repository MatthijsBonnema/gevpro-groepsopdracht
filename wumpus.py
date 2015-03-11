from random import randrange

class Wumpus:
    def __init__(self, heroPosition):
        self.heroXCoor = heroPosition[0]
        self.heroYCoor = heroPosition[1]
        self.spawn()
        
    def spawn(self):
        self.xCoor = randrange(1,6)
        self.yCoor = randrange(1,5)
        while abs(self.xCoor - self.heroXCoor) < 2:
            self.xCoor = randrange(1,6)
        while abs(self.yCoor - self.heroYCoor) < 2:
            self.yCoor = randrange(1,5)
        self.updateposition()
        
    def updateposition(self):
        self.position = (self.xCoor, self.yCoor)
    
    def hunt(self):
        """Makes Wumpus move towards hero in fastest way possible"""
        #calculates fastest route X-wise
        absXDistance = self.xCoor - self.heroXCoor #abs for absolute
        
        if absXDistance > 0:
            relXDistance = abs(5 - self.xCoor + self.heroXCoor) #rel for relative
        elif absXDistance < 0:
            relXDistance = abs(5 - self.heroXCoor + self.xCoor)
        else:
            relXDistance = 0
        absXDistance = abs(absXDistance)
        if absXDistance <= relXDistance:
            shortestXDistance = absXDistance
        else:
            shortestXDistance = relXDistance
            
        #calculates fastest route Y-wise
        absYDistance = self.yCoor - self.heroYCoor
        
        if absYDistance > 0:
            relYDistance = abs(4 - self.yCoor + self.heroYCoor) ######
        elif absYDistance < 0:
            relYDistance = abs(4 - self.heroYCoor + self.yCoor) ######
        else:
            relYDistance = 0
        absYDistance = abs(absYDistance)
        if absYDistance <= relYDistance:
            shortestYDistance = absYDistance
        else:
            shortestYDistance = relYDistance
        
        #movement of Wumpus
        if shortestXDistance >= shortestYDistance and shortestXDistance != 0: #makes Wumpus move diagonal
            if self.xCoor - self.heroXCoor > 0:
                if relXDistance < absXDistance:
                    self.xCoor = self.xCoor + 1
                else:
                    self.xCoor = self.xCoor - 1
            else:
                if relXDistance < absXDistance:
                    self.xCoor = self.xCoor - 1
                else:
                    self.xCoor = self.xCoor + 1
        if shortestXDistance < shortestYDistance and shortestYDistance != 0:
            if self.yCoor - self.heroYCoor > 0:
                if relYDistance < absYDistance:
                    self.yCoor = self.yCoor + 1
                else:
                    self.yCoor = self.yCoor - 1
            else:
                if relYDistance < absYDistance:
                    self.yCoor = self.yCoor - 1
                else:
                    self.yCoor = self.yCoor + 1
                    
        #keep wumpus within map-range
        if self.xCoor > 5: 
            self.xCoor = 1
        if self.xCoor < 1:
            self.xCoor = 5
        if self.yCoor > 4:
            self.yCoor = 1
        if self.yCoor < 1:
            self.yCoor = 4
            
        self.updateposition()
        
    def getposition(self):
        return self.position
        
    def __str__(self):
        return "Wumpus at {}".format(self.position)
        
    
        
        
    
        
        
