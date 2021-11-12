class Field:
    listCoordinate = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    def printField(self):
        print('  1 2 3')
        for row in range(3):
            print(row + 1, end=' ')
            for col in range(3):
                print(self.listCoordinate[row][col], end='')
                if col != 2: print('|', end='')
                else: print()