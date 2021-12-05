from collections.abc import Iterable

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

def generator() -> Iterable[tuple]:
    for x in list_1:
        for y in list_2:
            result = x * y
            yield (x, y, result)
            if result == to_find:
                print('Found!!!')
                return

f = generator()
for i in f:
    print('{} + {} = {}'.format(i[0], i[1], i[2]))