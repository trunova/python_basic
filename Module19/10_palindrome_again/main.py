str = input('Введите строку: ').lower()
dict_str = dict()
for i in str:
    if i in dict_str:
        dict_str[i] += 1
    else: dict_str[i] = 1
k = 0
for i in dict_str:
    if dict_str[i] % 2 != 0:
        k += 1
    if k == 2:
        print('Нельзя сделать палиндромом')
        break
else: print('Можно сделать палиндромом')
