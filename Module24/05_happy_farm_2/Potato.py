class Potato:
    states = {0: 'Отсутствует',
              1: 'Росток',
              2: 'Зелёная',
              3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.printState()


    def printState(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))

    def is_ripe(self):
        return self.state == 3
