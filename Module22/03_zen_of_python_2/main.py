file_zen = open('D:\\Python\\Projects\\python_basic\\Module22\\02_zen_of_python\\zen.txt', 'r', encoding='utf-8')
lines = 0
letters = 0
words = 0
for i_line in file_zen:
    lines += 1
    w = 0
    s = 0
    for i_letter in i_line:
        if i_letter == ' ' or i_letter == '.' or i_letter == '!' or i_letter == ',':
            if s != 0:
                w += 1
                letters += s
                s = 0
        elif i_letter != '\'' and i_letter != '-' and i_letter != '*':
            s += 1
    words += w
print('Количество букв латинского алфавита: ', letters)
print('Количество слов: ', words)
print('Количество строк: ', lines)
file_zen.close()