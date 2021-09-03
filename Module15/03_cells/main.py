n = int(input('Кол-во клеток: '))
unsuitableList = []
for i in range(1, n + 1):
    print('Эффективность', i, 'клетки:', end= ' ')
    k = int(input())
    if k < i:
        unsuitableList.append(k)
print('Неподходящие значения:', end=' ')
for i in unsuitableList:
    print(i, end=' ')
