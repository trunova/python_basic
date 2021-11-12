class Water:
    name = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Lightning):
            return Life()
        else: return None

class Earth:
    name = 'Земля'
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else: return None

class Fire:
    name = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Lightning):
            return Plasma()
        else: return None

class Air:
    name = 'Воздух'
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else: return None

class Lightning:
    name = 'Молния'
    def __add__(self, other):
        if isinstance(other, Water):
            return Life()
        elif isinstance(other, Fire):
            return Plasma()
        else: return None

class Dust:
    name = 'Пыль'

class Lava:
    name = 'Лава'

class Dirt:
    name = 'Грязь'

class Storm:
    name = 'Шторм'

class Steam:
    name = 'Пар'

class Life:
    name = 'Жизнь'

class Plasma:
    name = 'Плазма'

water = Water()
fire= Fire()

print('{} + {} = {}'.format(water.name, fire.name, (fire + water).name))
