from MyExceptions import ManDiesDepression

class House:
    """
    Базовый класс, описывающий дом

    __eat: количество съеденной еды
    """
    __eat = 0
    def __init__(self):
        self.__amountOfMoneyInTheNightstand = 100
        self.__amountOfFoodInTheRefrigerator = 50
        self.__catFood = 30
        self.__amountOfDirt = 0

    def get_eat(self):
        return self.__eat

    def aLotOfDirt(self):
        """
        Метод для проверки допустимого значения загрязнённости дома

        :return: bool
        """
        if self.__amountOfDirt > 90:
            return True
        return False

    def add_amountOfMoneyInTheNightstand(self, money):
        """
        Метод добавления денег в тумбочку

        :param money: заработанные деньги
        :type money: int
        """
        self.__amountOfMoneyInTheNightstand += money

    def add_foot(self, foodForHuman, foodForCat):
        """
        Метод добавления еды домой

        :param foodForHuman: единицы еды для людей
        :type foodForHuman: int
        :param foodForCat: единицы еды для кота
        :type foodForCat: int
        """
        self.spendMoney(foodForHuman + foodForCat)
        self.__amountOfFoodInTheRefrigerator += foodForHuman
        self.__catFood += foodForCat

    def spendMoney(self, money):
        """
        Метод "Потратить деньги"

        :param money: количество денег, которые нужно потратить
        :type money: int
        :raise: Если денег в тумбочке не хватает, вызывается исключение
        """
        if self.__amountOfMoneyInTheNightstand >= money:
            self.__amountOfMoneyInTheNightstand -= money

    def pollution(self):
        """ Метод "Загрязнение дома" """
        self.__amountOfDirt += 5

    def cleaning(self, n):
        """
        Метод "Уборка дома"

        :param n: количество единиц уборки
        :type n: int
        """
        self.__amountOfDirt -= n

    def eating(self, n):
        """
        Метод "Принять в пищу" (уменьшает количество еды)

        :param n: единицы еды
        :type n: int
        """
        if self.__amountOfFoodInTheRefrigerator <= n:
            self.__amountOfFoodInTheRefrigerator = 0
            self.__eat += self.__amountOfFoodInTheRefrigerator
        else:
            self.__amountOfFoodInTheRefrigerator -= n
            self.__eat += n



    def get_amountOfMoneyInTheNightstand(self):
        """
        Геттер для количества денег
        :return: __amountOfMoneyInTheNightstand
        :rtype: int
        """
        return self.__amountOfMoneyInTheNightstand

    def get_amountOfFoodInTheRefrigerator(self):
        """
        Геттер для количества еды людей
        :return: __amountOfFoodInTheRefrigerator
        :rtype: int
        """
        return self.__amountOfFoodInTheRefrigerator

    def get_catFood(self):
        """
        Геттер для количества еды кота
        :return: __catFood
        :rtype: int
        """
        return self.__catFood

    def get_amountOfDirt(self):
        """
        Геттер для степени загрязнённости дома
        :return: __amountOfDirt
        :rtype: int
        """
        return self.__amountOfDirt