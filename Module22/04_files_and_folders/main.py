import os

def count_dir(path):
    numberOfSubdirectories = 0
    numberOfFiles = 0
    catalogSize = 0
    for i_elem in os.listdir(path):
        newPath = os.path.join(path, i_elem)
        if os.path.isdir(newPath):
            numberOfSubdirectories += 1
            d = count_dir(newPath)
            catalogSize += d[0]
            numberOfSubdirectories += d[1]
            numberOfFiles += d[2]
        else:
            numberOfFiles += 1
            catalogSize += os.path.getsize(newPath) / 1024
    return [catalogSize, numberOfSubdirectories, numberOfFiles]

path = input('Введите путь до каталога: ')
lst = count_dir(path)
print('Размер каталога (в Кб):', lst[0])
print('Количество подкаталогов:', lst[1])
print('Количество файлов:', lst[2])
