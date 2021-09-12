n = int(input('Сколько элементов в списке? '))
listN = [int(input('Введите число: ')) for _ in range(n)]
print(listN)
for j in range(n - listN.count(0)):
    if listN[j] == 0:
        i = j + 1
        while listN[i] == 0:
            i += 1
            if i == len(listN): break
        else: listN[j], listN[i] = listN[i], listN[j]
listN = listN[:listN.index(0)]
print(listN)
