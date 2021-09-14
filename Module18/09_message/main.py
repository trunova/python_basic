message = input('Сообщение: ')
newMessage = ''
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s = ''
for i in message:
    if i in alphabet:
        s += i
    else:
        newMessage += s[::-1]
        newMessage += i
        s = ''
print('Новое сообщение:', newMessage)