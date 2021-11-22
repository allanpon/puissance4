"""
View.
"""
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class Puissance4GridView(QWidget):
    """
    Class Puissance 4.
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.__model = None

    def setModel(self, model):
        """
        Set the model.
        """
        self.__model = model
        self.update()

    def findColumn(self, x):
        """
        Search the column regarding the x position.
        """
        wscreen = self.geometry().width()
        w = len(self.__model.getMatrix()[0])
        gw = wscreen / w

        ret = 0
        while (ret + 1) * gw < x:
            ret += 1

        return ret

    def paintEvent(self, event):
        """
        Paint Event method redefined.
        """
        if self.__model == None:
            return

        matrix = self.__model.getMatrix()
        w = len(matrix[0])
        h = len(matrix)

        rect = self.geometry()
        gw = rect.width() / w
        gh = rect.height() / h

        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 11, Qt.SolidLine))

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                px = j * gw
                py = (h - i - 1) * gh

                if matrix[i][j] == 0:
                    painter.setBrush(QBrush(Qt.black))
                elif matrix[i][j] == 1:
                    painter.setBrush(QBrush(Qt.yellow))
                else:
                    painter.setBrush(QBrush(Qt.red))

                painter.drawEllipse(px, py, gw, gh)
