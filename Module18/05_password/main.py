def threeDigits(password):
    k = 0
    for i in password:
        if i == '0' or i == '1' or\
                i == '2' or i == '3' or i == '4' or\
                i == '5' or i == '6' or i == '7' or\
                i == '8' or i == '9':
            k += 1
    return k >= 3
def capitalLetter(password):
    for i in password:
        if i.isupper():
            return True
    else: return False

while True:
    password = input('Придумайте пароль: ')
    if threeDigits(password):
        if len(password) >= 8:
            if capitalLetter(password):
                print('Это надёжный пароль!')
                break
            else: print('Пароль ненадёжный. Попробуйте ещё раз.')
        else: print('Пароль ненадёжный. Попробуйте ещё раз.')
    else: print('Пароль ненадёжный. Попробуйте ещё раз.')

