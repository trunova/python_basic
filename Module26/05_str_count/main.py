import os
from collections.abc import Iterable


def get_path(directory: str) -> Iterable[str]:
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            yield filename

directory = input("Введите путь до директории: ")
line_count = 0
file = get_path(directory)
for filename in file:
    with open(directory + '\\' + filename, 'r', encoding='utf-8') as file_py:
        for line in file_py:
            if not line == '\n' and not line.startswith("#"):
                line_count += 1
print('Общее количество строк кода = {}'.format(line_count))