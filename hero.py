from random import randrange
class Hero:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.arrows = 4
        self.path = []
        self.spawn()
        
    def spawn(self):
        self.xCoor = int(randrange(1,6))
        self.yCoor = (randrange(1,5))
        self.updateposition()
        
    def foundgold(self):
        self.gold = self.gold + 1
        return self.gold
        
    def shoot(self):
        self.arrows = self.arrows - 1
        return self.arrows
        
    def moveup(self):
        self.yCoor = self.yCoor - 1 #due to coordinates of UI
        if self.yCoor < 1:
            self.yCoor = 4
        self.updateposition()
        
    def moveright(self):
        self.xCoor = self.xCoor + 1
        if self.xCoor > 5:
            self.xCoor = 1
        self.updateposition()
        
    def movedown(self):
        self.yCoor = self.yCoor + 1 #due to coordinates of UI
        if self.yCoor > 4:
            self.yCoor = 1
        self.updateposition()
    
    def moveleft(self): 
        self.xCoor = self.xCoor - 1  
        if self.xCoor < 1:
            self.xCoor = 5
        self.updateposition()
        
    def updateposition(self):
        self.position = (self.xCoor, self.yCoor)
        self.path.append(self.position)
        return self.position
    
    def getpath(self):
        return self.path
    
    def __str__(self):
        return "Name: {} Position:{} Gold:{} Arrows:{} Steps: {}".format(self.name,self.position, self.gold, self.arrows, len(self.path))
        
        
        
    
