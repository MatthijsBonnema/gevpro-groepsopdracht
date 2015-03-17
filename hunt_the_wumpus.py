# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hunt_the_wumpus.ui'
#
# Created: Mon Mar 16 14:32:52 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from room_generator import RoomGenerator
from hero import Hero
from wumpus import Wumpus
from time import sleep

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
        self.setupUi(self)

    def keyPressEvent(self, event):
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
        else:
            event.ignore()

    def eventHandler(self, event):
            if event == "up":
                self.hunter.moveright()
                self.movehero("up")
            if event == "down":
                self.hunter.movedown()
                self.movehero("down")
            if event == "left":
                self.hunter.moveleft()
                self.movehero("left")
            if event == "right":
                self.hunter.moveright()
                self.movehero("right")
            if event == "shoot":
                self.hunter.shoot()
                print("Shoot")
            if event == "move":

                print("Move")

    def setupUi(self, Form):
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
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.move = QtGui.QPushButton(Form)
        self.move.setFont(font)
        self.move.setObjectName(_fromUtf8("move"))
        self.gridLayout_4.addWidget(self.move, 1, 4, 1, 1)
        self.right = QtGui.QPushButton(Form)
        self.right.setFont(font)
        self.right.setObjectName(_fromUtf8("right"))
        self.gridLayout_4.addWidget(self.right, 2, 7, 1, 1)
        self.arrows_amount = QtGui.QLCDNumber(Form)
        self.arrows_amount.setObjectName(_fromUtf8("arrows_amount"))
        self.gridLayout_4.addWidget(self.arrows_amount, 0, 7, 1, 1)
        self.up = QtGui.QPushButton(Form)
        self.up.setFont(font)
        self.up.setObjectName(_fromUtf8("up"))
        self.gridLayout_4.addWidget(self.up, 1, 6, 1, 1)
        self.arrows = QtGui.QLabel(Form)
        self.arrows.setFont(font)
        self.arrows.setObjectName(_fromUtf8("arrows"))
        self.gridLayout_4.addWidget(self.arrows, 0, 6, 1, 1)
        self.shoot = QtGui.QPushButton(Form)
        self.shoot.setFont(font)
        self.shoot.setObjectName(_fromUtf8("shoot"))
        self.gridLayout_4.addWidget(self.shoot, 2, 4, 1, 1)
        self.down = QtGui.QPushButton(Form)
        self.down.setFont(font)
        self.down.setObjectName(_fromUtf8("down"))
        self.gridLayout_4.addWidget(self.down, 2, 6, 1, 1)
        self.Gold = QtGui.QLabel(Form)
        self.Gold.setFont(font)
        self.Gold.setObjectName(_fromUtf8("Gold"))
        self.gridLayout_4.addWidget(self.Gold, 0, 4, 1, 1)
        self.left = QtGui.QPushButton(Form)
        self.left.setFont(font)
        self.left.setObjectName(_fromUtf8("left"))
        self.gridLayout_4.addWidget(self.left, 2, 5, 1, 1)
        self.gold_amount = QtGui.QLCDNumber(Form)
        self.gold_amount.setObjectName(_fromUtf8("gold_amount"))
        self.gridLayout_4.addWidget(self.gold_amount, 0, 5, 1, 1)
        self.console = QtGui.QLabel(Form)
        self.console.setText(_fromUtf8(""))
        self.console.setObjectName(_fromUtf8("console"))
        self.console.setFont(font)
        self.gridLayout_4.addWidget(self.console, 0, 0, 3, 4)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Hunt the Wumpus", None))

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

        self.rooms = QtGui.QGraphicsPixmapItem()
        self.rooms.setPixmap(QtGui.QPixmap("rooms.png"))
        self.rooms.setPos(-587, -387)
        self.scene.addItem(self.rooms)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)

        self.graphicsView.setScene(self.scene)

        self.setConsoleMessage("Welcome to Hunt the Wumpus v1.0")

        self.hunter = Hero("Hero")
        hunterx, huntery = self.coordConverter(self.hunter.getposition())
        self.sethero(hunterx, huntery)
        self.wumpus = Wumpus(self.hunter.getposition())
        self.rooms = RoomGenerator(self.hunter.getposition(), self.wumpus.getposition())

        self.right.clicked.connect(self.eventHandlerRight)
        self.left.clicked.connect(self.eventHandlerLeft)
        self.up.clicked.connect(self.eventHandlerUp)
        self.down.clicked.connect(self.eventHandlerDown)
        self.move.clicked.connect(self.eventHandlerMove)
        self.shoot.clicked.connect(self.eventHandlerShoot)

        self.workThread = WorkerThread()
        self.connect(self.workThread, QtCore.SIGNAL("update(QString)"), self.test123, QtCore.Qt.DirectConnection)
        self.workThread.start()

    def test123(self):
        self.setConsoleMessage("test")

    def setArrowAmount(self, arrows):
        self.arrows_amount.display(arrows)

    def eventHandlerRight(self):
        self.eventHandler("right")

    def eventHandlerLeft(self):
        self.eventHandler("left")

    def eventHandlerUp(self):
        self.eventHandler("up")

    def eventHandlerDown(self):
        self.eventHandler("down")

    def eventHandlerMove(self):
        self.eventHandler("move")

    def eventHandlerShoot(self):
        self.eventHandler("shoot")

    def setConsoleMessage(self, message):
        self.console.setText(_translate("Form", message, None))

    def movehero(self, direction):
        if direction == "up":
            self.hero.setPixmap(QtGui.QPixmap('hero_down.png'))
            self.hero.moveBy(0, 195)
        if direction == "down":
            self.hero.setPixmap(QtGui.QPixmap('hero_up.png'))
            self.hero.moveBy(0, -195)
        if direction == "left":
            self.hero.setPixmap(QtGui.QPixmap('hero_left.png'))
            self.hero.moveBy(-240, 0)
        if direction == "right":
            self.hero.setPixmap(QtGui.QPixmap('hero_right.png'))
            self.hero.moveBy(240, 0)

    def sethero(self, hunterx, huntery):
        self.hero = QtGui.QGraphicsPixmapItem()
        self.hero.setPixmap(QtGui.QPixmap("hero_up.png"))
        self.hero.setPos(hunterx, huntery)
        self.scene.addItem(self.hero)

    def coordConverter(self, coord):
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



class WorkerThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        alive = True

        while alive:

            items = []

            # check if something is near
            xCor, yCor = ui.hunter.getposition()

            if ui.hunter.getposition()[0] == 1:
                positionCheck = [(xCor, yCor + 1), (xCor, 5), (xCor + 1, yCor), (xCor - 1, yCor)]
                positionCheckWumpus = [(xCor, yCor + 1), (xCor, 5), (xCor + 1, yCor), (xCor - 1, yCor)]
            elif ui.hunter.getposition()[0] == 5:
                positionCheck = [(xCor, yCor + 1), (xCor, yCor - 1), (1, yCor), (xCor - 1, yCor)]
                positionCheckWumpus = [(xCor, yCor + 1), (xCor, yCor - 1), (1, yCor), (xCor - 1, yCor)]
            elif ui.hunter.getposition()[1] == 1:
                positionCheck = [(xCor, yCor + 1), (xCor, 4), (xCor + 1, yCor), (xCor - 1, yCor)]
                positionCheckWumpus = [(xCor, yCor + 1), (xCor, 4), (xCor + 1, yCor), (xCor - 1, yCor)]
            elif ui.hunter.getposition()[1] == 4:
                positionCheck = [(xCor, 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]
                positionCheckWumpus = [(xCor, 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]
            else:
                positionCheck = [(xCor, yCor + 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]
                positionCheckWumpus = [(xCor, yCor + 1), (xCor, yCor - 1), (xCor + 1, yCor), (xCor - 1, yCor)]

            for coordinates in ui.rooms.showrooms():
                if coordinates[0] in positionCheck:
                    items.append(coordinates[1])
            if "gold" in items:
                print("There is gold near you!")
            if "bat" in items:
                print("Bats nearby")
            if "pit" in items:
                print("I feel a draft")

            notTurn = True

            if alive:
                if ui.hunter.getposition() == ui.wumpus.getposition():
                    print("You have been eaten by Wumpy\n")
                    alive = False
                if alive:
                    ui.wumpus.hunt()

                    if ui.hunter.getposition() == ui.wumpus.getposition():
                        print("You have been eaten by Wumpy\n")
                        alive = False
                        ### Aanroep Highscore functie Hier ###
            if ui.wumpus.getposition() in positionCheckWumpus:
                print("I smell a Wumpus\n")


            while notTurn:
                ui.setConsoleMessage("Do you want to move or shoot?")

                if action.lower() == "move" or action.lower() == "shoot":
                    notTurn = False
                else:
                    print("Not a valid input, use move or shoot\n")

            if action.lower() == "move":
                moveto = input("\nPlease select your move Hunter. up, down, left or right?\n")
                move = ui.hunter.move(moveto)

                if not move:  # if move == False
                    print("Not a valid input!\n")
                else:
                    print("You moved {}!\n".format(moveto))

                    for room in ui.rooms.showrooms():
                        if ui.hunter.getposition() == room[0]:
                            if room[1] == "pit":
                                print("You stepped on a {}".format(room[1]))
                                print("You died!\n")
                                alive = False
                                ### Highscore functie hier aanroepen ###
                            elif room[1] == "gold":
                                print("You stepped on a {}".format(room[1]))
                                ui.hunter.foundgold()
                            elif room[1] == "bat":
                                print("You stepped on a {}\nThe bat took you, and dropped you in a random room!".format(room[1]))
                                ui.hunter.setwumpuspos(ui.wumpus.getposition())
                                ui.hunter.respawn()
            elif action.lower() == "shoot":
                print("pew pew pew\n")

            # if alive:
            #     if self.hunter.getposition() == wumpus.getposition():
            #         print("You have been eaten by Wumpy\n")
            #         alive = False
            #     if alive:
            #         wumpus.hunt()
            #
            #         if self.hunter.getposition() == wumpus.getposition():
            #             print("You have been eaten by Wumpy\n")
            #             alive = False

        print("You found {} gold".format(ui.hunter.getgold()))
        print("You had {} arrows left".format(ui.hunter.getarrows()))

def run():
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())