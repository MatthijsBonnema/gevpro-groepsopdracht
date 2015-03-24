#!/usr/bin/python3
# File: hero.py
# Author: Tomer Gabay
# Date: 03/24/15
# Info:

from random import randrange

class Hero:
	def __init__(self, name):
		self.name = name
		self.gold = 0
		self.arrows = 4
		self.path = []
		self.arPath = [""] #follows path of arrow, not empty so [-1] works
		self.arDir = [""] #follows direction of arrow not empty so [-1] works
		self.spawn()
		self.victory = False

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

	def shoot(self, poswumpus):
		"""Sets current position of arrows"""
		self.poswumpus = poswumpus
		self.arXcor = self.xCor
		self.arYcor = self.yCor

	def shootup(self):
		self.arYcor -= 1
		if self.arDir[-1] == "down":
			del self.arDir[-1]
			del self.arPath[-1]
		else:
			self.arDir.append('up')
			if self.arYcor < 1:
				self.arYcor = 4
			self.arPath.append((self.arXcor, self.arYcor))
			self.postshootupdate()

	def shootleft(self):
		self.arXcor -= 1
		if self.arDir[-1] == "right":
			del self.arDir[-1]
			del self.arPath[-1]
		else:
			self.arDir.append('left')
			if self.arXcor < 1:
				self.arXcor = 5
			self.arPath.append((self.arXcor, self.arYcor))
			self.postshootupdate()

	def shootright(self):
		self.arXcor += 1
		if self.arDir[-1] == "left":
			del self.arDir[-1]
			del self.arPath[-1]
		else:
			self.arDir.append('right')
			if self.arXcor > 5:
				self.arXcor = 1
			self.arPath.append((self.arXcor, self.arYcor))
			self.postshootupdate()

	def shootdown(self):
		self.arYcor += 1
		if self.arDir[-1] == "up":
			del self.arDir[-1]
			del self.arPath[-1]
		else:
			self.arDir.append('down')
			if self.arYcor > 4:
				arYcor = 1
			self.arPath.append((self.arXcor, self.arYcor))
			self.postshootupdate()

	def postshootupdate(self):
		"""resets path and direction and substracts an arrow if shot is over"""
		# self.victory = False
		if len(self.arPath) == 6:
			self.arrows -= 1
			print(self.poswumpus, self.arPath)
			if self.poswumpus in self.arPath:
				self.victory = True
			self.arPath = [""]
			self.arDir = [""]
			print("Status:", self.victory)
			return self.arrows, self.victory

	def getVictory(self):
		return self.victory




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
