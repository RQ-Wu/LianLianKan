from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tool.readQssTool import readQssTool
from gameMap import Map


class Ui_game:
    def __init__(self):
        self.buttons = [[],[],[],[],[],[],[],[]]
        self.map = Map()

    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        for i in range(8):
            for j in range(16):
                self.buttons[i].append(QtWidgets.QPushButton(Dialog))
                self.buttons[i][j].setGeometry(QtCore.QRect(100+50*j, 125+50*i, 45, 45))
                self.buttons[i][j].setObjectName("btn"+str(i)+"_"+str(j))

    def getImage(self):
        qss=''
        for i in range(8):
            for j in range(16):
                num = self.map.getData()[i][j]
                qss+= 'QPushButton#btn'+str(i)+'_'+str(j)+'{' \
                    'border-image:url(../image/'+str(num)+'.png);}'
        return qss


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_game()
    ui.setupUi(mainWindow)
    ui.getImage()
    qss='''
        QMainWindow{
            border-image:url(../image/game-bg.jpg)
        }
    '''
    mainWindow.setStyleSheet(ui.getImage()+qss)
    mainWindow.show()
    print(ui.getImage())
    sys.exit(app.exec_())

