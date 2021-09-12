stick = int(input('Кол-во палок: '))
listStick = ['I' for _ in range(stick)]
for i in range(int(input('Кол-во бросков: '))):
    print('Бросок', i+1, end='. ')
    n1 = int(input('Сбиты палки с номера '))-1
    n2 = int(input('по номер '))-1
    for i in range(n1, n2+1):
        listStick[i] = '.'
for i in range(stick): print(listStick[i], end='')