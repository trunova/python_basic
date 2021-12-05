import sys

class QHofstadter:
    def __init__(self, lst: list):
        if lst == [1, 2]:
            sys.exit('Переданы значения [1, 2]')
        self.lst = lst[:]
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        try:
            self.count += 1
            if self.count == 1 or self.count == 2:
                return self.lst[self.count - 1]
            item = self.lst[-self.lst[-1]] + self.lst[-self.lst[-2]]
            self.lst.append(item)
            return item
        except IndexError:
            raise StopIteration()

qHofstadter = QHofstadter([1, 1])
for _ in range(10):
    print(next(qHofstadter))