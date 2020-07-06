from PyQt5 import QtCore, QtWidgets
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import *
import time

from qtpy import QtGui


class TestForm(QMainWindow):
    def __init__(self):
        super(TestForm,self).__init__()
        self.resize(300,600)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.red, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(10,120,10,400)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TestForm()
    qss='''
    QMainWindow{
    border-image:url(image/game-bg.jpg)
}
QPushButton:hover{
    border:2px black solid;
}
QPushButton#restart-btn{
    border-image:url(../image/restartButton.png)
}
    '''
    form.setStyleSheet(qss)
    form.show()
    sys.exit(app.exec_())