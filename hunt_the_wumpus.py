#!/usr/bin/python3
# File: hunt_the_wumpus.py
# Author: Matthijs Bonnema
# Date: 03/20/15
# Info:


from PyQt4 import QtCore, QtGui
import sys
import os
from room_generator import RoomGenerator
from hero import Hero
from wumpus import Wumpus
from time import sleep
import highscore
import start_UI

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.moveturn = False
        self.distance = 0
        self.setupUi(self)

    def keyPressEvent(self, event):
        """Checks for keys being pressed"""
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_W:
                self.eventHandler("up")
            if event.key() == QtCore.Qt.Key_S:
                self.eventHandler("down")
            if event.key() == QtCore.Qt.Key_A:
                self.eventHandler("left")
            if event.key() == QtCore.Qt.Key_D:
                self.eventHandler("right")
            if event.key() == QtCore.Qt.Key_Space:
                self.eventHandler("shoot")
            if event.key() == QtCore.Qt.Key_M:
                self.eventHandler("move")
            if event.key() == QtCore.Qt.Key_Escape:
                self.eventHandler("continue")

        else:
            event.ignore()  # If no key is pressed, ignore the event.

    def eventHandler(self, event):
        """Handles the events coming from the buttons and the keys"""
        if self.workThread.alive:
            if event == "up":
                if self.moveturn:  # If move turn is True, move the Hero, else move the arrow.
                    self.movehero("up")
                if self.shootturn:
                    self.movearrow("up")
            if event == "down":
                if self.moveturn:
                    self.movehero("down")
                if self.shootturn:
                    self.movearrow("down")
            if event == "left":
                if self.moveturn:
                    self.movehero("left")
                if self.shootturn:
                    self.movearrow("left")
            if event == "right":
                if self.moveturn:
                    self.movehero("right")
                if self.shootturn:
                    self.movearrow("right")
            if event == "shoot":  # If the event is shoot, start the shooting function
                self.hunter.shoot(self.wumpus.position)
                self.workThread.action = "shoot"
            if event == "move":  # If the event is move, start the moving function
                self.workThread.action = "move"
        else:
            if event == "continue":  # If the event is continue, restart the program.
                python = sys.executable
                os.execl(python, python, * sys.argv)

    def eventHandlerRight(self):
        """Allows the workThread to set the eventHandler"""
        self.eventHandler("right")

    def eventHandlerLeft(self):
        """Allows the workThread to set the eventHandler"""
        self.eventHandler("left")

    def eventHandlerUp(self):
        """Allows the workThread to set the eventHandler"""
        self.eventHandler("up")

    def eventHandlerDown(self):
        """Allows the workThread to set the eventHandler"""
        self.eventHandler("down")

    def setupUi(self, Form):
        """Sets up the UI of the game"""
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1200, 900)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setFont(font)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.down = QtGui.QPushButton(Form)
        self.down.setFont(font)
        self.down.setObjectName(_fromUtf8("down"))
        self.gridLayout_4.addWidget(self.down, 2, 10, 1, 1)
        self.up = QtGui.QPushButton(Form)
        self.up.setFont(font)
        self.up.setObjectName(_fromUtf8("up"))
        self.gridLayout_4.addWidget(self.up, 1, 10, 1, 1)
        self.move = QtGui.QPushButton(Form)
        self.move.setFont(font)
        self.move.setObjectName(_fromUtf8("move"))
        self.gridLayout_4.addWidget(self.move, 1, 8, 1, 1)
        self.right = QtGui.QPushButton(Form)
        self.right.setFont(font)
        self.right.setObjectName(_fromUtf8("right"))
        self.gridLayout_4.addWidget(self.right, 2, 11, 1, 1)
        self.arrows_amount = QtGui.QLCDNumber(Form)
        self.arrows_amount.setObjectName(_fromUtf8("arrows_amount"))
        self.gridLayout_4.addWidget(self.arrows_amount, 0, 11, 1, 1)
        self.arrows = QtGui.QLabel(Form)
        self.arrows.setFont(font)
        self.arrows.setObjectName(_fromUtf8("arrows"))
        self.gridLayout_4.addWidget(self.arrows, 0, 10, 1, 1)
        self.shoot = QtGui.QPushButton(Form)
        self.shoot.setFont(font)
        self.shoot.setObjectName(_fromUtf8("shoot"))
        self.gridLayout_4.addWidget(self.shoot, 2, 8, 1, 1)
        self.Gold = QtGui.QLabel(Form)
        self.Gold.setFont(font)
        self.Gold.setObjectName(_fromUtf8("Gold"))
        self.gridLayout_4.addWidget(self.Gold, 0, 8, 1, 1)
        self.left = QtGui.QPushButton(Form)
        self.left.setFont(font)
        self.left.setObjectName(_fromUtf8("left"))
        self.gridLayout_4.addWidget(self.left, 2, 9, 1, 1)
        self.gold_amount = QtGui.QLCDNumber(Form)
        self.gold_amount.setObjectName(_fromUtf8("gold_amount"))
        self.gridLayout_4.addWidget(self.gold_amount, 0, 9, 1, 1)
        self.InfoLabel = QtGui.QLabel(Form)
        self.InfoLabel.setObjectName(_fromUtf8("InfoLabel"))
        self.gridLayout_4.addWidget(self.InfoLabel, 0, 4, 1, 4)
        self.GoldLabel = QtGui.QLabel(Form)
        self.GoldLabel.setObjectName(_fromUtf8("GoldLabel"))
        self.gridLayout_4.addWidget(self.GoldLabel, 1, 4, 1, 2)
        self.PitLabel = QtGui.QLabel(Form)
        self.PitLabel.setObjectName(_fromUtf8("PitLabel"))
        self.gridLayout_4.addWidget(self.PitLabel, 2, 4, 1, 2)
        self.BatLabel = QtGui.QLabel(Form)
        self.BatLabel.setObjectName(_fromUtf8("BatLabel"))
        self.gridLayout_4.addWidget(self.BatLabel, 1, 6, 1, 2)
        self.EmptyLabel = QtGui.QLabel(Form)
        self.EmptyLabel.setObjectName(_fromUtf8("EmptyLabel"))
        self.gridLayout_4.addWidget(self.EmptyLabel, 2, 6, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.InfoLabel.setFont(font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """Constructs the buttons with text etc, and starts the setup of the game."""
        Form.setWindowTitle(_translate("Form", "Hunt the Wumpus", None))

        # Set the text of the Buttons

        self.move.setText(_translate("Form", "Move", None))
        self.shoot.setText(_translate("Form", "Shoot", None))

        self.right.setText(_translate("Form", "Right", None))
        self.up.setText(_translate("Form", "Up", None))
        self.left.setText(_translate("Form", "Left", None))
        self.down.setText(_translate("Form", "Down", None))

        self.arrows.setText(_translate("Form", "Arrows", None))
        self.Gold.setText(_translate("Form", "Gold", None))

        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setSceneRect(1, 4, 5, 4)
        self.graphicsView.scale(1, -1)


        self.graphicsView.setStyleSheet("border: 0px")

        # Creates the map

        self.rooms = QtGui.QGraphicsPixmapItem()
        self.rooms.setPixmap(QtGui.QPixmap("rooms.png"))
        self.rooms.setPos(-587, -387)
        self.scene.addItem(self.rooms)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)

        self.graphicsView.setScene(self.scene)

        # Ask for the name of the player, incase none is set; Anonymous.

        name, ok = QtGui.QInputDialog.getText(self, 'Hunt the Wumpus', 'Before we start Hunter, what is your name?\n')
#        name = "test"
        if name == "":
            name = "Anonymous"

        self.setConsoleMessage("info", "Welcome to Hunt the Wumpus v1.0")

        self.hunter = Hero(name)  # Start hunter class

        hunterx, huntery = self.coordConverter(self.hunter.getposition())
        self.sethero(hunterx, huntery)
        self.setLastDirection()
        self.setarrow()

        self.wumpus = Wumpus(self.hunter.getposition())  # Set the Wumpus class
        self.roomsmap = RoomGenerator(self.hunter.getposition(), self.wumpus.getposition())  # Creates the rooms with and without "Items"

        # Links the buttons to the eventHandler

        self.right.clicked.connect(self.eventHandlerRight)
        self.left.clicked.connect(self.eventHandlerLeft)
        self.up.clicked.connect(self.eventHandlerUp)
        self.down.clicked.connect(self.eventHandlerDown)
        self.move.clicked.connect(self.eventHandlerMove)
        self.shoot.clicked.connect(self.eventHandlerShoot)

        # Start the workThread

        self.workThread = WorkerThread()
        self.workThread.start()

        # Receive signals, most of them out of the workThread

        self.connect(self.workThread, QtCore.SIGNAL("action"), self.actionreset, QtCore.Qt.DirectConnection)
        self.connect(self.workThread, QtCore.SIGNAL("gold"), self.setgold, QtCore.Qt.DirectConnection)
        self.connect(self.workThread, QtCore.SIGNAL("arrow"), self.setArrowAmount, QtCore.Qt.DirectConnection)
        self.connect(self, QtCore.SIGNAL("setarrow"), self.resetarrow, QtCore.Qt.DirectConnection)
        self.connect(self, QtCore.SIGNAL("removearrow"), self.hidearrow, QtCore.Qt.DirectConnection)

    def setgold(self):
        """Set the amount of gold in the label"""
        self.hunter.foundgold()
        gold = self.hunter.getgold()
        self.gold_amount.display(gold)

    def actionreset(self):
        """Reset the action variable in the workThread"""
        self.workThread.action = None

    def setArrowAmount(self):
        """Set the amount of arrows in the label"""
        arrows = self.hunter.getarrows()
        self.arrows_amount.display(arrows)

    def eventHandlerMove(self):
        """Allows the workThread to control the eventHandler"""
        self.eventHandler("move")

    def eventHandlerShoot(self):
        """Allows the workThread to control the eventHandler"""
        self.eventHandler("shoot")

    def setConsoleMessage(self, label, message):
        """Sets the message in the labels"""
        if label == "info":
            self.InfoLabel.setText(_translate("Form", message, None))
        if label == "gold":
            self.GoldLabel.setText(_translate("Form", message, None))
        if label == "pit":
            self.PitLabel.setText(_translate("Form", message, None))
        if label == "empty":
            self.EmptyLabel.setText(_translate("Form", message, None))
        if label == "bat":
            self.BatLabel.setText(_translate("Form", message, None))

    def resetConsoleMessage(self, label):
        """Resets the message in the labels"""
        message = ""
        if label == "info":
            self.InfoLabel.setText(_translate("Form", message, None))
        if label == "gold":
            self.GoldLabel.setText(_translate("Form", message, None))
        if label == "pit":
            self.PitLabel.setText(_translate("Form", message, None))
        if label == "empty":
            self.EmptyLabel.setText(_translate("Form", message, None))
        if label == "bat":
            self.BatLabel.setText(_translate("Form", message, None))

    def movehero(self, direction):
        """Move the Hunter/Hero on the map"""
        if self.moveturn == True:  # If the moveturn is True
            self.position = self.hunter.getposition()  # Get the position of the hunter
            if direction == "up":  # If the direction is up
                if self.position[1] == 1:  # if the yCor is 1
                    self.workThread.direction = "up"  # Move the hero in the workThread
                    self.hero.setPixmap(QtGui.QPixmap('hero_down.png'))  # Set the right Pixmap
                    self.hero.moveBy(0, 3 * -195)  # Move the hunter to yCor 4
                else:  # For any other yCor
                    self.workThread.direction = "up"
                    self.hero.setPixmap(QtGui.QPixmap('hero_down.png'))
                    self.hero.moveBy(0, 195)  # Move the hunter one up (192 pixels)
                self.hunter.moveup()  # Move the hunter in memory
            if direction == "down":
                if self.position[1] == 4:
                    self.workThread.direction = "down"
                    self.hero.setPixmap(QtGui.QPixmap('hero_up.png'))
                    self.hero.moveBy(0, 3 * 195)
                else:
                    self.workThread.direction = "down"
                    self.hero.setPixmap(QtGui.QPixmap('hero_up.png'))
                    self.hero.moveBy(0, -195)
                self.hunter.movedown()
            if direction == "left":
                if self.position[0] == 1:
                    self.workThread.direction = "left"
                    self.hero.setPixmap(QtGui.QPixmap('hero_left.png'))
                    self.hero.moveBy(4 * 240, 0)
                else:
                    self.workThread.direction = "left"
                    self.hero.setPixmap(QtGui.QPixmap('hero_left.png'))
                    self.hero.moveBy(-240, 0)
                self.hunter.moveleft()
            if direction == "right":
                if self.position[0] == 5:
                    self.workThread.direction = "right"
                    self.hero.setPixmap(QtGui.QPixmap('hero_right.png'))
                    self.hero.moveBy(4 * -240, 0)
                else:
                    self.workThread.direction = "right"
                    self.hero.setPixmap(QtGui.QPixmap('hero_right.png'))
                    self.hero.moveBy(240, 0)
                self.hunter.moveright()

    def movearrow(self, direction):
        """Allows the arrow to move on the map"""
        if self.shootturn == True:  # If shootturn is True
            self.arrowposition = self.hunter.getarrowposition()  # Get the arrow position
            if direction == "up":
                if self.arrowposition[1] == 1:
                    self.workThread.direction = "up"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowdown.png'))
                    self.arrow.moveBy(0, 3 * -195)
                else:
                    self.workThread.direction = "up"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowdown.png'))
                    self.arrow.moveBy(0, 195)
                self.hunter.shootup()
            if direction == "down":
                if self.arrowposition[1] == 4:
                    self.workThread.direction = "down"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowup.png'))
                    self.arrow.moveBy(0, 3 * 195)
                else:
                    self.workThread.direction = "down"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowup.png'))
                    self.arrow.moveBy(0, -195)
                self.hunter.shootdown()
            if direction == "left":
                if self.arrowposition[0] == 1:
                    self.workThread.direction = "left"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowleft.png'))
                    self.arrow.moveBy(4 * 240, 0)
                else:
                    self.workThread.direction = "left"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowleft.png'))
                    self.arrow.moveBy(-240, 0)
                self.hunter.shootleft()
            if direction == "right":
                if self.arrowposition[0] == 5:
                    self.workThread.direction = "right"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowright.png'))
                    self.arrow.moveBy(4 * -240, 0)
                else:
                    self.workThread.direction = "right"
                    self.arrow.setPixmap(QtGui.QPixmap('arrowright.png'))
                    self.arrow.moveBy(240, 0)
                self.hunter.shootright()

    def setarrow(self):
        """Set the image of the arrow"""
        self.arrow = QtGui.QGraphicsPixmapItem()
        arrowpng = "arrow" + self.lastdirection + ".png"
        self.arrow.setPixmap(QtGui.QPixmap(arrowpng))

    def setLastDirection(self):
        """Sets the right direction of the arrow"""
        try:
            self.lastdirection = self.workThread.lastdirection  # If a last direction is set, set it to it
        except:
            self.lastdirection = "up"  # If no last direction is set, use up. Since hunter spawns facing up.

    def resetarrow(self):
        """Resets the arrow"""
        xCor, yCor = self.hunter.getposition()
        xCord, yCord = self.coordConverter((xCor, yCor))
        self.arrow.setPos(xCord, yCord)
        self.scene.addItem(self.arrow)

    def hidearrow(self):
        """Hides the arrow"""
        self.scene.removeItem(self.arrow)

    def sethero(self, hunterx, huntery):
        """Sets the hero image"""
        self.hero = QtGui.QGraphicsPixmapItem()
        self.hero.setPixmap(QtGui.QPixmap("hero_up.png"))
        self.hero.setPos(hunterx, huntery)
        self.scene.addItem(self.hero)

    def coordConverter(self, coord):
        """Convert the actual coords, to the coords on the map in pixels, kept as long if statement incase
        of small adjustments."""
        if coord == (1, 1):
            return -497, 266
        if coord == (1, 2):
            return -497, 71
        if coord == (1, 3):
            return -497, -124
        if coord == (1, 4):
            return -497, -319
        if coord == (2, 1):
            return -257, 266
        if coord == (2, 2):
            return -257, 71
        if coord == (2, 3):
            return -257, -124
        if coord == (2, 4):
            return -257, -319
        if coord == (3, 1):
            return -17, 266
        if coord == (3, 2):
            return -17, 72
        if coord == (3, 3):
            return -17, -124
        if coord == (3, 4):
            return -17, -319
        if coord == (4, 1):
            return 223, 266
        if coord == (4, 2):
            return 223, 72
        if coord == (4, 3):
            return 223, -124
        if coord == (4, 4):
            return 223, -319
        if coord == (5, 1):
            return 463, 266
        if coord == (5, 2):
            return 463, 72
        if coord == (5, 3):
            return 463, -124
        if coord == (5, 4):
            return 463, -319

    def setMoveTurn(self):
        """Allows workThread to set moveturn"""
        self.moveturn = True

    def resetMoveTurn(self):
        """Allows workThread to reset moveturn"""
        self.moveturn = False

    def setShootTurn(self):
        """Allows workThread to set shootturn"""
        self.emit(QtCore.SIGNAL("setarrow"))
        self.shootturn = True

    def resetShootTurn(self):
        """Allows workThread to reset shootturn"""
        self.emit(QtCore.SIGNAL("removearrow"))
        self.shootturn = False

    def respawn(self):
        """Respawn the hero, used for bat"""
        ui.hunter.respawn()
        xCor, yCor = self.coordConverter(self.hunter.getposition())
        self.hero.setPos(xCor, yCor)

    def died(self, won):
        """Controls what happens if hunter dies."""
        if self.workThread.deadreason == "pit":  # Check for dead reason
            ui.setConsoleMessage("info", "You stepped on a pit an died!")
        if self.workThread.deadreason == "wumpus":
            ui.setConsoleMessage("info", "You have been eaten by Wumpy!")
        ui.setConsoleMessage("gold", "You found {} gold".format(self.hunter.getgold()))  # Show the statistics
        ui.setConsoleMessage("pit", "You had {} arrows left".format(self.hunter.getarrows()))
        ui.setConsoleMessage("bat", "Score: {}".format(highscore.highscore(self.hunter.getname(),
                                                                           self.hunter.getgold(),
                                                                           self.hunter.getarrows(),
                                                                           len(self.hunter.getpath()),
                                                                           False)))  # Write to the highscore file
        ui.setConsoleMessage("empty", "Press Escape to restart the game.")  # Set replay message

    def win(self):
        ui.setConsoleMessage("info", "Well done! You defeated Wumpus!")
        ui.setConsoleMessage("gold", "You found {} gold".format(self.hunter.getgold()))
        ui.setConsoleMessage("pit", "You had {} arrows left".format(self.hunter.getarrows()))
        ui.setConsoleMessage("bat", "Score: {}".format(highscore.highscore(self.hunter.getname(),
                                                                   self.hunter.getgold(),
                                                                   self.hunter.getarrows(),
                                                                   len(self.hunter.getpath()),
                                                                   True)))
        highscore.highscore(self.hunter.getname(), self.hunter.getgold(), self.hunter.getarrows(),
                            len(self.hunter.getpath()), True)
        ui.setConsoleMessage("empty", "Press Escape to restart the game.")

    def closeEvent(self, QCloseEvent):
        """Properly quits the workthread if the screen gets closed"""
        self.workThread.quit()
        exit(0)



class WorkerThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        """Controls the backend of the game"""
        sleep(1)  # Wait for the ui to properly load

        # Set a bunch of variables

        ui.resetMoveTurn()
        self.alive = True
        self.action = None
        self.direction = None
        self.lastdirection = "up"
        self.emit(QtCore.SIGNAL("gold"))
        self.emit(QtCore.SIGNAL("arrow"))

        while self.alive:  # While the hero is alive

            # Clear the messages in the labels

            ui.resetConsoleMessage("gold")
            ui.resetConsoleMessage("pit")
            ui.resetConsoleMessage("empty")
            ui.resetConsoleMessage("bat")

            items = []  # Make a empty list with items

            # Check for any nearby items and Wumpus
            xCor, yCor = ui.hunter.getposition()

            positionCheck = [(xCor, yCor + 1), (5, yCor), (xCor + 1, yCor), (xCor, yCor - 1)]
            if xCor == 1:
                positionCheck.append((5, yCor))
            if xCor == 5:
                positionCheck.append((1, yCor))
            if yCor == 1:
                positionCheck.append((xCor, 4))
            if yCor == 4:
                positionCheck.append((xCor, 1))

            positionCheckWumpus = (positionCheck + [(xCor + 1, yCor + 1), (xCor - 1, yCor + 1), (xCor + 1, yCor - 1),
                                                   (xCor - 1, yCor - 1), (xCor - 2, yCor), (xCor + 2, yCor),
                                                   (xCor, yCor + 2), (xCor, yCor - 2)])
            if xCor == 1:
                positionCheckWumpus.append((4, yCor))
            if xCor == 5:
                positionCheckWumpus.append((1, yCor))
            if yCor == 1:
                positionCheckWumpus.append((xCor, 4))
            if yCor == 4:
                positionCheckWumpus.append((xCor, 1))
            if (xCor, yCor) == (1, 1):
                positionCheckWumpus.append((5, 4))
            if (xCor, yCor) == (5, 4):
                positionCheckWumpus.append((1, 1))
            if (xCor, yCor) == (1, 4):
                positionCheckWumpus.append((5, 1))
            if (xCor, yCor) == (5, 1):
                positionCheckWumpus.append((1, 4))

            for coordinates in ui.roomsmap.showrooms():
                for rooms in positionCheck:
                    if str(coordinates[0]) == str(rooms):
                        items.append(coordinates[1])
            if "gold" in items:
                ui.setConsoleMessage("gold", "There is gold near you!")
            if "bat" in items:
                ui.setConsoleMessage("bat", "Bats nearby")
            if "pit" in items:
                ui.setConsoleMessage("pit", "I feel a draft")

            for coordinates in ui.roomsmap.showrooms():
                for rooms in positionCheckWumpus:
                    if str(coordinates[0]) == str(rooms):
                        if str(rooms) == str(ui.wumpus.getposition()):
                            ui.setConsoleMessage("empty", "I smell a Wumpus!")

            if self.alive:  # If the hunter is still alive
                if ui.hunter.getposition() == ui.wumpus.getposition():  # If position of hunter is equal to the
                # position of Wumpus
                    self.alive = False  # Hunter is dead
                    self.deadreason = "wumpus"  # Set the reason of dead to Wumpus
                    ui.died(False)  # Run died
                if self.alive:
                    ui.wumpus.hunt(ui.hunter.getposition())  # Move wumpus in direction of hunter
                    if ui.hunter.getposition() == ui.wumpus.getposition():
                        self.alive = False
                        self.deadreason = "wumpus"
                        ui.died(False)
            if self.alive:
                ui.setConsoleMessage("info", "Do you want to move or shoot?")

                self.emit(QtCore.SIGNAL("action"))
                self.action = None
                while self.action == None:  # While no action is set, sleep for 0.5 seconds
                    sleep(0.5)

                if self.action.lower() == "move":  # If action is move
                    ui.setMoveTurn()  # Set the move turn
                    ui.setConsoleMessage("info", "Please select your move Hunter. up, down, left or right?")
                    self.direction = None  # Reset the direction
                    while self.direction == None:  # While no direction is set, sleep for 0.1 seconds
                        sleep(0.1)
                    ui.setLastDirection()  # Set last direction
                    ui.resetMoveTurn()  # Reset the move turn
                    self.lastdirection = self.direction

                    ui.setConsoleMessage("info", "You moved {}!".format(self.action))

                    # Check if hunter stepped on items

                    for room in ui.roomsmap.showrooms():
                        if ui.hunter.getposition() == room[0]:
                            if room[1] == "pit":
                                ui.setConsoleMessage("pit", "You stepped on a {}".format(room[1]))
                                self.alive = False
                                self.deadreason = "pit"  # Set the dead reason to pit
                            elif room[1] == "gold":
                                ui.setConsoleMessage("gold", "You stepped on a {}".format(room[1]))
                                self.emit(QtCore.SIGNAL("gold"))  # Give a gold signal to main thread
                            elif room[1] == "bat":
                                ui.setConsoleMessage("info", "You stepped on a {}. The bat took you, "
                                                             "and dropped you in a random room!".format(room[1]))
                                ui.hunter.setwumpuspos(ui.wumpus.getposition())  # Set the wumpis position
                                ui.respawn()  # Respawn the hunter
                                sleep(2)  # Shows the bat messsage for 2 seconds

                # If player pressed shoot

                elif self.action.lower() == "shoot":
                    ui.setShootTurn()  # Set shootturn
                    ui.setConsoleMessage("info", "Please select what way you want to shoot. up, down, left or right?")
                    self.distance = 0  # Set distance to 0
                    while len(ui.hunter.arPath) != 6:  # While player did not set a path of lengt 6 (allows trackback)
                        self.distance = ui.getDistance()  # Set the distance
                        sleep(0.1)  # Slows down the while loop
                    ui.hunter.resetarpath()  # Reset the path of the arrow
                    ui.resetShootTurn()  # Reset the shootturn
                    ui.hunter.shoot(ui.wumpus.position)  # Shoot the arrow
                    if ui.hunter.getVictory():  # If wumpus got hit
                        self.alive = False  # Let the hunter die
                    if ui.hunter.getarrows == 0:
                        ui.died(False)  # If no arrows are left, you die
                    self.emit(QtCore.SIGNAL("arrow"))  # Run the arrow funciton in mainthread

            self.action = None  # Reste the action

        if ui.hunter.victory:  # If player won, run win
            ui.win()
        else:  # Else run died
            ui.died(False)


    def actionMove(self):
        """Set action to move"""
        self.action = "move"

    def actionShoot(self):
        """Set action to shoot"""
        self.action = "shoot"

def run():
    sleep(1) # Wait while games get loaded

if __name__ == "__main__":

    class DevNull:
        """Write all errors to blackhole, since shown errors are PyQt bugs"""
        def write(self, msg):
            pass

    sys.stderr = DevNull()

    start_UI.main()  # Start the start screen
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')  # Set the appstyle
    ui = Ui_Form()  # Run the game
    ui.show()
    sys.exit(app.exec_())
