k = int(input('Сдвиг: '))
listN = []
for i in range(int(input('Сколько элементов в изначальном списке? '))):
    print(i+1, 'элемент списка:', end=' ')
    listN.append(int(input()))
print('Изначальный список: ', listN)
newListN = []
for i in range(len(listN) - k, len(listN)):
    newListN.append(listN[i])
for i in range(len(listN) - k):
    newListN.append(listN[i])
print('Сдвинутый список:', newListN)