import math
import random

class Automobile:
    def __init__(self, x, y, angle):
        self.__x = x
        self.__y = y
        if angle >= 0 and angle <= 360:
            self.__angle = angle

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def move(self, distance):
        self.__x += distance * round(math.cos(self.__angle), 2)
        self.__y += distance * round(math.sin(self.__angle), 2)

    def turn(self, angle):
        if self.__angle + angle >= 0 and self.__angle + angle <= 360:
            self.__angle += angle


class Bus(Automobile):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.__numberOfPassengers = 0
        self.__amountOfMoneyReceived = 0

    def get_numberOfPassengers(self):
        return self.__numberOfPassengers
    def get_amountOfMoneyReceived(self):
        return self.__amountOfMoneyReceived

    def goOut(self, number):
        self.__numberOfPassengers -= number

    def toComeIn(self, number):
        self.__numberOfPassengers += number

    def move(self, distance):
        super().move(distance)
        for i in range(distance // 50):
            n = random.randint(0, 8)
            self.toComeIn(n)
            self.__amountOfMoneyReceived += n * 10
            self.goOut(random.randint(0, self.__numberOfPassengers))

car = Automobile(8, 6, math.radians(270))
car.move(10)
print('Координаты машины после перемещения:\nx = {} y = {}'.format(car.get_x(), car.get_y()))

bus = Bus(0, 0, math.radians(30))
bus.move(200)
print('Координаты автобуса после перемещения:\nx = {} y = {}'.format(bus.get_x(), bus.get_y()))
print('Число пассажиров = {}, количество полученных денег = {}'.format(bus.get_numberOfPassengers(),
                                                                       bus.get_amountOfMoneyReceived()))
