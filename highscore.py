#!/usr/bin/python3

from PyQt4 import QtGui, QtCore
import sys

class Show_highscore(QtGui.QWidget):
    def __init__(self):

        super(Show_highscore, self).__init__()

        self.setWindowTitle("Highscores")
        self.setGeometry(0, 0, 200, 50)
        self.initUI()


    def initUI(self):

        self.namelabel = QtGui.QLabel("Name")
        self.scorelabel = QtGui.QLabel("Score")

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.namelabel, 0, 0)
        self.grid.addWidget(self.scorelabel, 0, 1)

        number_of_entries = self.entrycount()


        if number_of_entries >1:
            self.file = open("highscores.txt")
            for i in range(number_of_entries):
                line = self.file.readline()
                line = line.split()
                self.grid.addWidget(QtGui.QLabel(str(line[0])))
                self.grid.addWidget(QtGui.QLabel(str(line[1])))
            self.file.close()
        else:
            self.grid.addWidget(QtGui.QLabel("To compare your scores there need to be at least 2 entries."))

        self.setLayout(self.grid)


    def entrycount(self):

        self.file = open("highscores.txt")
        entrylist = []
        for entry in self.file:
            entrylist.append(entry)
        number_of_entries = len(entrylist)
        self.file.close()

        if number_of_entries >= 10:
            return 10
        else:
            return int(number_of_entries)


def main():

    app = QtGui.QApplication(sys.argv)
    object = Show_highscore()
    object.show()
    app.exec_()




def highscore(name, gold_amount, arrowsleft, number_of_steps, won):

    if won:
        score = 5000 - (number_of_steps * 100) + (arrowsleft * 250) + (gold_amount * 1000)
    else:
        score = 0 - (number_of_steps * 100) + (arrowsleft * 250) + (gold_amount * 1000)

    print("Score: ", score)

    # This prevents scores below 1000 becoming placed higher.
    if score < 1000:
        score = "0"+str(score)

    if score <=0:
        score = "0000"


    score_item = [str(score), str(name)]
    scorelist = [score_item]


    file_name = "highscores.txt"



    file = open(file_name, "r")
    for line in file:
        scorelist.append(line.split())
    file.close()

    scorelist.sort(reverse=True)

    

    file = open(file_name, "w")

    for item in scorelist:
        file.write((item[0])+" "+(item[1])+"\n")

    file.close()

if __name__ == "__main__":
    main()
