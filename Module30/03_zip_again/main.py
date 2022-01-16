from typing import List


strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

results = list(map(lambda a, b: (a, b), strings, numbers))

if __name__ == "__main__":
    print(results)
