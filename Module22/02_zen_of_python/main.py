file_zen = open('zen.txt', 'r', encoding='utf-8')
listLine = list()
for iLine in file_zen:
    listLine.append(iLine)
file_zen.close()
print(listLine[len(listLine) - 1])
for iLine in range(len(listLine) - 2, -1, -1):
    print(listLine[iLine], end='')