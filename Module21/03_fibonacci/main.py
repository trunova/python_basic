def findNum(num_pos):
    if num_pos >= 3:
        return findNum(num_pos - 1) + findNum(num_pos - 2)
    elif num_pos > 0: return 1
    else: return 0


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число: {0}'.format(findNum(num_pos)))