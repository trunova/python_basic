str = input('Введите строку: ')
print('Полученая последовательность:',str[len(str) - str[::-1].index('h') - 2 : str.index('h') : -1])