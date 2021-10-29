import os
s = input('Введите строку: ')
p = input('Куда хотите сохранить документ? '
                           'Введите последовательность папок (через пробел):\n').split(' ')
name = input('\nВведите имя файла:') + '.txt'
pathName = os.path.join(*p, name)
print(pathName)
f = open(name, 'r+')
if os.path.getsize(name) > 0:
    answer = input('Вы действительно хотите перезаписать файл? ').lower()
    if answer == 'да':
        f.write(s)
        print('Файл успешно перезаписан!')
else:
    f.write(s)
    print('Файл успешно сохранён!')
f.close()