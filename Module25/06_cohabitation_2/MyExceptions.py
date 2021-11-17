class ManDiesOfHunger(Exception):
    def __init__(self, name = ''):
        self.name = name

class CatDiedOfHunger(Exception):
    def __init__(self, text = ''):
        self.txt = text

class ManDiesDepression(Exception):
    def __init__(self, name = ''):
        self.name = name

