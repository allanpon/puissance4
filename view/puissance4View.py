"""
Class main application view.
"""

from PyQt5.QtWidgets import QMainWindow

from view.puissance4GridView import Puissance4GridView


class Puissance4View(QMainWindow):

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.__model = None
        self.__controller = None
        self.setWindowTitle("Puissance 4")
        self.setFixedSize(700, 600)

        self.__gridView = Puissance4GridView()
        self.setStyleSheet("background-color:blue;")
        self.setCentralWidget(self.__gridView)
        self.show()
        self.statusBar().setStyleSheet("background-color:white;font-size: 36px;")
        self.statusBar().showMessage("Puissance 4")

    def setModel(self, model):
        """
        Setter
        """
        self.__model = model
        self.__gridView.setModel(model)

    def setController(self, controller):
        """
        Setter
        """
        self.__controller = controller

    def updateStatus(self, s):
        """
        Update the status bar
        """
        self.statusBar().showMessage(s)

    def updateView(self):
        """
        Update.
        """
        self.__gridView.update()

    def mousePressEvent(self, event):
        """
        Redefine the mouse event
        """
        self.__controller.playPosition(
            self.__gridView.findColumn(event.pos().x()))
