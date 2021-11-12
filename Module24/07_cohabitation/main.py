import random

from Human import Human
from House import House

def action(human):
    n = random.randint(1, 6)
    if human.degreeOfSatiety < 20:
        human.Eat()
    elif human.house.refrigeratorWithFood < 10:
        human.go_to_the_store_for_food()
    elif human.house.bedsideTableWithMoney < 50:
        human.Work()
    elif n == 1:
        human.Work()
    elif n == 2:
        human.Eat()
    else:
        human.Play()


house = House()
human1 = Human('Иван', house)
human2 = Human('Никита', house)

for i in range(365):
    action(human1)
    action(human2)
if human1.degreeOfSatiety > 0 :
    print('{} жив'.format(human1.name))
if human2.degreeOfSatiety > 0 :
    print('{} жив'.format(human2.name))

