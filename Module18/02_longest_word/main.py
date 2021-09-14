wordList = input('Введите строку: ').split(' ')
longWord = ''
for i in wordList:
    if len(i) > len(longWord):
        longWord = i
print('Самое длинное слово:', longWord, 'его длина =', len(longWord))