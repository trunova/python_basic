from Gardener import Gardener
from GardenBed import GardenBed
from Potato import Potato

lst_potato = []
for i in range(5):
    lst_potato.append(Potato(i+1))

gardenBed = GardenBed(5)

gardener = Gardener('Марк', gardenBed)
gardener.take_care_of_the_garden()
gardener.take_care_of_the_garden()
gardener.harvest()
gardener.take_care_of_the_garden()
gardener.harvest()
gardener.take_care_of_the_garden()
