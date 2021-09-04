listContainers = []
for i in range(int(input('Кол-во контейнеров: '))):
    w = int(input('Введите вес контейнера: '))
    if w < 200:
        listContainers.append(w)
    else: print('Вес контейнера не должен превышать 200 кг')
newW = int(input('Введите вес нового контейнера: '))
newI = len(listContainers) + 1
if newW < 200:
    for i in range(len(listContainers)):
        if newW > listContainers[i]:
            newI = i + 1
            break
else:
    print('Вес нового контейнера не должен превышать 200 кг')
print('Номер, куда встанет новый контейнер:', newI)
