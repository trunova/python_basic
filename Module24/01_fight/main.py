import random

class Warrior:
    health = 100
    def __init__(self, name):
        self.name = name

    def hit(self, warrior):
        warrior.health -= 20
        print('Атаковал {}, у {} осталось {} здоровья'.format(self.name,
                                                              warrior.name,
                                                              warrior.health))
        if warrior.health <= 0:
            print('Победу одержал {}'.format(self.name))
        return warrior.health > 0


warrior1 = Warrior('Воин01')
warrior2 = Warrior('Воин02')
hit = True
while hit:
    if random.randint(0, 1) == 0:
        hit = warrior1.hit(warrior2)
    else:
        hit = warrior2.hit(warrior1)