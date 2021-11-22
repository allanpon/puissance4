"""
Controller.
"""


class Puissance4Controller:
    """
    Class Puissance 4.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.__model = None
        self.__view = None

        self.__counter = 0
        self.__terminated = False

    def setView(self, view):
        """
        Set the view.
        """
        self.__view = view

    def setModel(self, model):
        """
        Set the model.
        """
        self.__model = model

    def searchWinner(self):
        """
        Search for a winner if exist.
        Return 0 if no winner, 1 if player 1 wins and 2 otherwise.
        """
        ret = 0

        matrix = self.__model.getMatrix()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    continue

                if j + 3 >= len(matrix[i]):
                    continue

                if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i][j + 2] and matrix[i][j] == matrix[i][j + 3]:
                    return matrix[i][j]

                if i >= 3 and matrix[i][j] == matrix[i-1][j + 1] and matrix[i][j] == matrix[i-2][j + 2] and matrix[i][j] == matrix[i-3][j + 3]:
                    return matrix[i][j]

                if i < len(matrix) - 4 and matrix[i][j] == matrix[i+1][j + 1] and matrix[i][j] == matrix[i+2][j + 2] and matrix[i][j] == matrix[i + 3][j + 3]:
                    return matrix[i][j]

                if i >= 3 and matrix[i][j] == matrix[i-1][j] and matrix[i][j] == matrix[i-2][j] and matrix[i][j] == matrix[i-3][j]:
                    return matrix[i][j]

        return ret

    def playPosition(self, column):
        """
        Put a coin at the given column.
        """
        if self.__terminated:
            return
        matrix = self.__model.getMatrix()

        if column < 0 or column >= len(matrix[0]):
            return

        pos = 0
        while pos < len(matrix) and matrix[pos][column] != 0:
            pos += 1

        if pos >= len(matrix):
            return

        matrix[pos][column] = 1 + self.__counter % 2
        self.__model.setMatrix(matrix)

        winner = self.searchWinner()
        if winner != 0:
            self.__terminated = True
            self.__view.updateStatus(str(1 + self.__counter % 2) + " a gagné")
        else:
            self.__counter += 1
            self.__view.updateStatus(
                str(1 + self.__counter % 2) + " doit joué")
