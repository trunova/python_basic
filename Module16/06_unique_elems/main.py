list1 = []
print('Заполнение первого списка:')
for i in range(3):
    print('Введите', i+1, 'число:', end=' ')
    list1.append(int(input()))
list2 = []
print('Заполнение второго списка:')
for i in range(7):
    print('Введите', i+1, 'число:', end=' ')
    list2.append(int(input()))
print('Первый список: ', list1)
print('Второй список: ', list2)
for i in range(7):
    list1.append(list2[i])
list1 = set(list1)
print('Новый первый список с уникальными элементами:', list1)