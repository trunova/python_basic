import random

sum_num = 0
with open('numbers.txt', 'a') as num_file:
    while sum_num < 777:
        if random.randint(1, 13) == 1:
            raise BaseException('Случайное исключение')
        num = int(input('Введите число'))
        sum_num += num
        num_file.write(str(num) + '\n')