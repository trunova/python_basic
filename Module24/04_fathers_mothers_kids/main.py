from Parent import Parent
from Child import Child

child1 = Child('Маша', 12)
p1 = Parent('Владимир', 32, [child1])
p2 = Parent('Екатерина', 22, [child1])
p1.reportInformationAboutYourself()
p2.reportInformationAboutYourself()

