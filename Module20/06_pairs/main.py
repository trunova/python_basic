lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Оригинальный список:', lst)
newList = list()

newList = list(zip(lst[::2], lst[1::2]))
print('Новый список:', newList)

newList.clear()
for i in range(0, len(lst), 2):
    newList.append((lst[i], lst[i+1]))
print('Новый список:', newList)