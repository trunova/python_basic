def sort(listN):
    size = len(listN)
    for i in range(size - 1):
        minIndex = i;
        for j in range(i + 1, size):
            if listN[j] < listN[minIndex]:
                minIndex = j
        tmp = listN[i]
        listN[i] = listN[minIndex]
        listN[minIndex] = tmp
    return listN

listN = []
for i in range(int(input('Сколько элементов в изначальном списке? '))):
    print(i+1, 'элемент списка:', end=' ')
    listN.append(int(input()))
print('Изначальный список: ', listN)
print('Отсортированный список: ', sort(listN))
