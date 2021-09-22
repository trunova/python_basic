def dictionaryInversion(dictText):
    newDictText = {i:[j for j in dictText if dictText.get(j) == i]
                   for i in set(dictText.values())}
    return newDictText

def printDict(d):
    for i in sorted(d.keys()):
        print(i, ':', d[i])

text = input('Введите текст: ')
dictText = dict()
for i in text:
    if i in dictText:
        dictText[i] +=1
    else: dictText[i] = 1
print('Оригинальный словарь частот:')
printDict(dictText)
print('Инвертированный словарь частот:')
newDictText = dictionaryInversion(dictText)
printDict(newDictText)
