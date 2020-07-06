from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QMovie

from LLKGame.game import *


class Ui_challenge(Ui_game):
    def __init__(self, Dialog):
        super().__init__(Dialog)
        self.movie = QMovie('../image/loading.gif')
        self.timeLable = QLabel(self.dialog)
        self.textScore = QtWidgets.QPushButton(self.dialog)
        self.setupChallengeUi(self.score)

    def setupChallengeUi(self, score):
        """
        Set up some ui belong to the challenge model
        :return:
        """
        # the text to show the score
        self.textScore.setText("分数：" + str(score))
        self.textScore.move(800, 35)
        self.textScore.resize(150, 50)
        self.textScore.setStyleSheet("color:#ff6600;font-size:30px;font-weight:bold;")
        self.textScore.setEnabled(False)
        # the timeBar to show the time remained
        self.timeLable.setMovie(self.movie)
        self.timeLable.resize(1000, 50)
        self.timeLable.move(150, 540)
        self.movie.start()

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
            self.score += 5
            self.refreshGame()
            self.dialog.setPoints(points)
            self.dialog.update()
            return True
        else:
            self.buttons[buttonPosition[1]][buttonPosition[0]].setChecked(False)
            self.buttons[buttonPosition[3]][buttonPosition[2]].setChecked(False)
            self.score -= 10
            print(self.score)
            self.refreshGame()
            return False

    def refreshGame(self):
        """
        Function to refresh the game,render the cells again
        :return: none
        """
        self.dialog.setStyleSheet(self.getQss())
        self.textScore.setText("得分：" + str(self.score))
        if np.sum(self.map.getData()) == 0:
            self.gameOver()
        else:
            QApplication.processEvents()

    def restart(self):
        """
        Function to restart the game
        :return: none
        """
        self.map = GameMap()
        self.refreshGame()

        # restart the timeBar
        self.movie = QMovie('../image/loading.gif')
        self.timeLable.setMovie(self.movie)
        self.movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    testWindow = GameForm()
    ui = Ui_challenge(testWindow)
    testWindow.show()
    sys.exit(app.exec_())
