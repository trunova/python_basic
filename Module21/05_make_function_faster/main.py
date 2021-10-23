import math

def calculating_math_func(data, factorials):
    if data in factorials:
        result = factorials[data]
    else:
        result = math.factorial(data)
        factorials[data] = result
        result /= data ** 3
        result = result ** 10
    return result

factorials = {}
while True:
    data = int(input('Введите число: '))
    print('Результат: {}'.format(calculating_math_func(data, factorials)))
    print(factorials)