from Potato import Potato
class GardenBed:

    def __init__(self, count):
        self.listPotatos = [Potato(index) for index in range(1, count + 1)]

    def growAll(self):
        print('Вся картошка прорастает!\n')
        for i_potato in self.listPotatos:
            i_potato.grow()
        print()

    def are_all_ripe(self):
        if all([i_potato.is_ripe() for i_potato in self.listPotatos]):
            print('Вся картошка созрела. Можно собирать!\n')
            return True
        else:
            print('Картошка ещё не созрела\n')
            return False
