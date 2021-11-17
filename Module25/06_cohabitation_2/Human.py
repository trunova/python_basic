from MyExceptions import ManDiesDepression, ManDiesOfHunger
from House import House

class Human:
    """
    Базовый класс, описывающий человека

    Args:
        name (str): передаётся имя человека
        house (House): передаётся дом, в котором живёт человек
    """
    def __init__(self, name, house):
        self.__name = name
        self.__degreeOfSatiety = 30
        self.__degreeOfHappiness = 100
        self.house = house

    def get_degreeOfSatiety(self):
        return self.__degreeOfSatiety

    def get_degreeOfHappiness(self):
        return self.__degreeOfHappiness

    def degreeOfSatietyLessThanZero(self):
        """
        Метод для проверки допустимого значения степени сытости

        :raise: Если степеь сытости < 0, вызывается исключение
        """
        if self.__degreeOfSatiety < 0:
            raise ManDiesOfHunger(self.__name)

    def degreeOfHappinessLessThanZero(self):
        """
        Метод для проверки допустимого значения степени счастья

        :raise: Если степеь счастья < 0, вызывается исключение
        """
        if self.__degreeOfHappiness < 0:
            raise ManDiesDepression(self.__name)

    def decreaseDegreeOfSatiety(self, n):
        """
        Метод для уменьшения степени сытости на n единиц сытости

        :param n: единицы сытости
        :type n: int
        """
        self.__degreeOfSatiety -= n
        self.degreeOfSatietyLessThanZero()

    def decreaseDegreeOfHappiness(self, n):
        """
        Метод для уменьшения степени счастья на n единиц счастья

        :param n: единицы счастья
        :type n: int
        """
        self.__degreeOfSatiety -= n
        self.degreeOfHappinessLessThanZero()

    def increaseDegreeOfHappiness(self, n):
        """
        Метод для увеличения степени счастья на n единиц счастья

        :param n: единицы счастья
        :type n: int
        """
        self.__degreeOfHappiness += n

    def eat(self, n):
        """
        Метод "Принять в пищу" (увеличивает степень сытости)

        :param n: единицы еды
        :type n: int
        """
        if n > 30: n = 30
        self.__degreeOfSatiety += n
        self.house.eating(n)

    def petTheCat(self):
        """
        Метод "Гладить кота" (увеличивает степень счастья)
        :param cat: кот
        :type cat: Cat
        """
        self.__degreeOfHappiness += 5
