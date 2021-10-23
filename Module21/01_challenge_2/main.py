def allNum(num):
    if num > 0:
        allNum(num - 1)
        print(num)


allNum(int(input('Сколькоцифр выводить? ')))