s = input('Введите строку: ')
newS = s[0].upper()
for i in range(1, len(s)):
    if s[i-1] == ' ' and s[i] != ' ':
        newS += s[i].upper()
    else: newS += s[i]
print('Результат:', newS)