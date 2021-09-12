str = input('Введите текст: ')
k = 0
listVowels2 = [x for x in str if x in 'аеёиоуыэюя']
print('Список гласных букв:', listVowels2)
print('Длина списка:', len(listVowels2))
