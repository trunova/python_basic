import math
def reversNumber(N):
    fractionalPart = '.'
    wholePart = ''
    i = len(N) - 1
    while N[i] != '.':
        fractionalPart += N[i]
        i -= 1
    i -= 1
    while i != -1:
        wholePart += N[i]
        i -= 1
    return wholePart + fractionalPart

N1 = input('Введите первое число: ')
N2 = input('Введите второе число: ')
print('Первое число наоборот:', reversNumber(N1))
print('Второе число наоборот:', reversNumber(N2))
print('Сумма:', float(reversNumber(N1)) + float(reversNumber(N2)))







