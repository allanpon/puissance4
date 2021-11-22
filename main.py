"""
Main program.
"""
import sys
from PyQt5.QtWidgets import QApplication

from model.puissance4Model import Puissance4Model
from view.puissance4View import Puissance4View
from controller.puissance4Controller import Puissance4Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = Puissance4Model(6, 7)
    view = Puissance4View()
    controller = Puissance4Controller()

    view.setModel(model)
    view.setController(controller)

    model.setView(view)

    controller.setView(view)
    controller.setModel(model)

    sys.exit(app.exec_())
