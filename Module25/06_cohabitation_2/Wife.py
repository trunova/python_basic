import random

from Human import Human
from House import House

class Wife(Human):
    """
    Класс Жена. Родитель: Human

    __furCoat: количество купленных шуб

    Args:
        name (str): передаётся имя человека
        house (House): передаётся дом, в котором живёт человек
    """
    __furCoat = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def get_furCoat(self):
        return self.__furCoat

    def buyFood(self, foodForHuman, foodForCat):
        """
        Метод "Купить продукты"

        :param foodForHuman: количество единиц еды для людей, которое нужно приобрести
        :type foodForHuman: int
        :param foodForCat: количество единиц еды для кота, которое нужно приобрести
        :type foodForCat: int
        """
        self.decreaseDegreeOfSatiety(10)
        self.house.add_foot(foodForHuman, foodForCat)
    def buyFurCoat(self):
        """
        Метод "Покупка шубы"
        (степень счастья растёт)
        """
        self.decreaseDegreeOfSatiety(10)
        self.house.spendMoney(350)
        self.__furCoat += 1
        self.increaseDegreeOfHappiness(60)


    def cleanTheHouse(self):
        """
        Метод "Уборка дома"
        """
        self.decreaseDegreeOfSatiety(10)
        self.house.cleaning(random.randint(30, 100))