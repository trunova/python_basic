dictSynonyms = dict()
for i in range(int(input('Введите количество пар слов: '))):
    listWorlds = input('{0} пара: '.format(i+1)).lower().split(' - ')
    dictSynonyms[listWorlds[0]] = listWorlds[1]
    dictSynonyms[listWorlds[1]] = listWorlds[0]
while True:
    w = input('Введите слово: ').lower()
    if w in dictSynonyms:
        print('Синоним: {0}'.format(dictSynonyms.get(w)))
    elif w == 'end': break
    else: print('Такого слова в словаре нет.')
