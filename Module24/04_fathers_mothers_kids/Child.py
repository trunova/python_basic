class Child:

    def __init__(self, name, age = 0, stateOfCalm = True, stateOfHunger = True, listParent = None):
        self.name = name
        self.age = age
        self.stateOfCalm = stateOfCalm
        self.stateOfHunger = stateOfHunger
        self.listParent = []

    def parent(self, parent):
        self.listParent.append(parent)

    def disturb(self):
        self.stateOfCalm = False

    def getHungry(self):
        self.stateOfHunger = False

    def printInfo(self):
        print('{}, возраст: {}'.format(self.name, self.age), end=' ')