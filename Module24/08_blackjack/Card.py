class Card:
    priceValuesString = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   '10': 10, 'валет': 10, 'дама': 10, 'король': 10, 'туз': [1, 11]}

    def __init__(self, name):
        try:
            if name.lower() in self.priceValuesString.keys():
                self.name = name.lower()
                self.value = self.priceValuesString.get(name)
            else: raise ValueError()
        except ValueError: print('Карты {} не может существовать'.format(role))