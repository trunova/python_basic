import random

class Player:

    def __init__(self, value, field):
        self.value = value
        self.field = field

    def move(self, row, col):
        if self.field.listCoordinate[row - 1][col - 1] == '_':
            self.field.listCoordinate[row - 1][col - 1] = self.value
            if self.countValues() == 0: raise BaseException()
        else: raise IndexError()

    def botMove(self):
        while True:
            row = random.randint(1, 3)
            col = random.randint(1, 3)
            if self.field.listCoordinate[row - 1][col - 1] == '_':
                self.field.listCoordinate[row - 1][col - 1] = self.value
                if self.countValues() == 0: raise BaseException()
                break

    def countValues(self, value = '_'):
        count = 0
        for row in self.field.listCoordinate:
            for i in row:
                if i == value: count += 1
        return count

    def is_winner(self):
        if self.countValues(value=self.value) >= 3:
            if self.field.listCoordinate[0][0] == self.value and \
                    self.field.listCoordinate[0][1] == self.value and \
                    self.field.listCoordinate[0][2] == self.value:
                return True
            if self.field.listCoordinate[1][0] == self.value and \
                    self.field.listCoordinate[1][1] == self.value and \
                    self.field.listCoordinate[1][2] == self.value:
                return True
            if self.field.listCoordinate[2][0] == self.value and \
                    self.field.listCoordinate[2][1] == self.value and \
                    self.field.listCoordinate[2][2] == self.value:
                return True
            if self.field.listCoordinate[0][0] == self.value and \
                    self.field.listCoordinate[1][0] == self.value and \
                    self.field.listCoordinate[2][0] == self.value:
                return True
            if self.field.listCoordinate[0][1] == self.value and \
                    self.field.listCoordinate[1][1] == self.value and \
                    self.field.listCoordinate[2][1] == self.value:
                return True
            if self.field.listCoordinate[0][2] == self.value and \
                    self.field.listCoordinate[1][2] == self.value and \
                    self.field.listCoordinate[2][2] == self.value:
                return True
            if self.field.listCoordinate[0][0] == self.value and \
                    self.field.listCoordinate[1][1] == self.value and \
                    self.field.listCoordinate[2][2] == self.value:
                return True
            if self.field.listCoordinate[0][2] == self.value and \
                    self.field.listCoordinate[1][1] == self.value and \
                    self.field.listCoordinate[2][0] == self.value:
                return True
        return False