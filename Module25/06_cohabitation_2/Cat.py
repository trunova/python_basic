from MyExceptions import CatDiedOfHunger
from House import House

class Cat:
    """
    Базовый класс, описывающий кота

    Args:
        name (str): передаётся имя кота
        house (House): передаётся дом, в котором живёт кот
    """
    def __init__(self, name, house):
        self.__name = name
        self.__degreeOfSatiety = 30
        self.house = house

    def get_degreeOfSatiety(self):
        return self.__degreeOfSatiety

    def degreeOfSatietyLessThanZero(self):
        """
        Метод для проверки допустимого значения степени сытости

        :raise: Если степеь сытости < 0, вызывается исключение
        """
        if self.__degreeOfSatiety < 0:
            raise CatDiedOfHunger()

    def eat(self, n):
        """
        Метод "Принять в пищу" (увеличивает степень сытости)

        :param n: единицы еды
        :type n: int
        """
        if n >= 10:
            self.__degreeOfSatiety += 20
        else:
            self.__degreeOfSatiety += 2 * n

    def sleep(self):
        """ Метод "Спать" """
        self.__degreeOfSatiety -= 10
        self.degreeOfSatietyLessThanZero()

    def tearWallpaper(self):
        """ Метод "Драть обои" """
        self.__degreeOfSatiety -= 10
        self.house.pollution()
        self.degreeOfSatietyLessThanZero()



