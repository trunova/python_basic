from Human import Human
from House import House

class Husband(Human):
    """
    Класс Муж. Родитель: Human

    __money: количество заработанных денег

    Args:
        name (str): передаётся имя человека
        house (House): передаётся дом, в котором живёт человек
    """
    __money = 0
    def __init__(self, name, house):
        super().__init__(name, house)

    def get_money(self):
        return self.__money

    def play(self):
        """
        Метод "Играть в компьютер"
        (степень счастья растёт)
        """
        self.decreaseDegreeOfSatiety(10)
        self.increaseDegreeOfHappiness(20)

    def goToWork(self):
        """
        Метод "Ходить на работу"
        (прибавляются деньги)
        """
        self.decreaseDegreeOfSatiety(10)
        self.house.add_amountOfMoneyInTheNightstand(150)
        self.__money += 150
