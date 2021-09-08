people = int(input('Кол-во человек: '))
num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', num, 'человек')
listNum = []
for i in range(1, people + 1):
    listNum.append(i)
start = 0
for _ in range(people - 1):
    print('Текущий круг людей:', listNum)
    print('Начало счёта с номера', listNum[start])
    ind = start + num - 1
    while len(listNum) <= ind:
        ind -= len(listNum)
    print('Выбывает человек под номером', listNum[ind])
    print()
    listNum.remove(listNum[ind])
    if ind == len(listNum): start = 0
    else: start = ind
print('Остался человек под номером', listNum[0])
