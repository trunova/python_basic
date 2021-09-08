countNum = int(input('Кол-во чисел: '))
listN = []
for i in range(countNum):
    listN.append(int(input('Число:')))
print('Последовательность: ', listN)
startInd = 0
endInd = countNum - 1
start = startInd
while True:
    if listN[endInd] != listN[startInd]:
        startInd += 1
    else:
        start = startInd
        if startInd == endInd:
            k += countNum - 1
            for i in range(countNum - 2, -1, -1):
                listN.append(listN[i])
            break
        else:
            while endInd > startInd:
                if listN[endInd] == listN[startInd]:
                    startInd += 1
                    endInd -= 1
                else:
                    startInd = start + 1
                    endInd = countNum - 1
                    break
            else:
                for i in range(start - 1, -1, -1):
                    listN.append(listN[i])
                break
print('Нужно приписать чисел:', start)
print('Сами числа: ', end= '')
for i in range(countNum, len(listN)):
    print(listN[i], end=' ')