class Gardener:

    def __init__(self, name, gardenBed):
        self.name = name
        self.gardenBed = gardenBed

    def take_care_of_the_garden(self):
        if len(self.gardenBed.listPotatos) != 0:
            self.gardenBed.growAll()
        else: print('Вся картошка уже собрана\n')


    def harvest(self):
        if self.gardenBed.are_all_ripe():
            self.gardenBed.listPotatos = []
            print('Урожай собран.\n')