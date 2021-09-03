def reversWorld(world1):
    world2 = ''
    for i in range(len(world1) - 1, -1, - 1):
        world2 += world1[i]
    return world2

world = input('Введите слово: ')
if world == reversWorld(world):
    print('Слово является палиндромом')
else: print('Слово не является палиндромом')