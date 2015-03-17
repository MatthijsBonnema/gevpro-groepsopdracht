# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hunt_the_wumpus.ui'
#
# Created: Mon Mar 16 14:32:52 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from functools import partial
import hero

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
                self.movehero("up")
            if event == "down":
                self.movehero("down")
            if event == "left":
                self.movehero("left")
            if event == "right":
                self.movehero("right")
            if event == "shoot":
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
        self.sethero()
        # self.setArrowAmount()

        self.right.clicked.connect(self.eventHandlerRight)
        self.left.clicked.connect(self.eventHandlerLeft)
        self.up.clicked.connect(self.eventHandlerUp)
        self.down.clicked.connect(self.eventHandlerDown)
        self.move.clicked.connect(self.eventHandlerMove)
        self.shoot.clicked.connect(self.eventHandlerShoot)

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



    def sethero(self):
        self.hero = QtGui.QGraphicsPixmapItem()
        self.hero.setPixmap(QtGui.QPixmap("hero_up.png"))
        self.hero.setPos(-497, -319)
        self.scene.addItem(self.hero)


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