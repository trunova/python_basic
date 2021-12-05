from typing import Any, Optional
from collections.abc import Iterable
import os

def gen_files_path(catalog: str, directory = os.path.abspath(os.sep)) -> str:
    for filename in os.listdir(directory):
        if filename == catalog:
            return
        yield directory + '\\' + filename

directory = input('Введите директорию: ')
catalog = input('Введите каталог: ')
if directory == '':
    genFilesPath = gen_files_path(catalog)
else: genFilesPath = gen_files_path(catalog, directory=directory)

for i in genFilesPath:
    print(i)