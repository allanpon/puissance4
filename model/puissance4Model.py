"""
Model.
"""


class Puissance4Model:
    """
    Class Puissance 4.
    """

    def __init__(self, w, h):
        """
        Constructor.
        """
        self.__view = None
        self.__matrix = [[0 for i in range(h)] for j in range(w)]

    def setView(self, view):
        """
        Set the view.
        """
        self.__view = view

    def getMatrix(self):
        """
        Get the matrix.
        """
        return self.__matrix

    def setMatrix(self, matrix):
        self.__matrix = matrix
        self.__view.updateView()
