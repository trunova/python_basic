class Human:

    def __init__(self, name, house, degreeOfSatiety = 50):
        self.name = name
        self.degreeOfSatiety = degreeOfSatiety
        self.house = house
        self.house.listHumans.append(self)


    def Eat(self):
        if self.degreeOfSatiety <= 30:
            self.degreeOfSatiety += 20
        else: self.degreeOfSatiety = 50
        if self.house.refrigeratorWithFood >= 20:
            self.house.refrigeratorWithFood -= 20
        else: self.house.refrigeratorWithFood = 0

    def Work(self):
        if self in self.house.listHumans:
            self.house.bedsideTableWithMoney += 60
            self.degreeOfSatiety -= 10
            if self.degreeOfSatiety <= 0:
                self.house.listHumans.remove(self)
                print('{} умер'.format(self.name))

    def Play(self):
        if self in self.house.listHumans:
            self.degreeOfSatiety -= 10
            if self.degreeOfSatiety <= 0:
                self.house.listHumans.remove(self)
                print('{} умер'.format(self.name))

    def go_to_the_store_for_food(self):
        if self.house.bedsideTableWithMoney >= 20:
            self.house.refrigeratorWithFood += 100
            self.house.bedsideTableWithMoney -= 20