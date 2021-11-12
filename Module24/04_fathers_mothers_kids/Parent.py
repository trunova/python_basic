class Parent:
    def __init__(self, name, age, listChild = None):
        self.name = name
        self.age = age
        self.listChild = []
        for i_child in listChild:
            if self.is_a_child(i_child):
                self.listChild.append(i_child)
        if len(self.listChild) != 0:
            for i_child in self.listChild:
                i_child.parent(self)

    def is_a_child(self, child):
        return self.age - child.age >= 16

    def reportInformationAboutYourself(self):
        print('Имя: {}, возраст: {}'.format(self.name, self.age), end='')
        if len(self.listChild) != 0:
            print(', дети:', end=' ')
            for i_child in self.listChild:
                i_child.printInfo()
        print()

    def calmTheChild(self, child):
        try:
            if child in self.listChild:
                child.stateOfCalm = True
            else: raise ValueError
        except ValueError: print('У родителя {} нет такого ребёнка'.format(self.name))

    def feedTheChild(self, child):
        try:
            if child in self.listChild:
                child.stateOfHunger = True
            else:
                raise ValueError
        except ValueError:
            print('У родителя {} нет такого ребёнка'.format(self.name))