word = input('Введите слово: ')
k = 0
for i in word:
    if word.count(i) == 1:
        k += 1
print('Кол-во уникальных букв:', k)