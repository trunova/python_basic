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
listSkates = []
listPeople = []
for i in range(int(input('Кол-во коньков: '))):
    print('Размер', i+1,'пары:', end=' ')
    listSkates.append(int(input()))
for i in range(int(input('Кол-во людей: '))):
    print('Размер ноги', i+1,'человека:', end=' ')
    listPeople.append(int(input()))
n = 0
listSkates = sort(listSkates)
for j in range(len(listPeople)):
    for i in range(len(listSkates)):
        if listSkates[i] >= listPeople[j]:
            n += 1
            listSkates.remove(listSkates[i])
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', n)
