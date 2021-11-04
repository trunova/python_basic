import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            if len(nums_list) < 2:
                raise IndexError()
            elif not (nums_list[0].isdigit() and nums_list[1].isdigit()):
                raise ValueError()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            with open('result.txt', 'a') as file_2:
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(str(my_list)) + '\n')
except TypeError:
    print('Ошибка: В файл может быть записана только строка')
except IndexError:
    print('Ошибка: В строке файла должно быть два значения')
except ValueError:
    print('Ошибка: Значения не являются числами')