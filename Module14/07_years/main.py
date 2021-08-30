firstYear = int(input('Введите первый год: '))
secondYear = int(input('Введите второй год: '))
print('Года от 1900 до 2100 с тремя одинаковыми цифрами:')
for i in range(firstYear, secondYear + 1):
    k1 = i % 10
    k2 = i % 100 // 10
    k3 = i // 100 % 10
    k4 = i // 1000
    if (k1 != k2 and k2 == k3 == k4) or (k1 != k2 and k1 == k3 == k4) or (k1 != k3 and k1 == k2 == k4) or (k1 != k4 and k1 == k2 == k3):
        print(i)


