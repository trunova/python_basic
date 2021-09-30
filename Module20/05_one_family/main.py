family = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Попов", "Никита"): 28,
    ("Попова", "Екатерина"): 28,
    ("Попова", "Дарья"): 7,
    ("Попов", "Дмитрий"): 5,
    ("Ковалёв", "Сергей"): 34,
    ("Ковалёва", "Виктория"): 10,
    ("Шмелёв", "Иван"): 35,
    ("Шмелёва", "Мария"): 34,
    ("Шмелёва", "Маргарита"): 10,
}

surname = input('Введите фамилию: ')
s = [surname]
if surname[len(surname) - 1] == 'а':
    s.append(surname[:len(surname) - 1])
else: s.append(surname + 'а')

for i_initials, i_age in family.items():
    if i_initials[0] in s:
        print(i_initials[0], i_initials[1], i_age)