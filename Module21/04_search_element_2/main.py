site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def findKey(d, key, l=3):
	if l != 0:
		if key in d:
			return d[key]
		for i in d.values():
			if isinstance(i, dict):
				result = findKey(i, key, l-1)
				if result: break
		else: result = None
		return result
key = input('Введите искомый ключ: ')
choice = input('Хотите установить '
         'максимальную длину поиска? ').lower()
if choice == 'да':
	print(findKey(site, key, l=int(input('Длина: '))))
elif choice == 'нет':
	print(findKey(site, key))
else:
	print('Введите "да" или "нет"')
