import random

from MyExceptions import ManDiesDepression, ManDiesOfHunger, CatDiedOfHunger
from Wife import Wife
from Husband import Husband
from Cat import Cat
from House import House

house = House()
wife = Wife('Emily', house)
husband = Husband('Martin', house)
cat = Cat('Tom', house)

try:
    for i_day in range(365):
        n = random.randint(1, 4)
        if wife.get_degreeOfSatiety() <= 10:
            wife.eat(20)
        elif wife.get_degreeOfHappiness() <= 5:
            wife.petTheCat()
        elif house.get_amountOfDirt() > 60:
            wife.cleanTheHouse()
        elif house.get_amountOfFoodInTheRefrigerator() < 10:
            wife.buyFood(50, 0)
        elif house.get_catFood() < 5:
            wife.buyFood(0, 30)
        elif n == 3:
            wife.cleanTheHouse()
        elif n == 2: wife.buyFurCoat()
        else: wife.eat(10)

        if husband.get_degreeOfSatiety() <= 10:
            husband.eat(20)
        elif husband.get_degreeOfHappiness() <= 5:
            husband.petTheCat()
        elif house.get_amountOfMoneyInTheNightstand() < 7000:
            husband.goToWork()
        elif n == 4: husband.play()
        else: husband.eat(10)

        if cat.get_degreeOfSatiety() < 10:
            cat.eat(20)
        elif n == 3: cat.sleep()
        elif n == 4: cat.tearWallpaper()
        else: cat.eat(5)

        if house.aLotOfDirt():
            wife.decreaseDegreeOfHappiness(10)
            husband.decreaseDegreeOfHappiness(10)
            cat.decreaseDegreeOfHappiness(10)

except ManDiesDepression: print('Один из членов семью умер от депрессии')
except ManDiesOfHunger: print('Один из членов семью умер от голода')
except CatDiedOfHunger: print('Кот умер от голода')

print('За год заработано денег = {}, куплено шуб = {}, съедено еды = {}'.format(husband.get_money(),
                                                                                wife.get_furCoat(),
                                                                                house.get_eat()))