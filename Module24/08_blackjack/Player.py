import random
from Card import Card

class Player:
    priceValuesInt = {1: 'туз', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                      10: ['валет', 'дама', 'король']}
    rl = ['игрок', 'дилер']
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10.0, 10.1, 10.2]

    def __init__(self, role):
        self.sumOfPoints = 0
        self.Hand = list()
        try:
            if role.lower() in self.rl:
                self.role = role.lower()
            else: raise ValueError()
        except ValueError: print('Роли {} не может существовать'.format(role))

    def choose_a_card(self, count = 1):
        if len(self.lst) == 0:
            print('В колоде нет больше карт!')
        else:
            for _ in range(count):
                n = random.choice(self.lst)
                print(n)
                if int(n) == 10:
                    self.Hand.append(Card(self.priceValuesInt.get(10)[int(str(n)[3:])]))
                else:
                    self.Hand.append(Card(self.priceValuesInt.get(n)))
                self.lst.remove(n)
                if n == 1 and self.sumOfPoints + 11 <= 21:
                    n = 11
                self.sumOfPoints += int(n)

    def is_win(self, dealer):
        return self.sumOfPoints < 21 and (self.sumOfPoints == 21 or self.sumOfPoints > dealer.sumOfPoints)