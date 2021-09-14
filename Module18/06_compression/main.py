abc = input('Введите строку: ')
newAbc = ''
i = 0
size = len(abc)
while i != size:
    newAbc += abc[i]
    j = i
    while abc[j] == abc[i]:
        j += 1
        if j == size: break
    newAbc += str(j - i)
    i = j

print('Закодированная строка:', newAbc)
