import random

class KillError(Exception):
    def __init__(self, text = ''):
        self.txt = text
class DrunkError(Exception):
    def __init__(self, text = ''):
        self.txt = text
class CarCrashError(Exception):
    def __init__(self, text = ''):
        self.txt = text
class GluttonyError(Exception):
    def __init__(self, text = ''):
        self.txt = text
class DepressionError(Exception):
    def __init__(self, text = ''):
        self.txt = text

def one_day():
    if random.randint(1, 10) == 1:
        n = random.randint(1, 5)
        if n == 1: raise KillError()
        elif n == 2: raise DrunkError()
        elif n == 3: raise CarCrashError()
        elif n == 4: raise GluttonyError()
        elif n == 5: raise DepressionError()
    return random.randint(1, 7)

CONST_KARMA = 500
karma = 0
with open('karma.log', 'a', encoding="utf-8") as karma_file:
    while karma != 500:
        try:
            karma += one_day()
            if karma > 500: karma = 500
        except KillError: karma_file.write('Исключение KillError, при карме = {}\n'.format(karma))
        except DrunkError: karma_file.write('Исключение DrunkError, при карме = {}\n'.format(karma))
        except CarCrashError: karma_file.write('Исключение CarCrashError, при карме = {}\n'.format(karma))
        except GluttonyError: karma_file.write('Исключение GluttonyError, при карме = {}\n'.format(karma))
        except DepressionError: karma_file.write('Исключение DepressionError, при карме = {}\n'.format(karma))