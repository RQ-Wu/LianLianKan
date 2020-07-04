from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import *
from tool.readQssTool import readQssTool
from LLKdata.gameMap import GameMap
from LLKdata.connect import *
import time


def getState(button):
    if button.isChecked():
        print('button pressed')
    else:
        print('button released')


class Ui_game:
    def __init__(self,Dialog):
        self.dialog = Dialog
        self.buttons = [[],[],[],[],[],[],[],[]]
        self.map = GameMap()

    def setupUi(self,Dialog):
        self.buttons = [[], [], [], [], [], [], [], []]
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        for i in range(8):
            for j in range(16):
                self.buttons[i].append(QtWidgets.QPushButton(Dialog))
                self.buttons[i][j].setGeometry(QtCore.QRect(100+50*j, 125+50*i, 45, 45))
                self.buttons[i][j].setObjectName("btn"+str(i)+"_"+str(j))
                self.buttons[i][j].setCheckable(True)
                self.buttons[i][j].clicked.connect(lambda: getState(self.buttons[i][j]))
                self.buttons[i][j].clicked.connect(lambda: self.isRemovable())

    def getImage(self):
        qss=''
        for i in range(8):
            for j in range(16):
                num = self.map.getData()[i][j]
                qss+= 'QPushButton#btn'+str(i)+'_'+str(j)+'{' \
                    'border-image:url(../image/'+str(num)+'.png);}'
        return qss

    def isRemovable(self):
        buttonPosition = []
        cnt = 0
        for i in range(8):
            for j in range(16):
                if self.buttons[i][j].isChecked():
                    buttonPosition.append(j)
                    buttonPosition.append(i)
                    cnt = cnt + 1
                    if cnt == 2:
                        break
        if len(buttonPosition) < 4:
            return False
        elif connect(self.map.getData(),buttonPosition[0],buttonPosition[1],buttonPosition[2],buttonPosition[3]):
            self.buttons[buttonPosition[1]][buttonPosition[0]].setCheckable(False)
            self.buttons[buttonPosition[3]][buttonPosition[2]].setCheckable(False)
            self.buttons[buttonPosition[1]][buttonPosition[0]].setEnabled(False)
            self.buttons[buttonPosition[3]][buttonPosition[2]].setEnabled(False)
            self.refreshGame()
            return True
        else:
            self.buttons[buttonPosition[1]][buttonPosition[0]].setChecked(False)
            self.buttons[buttonPosition[3]][buttonPosition[2]].setChecked(False)
            return False

    def refreshGame(self):
        qss = '''
            QMainWindow{
                border-image:url(../image/game-bg.jpg)
            }
            QPushButton:hover{
                    border:5px black solid;
            }
            '''
        self.dialog.setStyleSheet(self.getImage() + qss)
        if not np.sum(self.map.getData()) == 0:
            self.gameOver()
        else:
            QApplication.processEvents()

    def gameOver(self):
        QMessageBox.about(self.dialog,'..','...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_game(mainWindow)
    ui.setupUi(mainWindow)
    qss = '''
                QMainWindow{
                    border-image:url(../image/game-bg.jpg);
                }
                QPushButton:hover{
                    border:2 black solid;
                }
                '''
    mainWindow.setStyleSheet(ui.getImage()+qss)
    mainWindow.show()
    sys.exit(app.exec_())




