listVideoCards = []
maxV = 0
for i in range(int(input('Кол-во видеокарт: '))):
    print(i+1, 'Видеокарта:', end=' ')
    v = int(input())
    listVideoCards.append(v)
    if v > maxV:
        maxV = v
print('Старый список видеокарт:', listVideoCards)
for _ in range(listVideoCards.count(maxV)):
    listVideoCards.remove(maxV)
print('Новый список видеокарт:', listVideoCards)


