n = int(input('Введите максимальное число: '))
listN = list()
while True:
    s = input('Нужное число есть среди вот этих чисел: ')
    if s == 'Помогите!' or len(listN) == 1:
        print('Артём мог загадать следующие числа:', end=' ')
        for i in listN: print(i, end=' ')
        break
    else:
        answer = input('Ответ Артёма: ').lower()
        if answer == 'нет':
            for i in s.split(' '):
                if int(i) in listN:
                    listN.remove(int(i))
        elif answer == 'да':
            listN.clear()
            for i in s.split(' '):
                listN.append(int(i))