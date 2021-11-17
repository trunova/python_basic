class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculation_of_taxes(self, n):
        return self.worth / n


class Appartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculation_of_taxes(self):
        return super().calculation_of_taxes(1000)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculation_of_taxes(self):
        return super().calculation_of_taxes(200)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculation_of_taxes(self):
        return super().calculation_of_taxes(500)


money = int(input('Введите количество ваших денег: '))
appartment = Appartment(int(input('Введите стоимость квартиры: ')))
car = Car(int(input('Введите стоимость машины: ')))
countryHouse = CountryHouse(int(input('Введите стоимость загородного дома: ')))
sumTaxes = appartment.calculation_of_taxes() + car.calculation_of_taxes() + countryHouse.calculation_of_taxes()
print('Налоги:\nНа квартиру = {}\nНа машину = {}\nНа загородный дом = {}'.format(
        appartment.calculation_of_taxes(),
        car.calculation_of_taxes(),
        countryHouse.calculation_of_taxes()
    ))
if sumTaxes > money: print('У вас не хватает суммы = {}, чтобы оплатить налоги.'.format(sumTaxes - money))