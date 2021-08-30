def leastDivisor(a):
    divisor = a
    for i in range(2, a+1):
        if a % i == 0:
            return i
    return divisor

a = int(input('Введите число: '))
if a > 1:
    print('Наименьший делитель, отличный от единицы:', leastDivisor(a))
else: print('Введённое число <= 1')
