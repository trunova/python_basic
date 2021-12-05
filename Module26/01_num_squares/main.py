from collections.abc import Iterable

class Iter:
    """ класс-итератор """
    def __init__(self, N: int):
        self.N = N
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.count < self.N:
            self.count += 1
            return self.count * self.count
        else: raise StopIteration

def generator(N: int) -> Iterable[int]:
    """ функция-генератор """
    for i in range(1, N + 1):
        yield i * i

N = int(input('Введите число: '))

""" генераторное выражение """
generatorN2 = (i * i for i in range(1, N + 1))

iterN = Iter(N)
for i in iterN:
    print(i, end=' ')
print()
generatorN = generator(N)
for i in generatorN:
    print(i, end=' ')
print()
for i in generatorN2:
    print(i, end=' ')
