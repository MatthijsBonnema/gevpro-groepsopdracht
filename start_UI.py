#!/usr/bin/python3
# File: start_UI.py
# Author: Tomer Gabay
# Date: 03/25/15
# Info: QtDesigner was used 

from PyQt4 import QtCore, QtGui
import sys
import hunt_the_wumpus
import highscore

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
        self.allowclose = True

    def setupUi(self, Form):
        self.closeWidget = False
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(409, 252)
        Form.setStyleSheet(_fromUtf8("background-color: black;"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.up_widget = QtGui.QWidget(Form)
        self.up_widget.setStyleSheet(_fromUtf8("text-align: center;"))
        self.up_widget.setObjectName(_fromUtf8("up_widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.up_widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.title_lbl = QtGui.QLabel(self.up_widget)
        self.title_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_lbl.setStyleSheet(_fromUtf8("color: red;\n"
                                               "font: 63 italic 10pt \"URW Chancery L\";"))
        self.title_lbl.setObjectName(_fromUtf8("title_lbl"))
        self.verticalLayout_2.addWidget(self.title_lbl)
        self.by_lbl = QtGui.QLabel(self.up_widget)
        self.by_lbl.setStyleSheet(_fromUtf8("color: yellow;"))
        self.by_lbl.setObjectName(_fromUtf8("by_lbl"))
        self.verticalLayout_2.addWidget(self.by_lbl)
        self.verticalLayout.addWidget(self.up_widget)
  
        self.down_widget = QtGui.QWidget(Form)
        self.down_widget.setObjectName(_fromUtf8("down_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.down_widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.play_btn = QtGui.QPushButton(self.down_widget)
        self.play_btn.setMinimumSize(QtCore.QSize(130, 0))
        self.play_btn.setMaximumSize(QtCore.QSize(130, 16777215))
        self.play_btn.setStyleSheet(_fromUtf8("background-color: green;\n"
                                              "color: black;"))
        self.play_btn.setObjectName(_fromUtf8("play_btn"))
        self.horizontalLayout.addWidget(self.play_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.highscores_btn = QtGui.QPushButton(self.down_widget)
        self.highscores_btn.setMinimumSize(QtCore.QSize(130, 0))
        self.highscores_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.highscores_btn.setStyleSheet(_fromUtf8("background-color: orange;\n"
                                                    "color: black;"))
        self.highscores_btn.setObjectName(_fromUtf8("highscores_btn"))
        self.horizontalLayout.addWidget(self.highscores_btn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.down_widget)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
        #activate game or highscores:
        self.play_btn.clicked.connect(self.activategame)
        self.highscores_btn.clicked.connect(self.highscores)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Hunt the Wumpus", None))
        self.title_lbl.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;"
                                                  " font-weight:400; font-style:normal;\">Hunt The Wumpus</span></p>"
                                                  "<p><span style=\" font-size:36pt; font-weight:400;"
                                                  " font-style:normal;\"><br/></span></p></body></html>",
                                          None))
        self.by_lbl.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">"
                                               "By: Matthijs Bonnema, Tomer Gabay, Jeroen Wilkens</span></p>"
                                               "</body></html>", None))
        self.play_btn.setText(_translate("Form", "Play!", None))
        self.highscores_btn.setText(_translate("Form", "Highscores", None))

    def highscores(self):
        highscore.main()

    def activategame(self):
        self.allowclose = False
        self.close()
        return 0

    def closeEvent(self, QCloseEvent):
        if self.allowclose:
            exit(0)


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')
    interface = Ui_Form()
    interface.show()
    app.exec_()


if __name__ == "__main__":
    main()
