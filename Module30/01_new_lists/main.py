from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


if __name__ == "__main__":
    result1 = list(map(lambda num: round(num * num * num, 3), floats))
    result2 = list(filter(lambda name: len(name) >= 5, names))
    result3 = reduce(lambda a, b: a + b, numbers)
    print(result1, "\n", result2, "\n", result3)
