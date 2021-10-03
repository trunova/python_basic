lst = list()
str = input('Строка: ')
nums = input('Кортеж чисел: ')
n = nums.split(', ')
for i in range(len(n)):
    lst.append((str[i], n[i]))
    if i == len(str) - 1:
        break
print('Результат:')
for i in lst:
    print(i)