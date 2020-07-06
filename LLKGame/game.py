from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import *
from qtpy import QtGui
from tool.readQssTool import readQssTool
from LLKGame.gameMap import GameMap
from LLKGame.connect import *
from Menu.menu import *
import time


class Ui_game:
    def __init__(self, Dialog):
        self.dialog = Dialog
        self.buttons = [[], [], [], [], [], [], [], []]
        self.map = GameMap()
        self.setupUi(self.dialog)
        self.dialog.setStyleSheet(self.getQss())
        self.score = 0

    def setupUi(self, Dialog):
        # set up buttons for the cells of the game
        self.buttons = [[], [], [], [], [], [], [], []]
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        for i in range(8):
            for j in range(16):
                self.buttons[i].append(QtWidgets.QPushButton(Dialog))
                self.buttons[i][j].setGeometry(QtCore.QRect(100 + 50 * j, 125 + 50 * i, 45, 45))
                self.buttons[i][j].setObjectName("btn" + str(i) + "_" + str(j))
                self.buttons[i][j].setCheckable(True)
                self.buttons[i][j].clicked.connect(lambda: self.isRemovable())
        # set up a button for restarting the game
        restartButton = QtWidgets.QPushButton(Dialog)
        restartButton.setObjectName('restart-btn')
        restartButton.setGeometry(QtCore.QRect(20, 70, 50, 50))
        restartButton.clicked.connect(lambda: self.restart())
        # set up a button for going home
        homeButton = QtWidgets.QPushButton(Dialog)
        homeButton.setObjectName('home-btn')
        homeButton.setGeometry(QtCore.QRect(20, 20, 50, 50))
        homeButton.clicked.connect(lambda: self.goHome())

    def getQss(self):
        """
        Function to render the GUI with tht stylesheet file
        :return:string(qss to render the cells)
        """
        qss = readQssTool.readQss('C:/Users//12/Desktop/LLK/LLKGame/game.qss')
        for i in range(8):
            for j in range(16):
                num = self.map.getData()[i][j]
                qss += 'QPushButton#btn' + str(i) + '_' + str(j) + '{' \
                                                                   'border-image:url(../image/' + str(num) + '.png);}'
        return qss

    def isRemovable(self):
        """
        Function to judge if two cells is removable and to do some matching operator:
        1. remove the image
        2. paint the line on the window
        3. refresh the game
        :return:boolean(if two cells is removable)
        """
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
        flag, points = connect(self.map.getData(), buttonPosition[0],
                               buttonPosition[1], buttonPosition[2], buttonPosition[3])
        if flag:
            self.buttons[buttonPosition[1]][buttonPosition[0]].setCheckable(False)
            self.buttons[buttonPosition[3]][buttonPosition[2]].setCheckable(False)
            self.buttons[buttonPosition[1]][buttonPosition[0]].setEnabled(False)
            self.buttons[buttonPosition[3]][buttonPosition[2]].setEnabled(False)
            self.refreshGame()
            self.dialog.setPoints(points)
            self.dialog.update()
            self.score += 5

            return True
        else:
            self.buttons[buttonPosition[1]][buttonPosition[0]].setChecked(False)
            self.buttons[buttonPosition[3]][buttonPosition[2]].setChecked(False)
            self.score -= 10
            self.refreshGame()
            return False

    def refreshGame(self):
        """
        Function to refresh the game,render the cells again
        :return: none
        """
        self.dialog.setStyleSheet(self.getQss())
        if np.sum(self.map.getData()) == 0:
            self.gameOver()
        else:
            QApplication.processEvents()

    def gameOver(self):
        """
        Function to show the dialog when game is over
        :return: none
        """
        msgBox = QMessageBox(QMessageBox.Information, 'GAMEOVER', '游戏完成！')
        restart = msgBox.addButton('重新开始', QMessageBox.AcceptRole)
        cancel = msgBox.addButton('取消', QMessageBox.DestructiveRole)
        reply = msgBox.exec()
        if reply == QMessageBox.AcceptRole:
            self.restart()

    def restart(self):
        """
        Function to restart the game
        :return: none
        """
        self.map = GameMap()
        self.refreshGame()

    def goHome(self):
        self.dialog.goHome()


class GameForm(QMainWindow):
    def __init__(self):
        super(GameForm, self).__init__()
        self.points = []
        self.flag = False

    def setPoints(self, points):
        self.points = points

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """
        Override to paint the line between two images
        :param a0:
        :return:
        """
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.red, 2, Qt.SolidLine)
        painter.setPen(pen)
        if self.flag:
            self.flag = False
            self.setPoints([])
            time.sleep(0.3)
            print(self.points)
            self.update()
        for i in range(len(self.points) - 1):
            painter.drawLine(self.points[i][0] * 50 + 125, self.points[i][1] * 50 + 150,
                             self.points[i + 1][0] * 50 + 125, self.points[i + 1][1] * 50 + 150)
            self.flag = True
        painter.end()

    def goHome(self):
        """
        Fuction to go back to home page
        :return:
        """
        self.hide()
        mainWindow = Ui_Menu()
        mainWindow.setWindowTitle('连连看')
        mainWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gameForm = GameForm()
    ui = Ui_game(gameForm)
    gameForm.show()
    sys.exit(app.exec_())
