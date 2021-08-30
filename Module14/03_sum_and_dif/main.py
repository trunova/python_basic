def sum1(N):
    s = 0
    while N != 0:
        s += N % 10
        N //= 10
    return s
def sum2(N):
    s = 0
    while N != 0:
        s += 1
        N //= 10
    return s
N = int(input('Введите число: '))
print('Сумма цифр:', sum1(N))
print('Кол-во цифр в числе:', sum2(N))
print('Разность суммы и кол-ва цифр:', abs(sum1(N) - sum2(N)))
