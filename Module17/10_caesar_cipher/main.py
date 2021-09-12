alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
            'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
            'э', 'ю', 'я']
str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
encryptedMessage = ''
for i in str:
    if i == ' ' or i == ',' or i == '.' or i == '!' or i == '?':
        encryptedMessage += i
    elif i in alphabet:
        ind = alphabet.index(i) + shift
        if ind >= len(alphabet):
            ind -= len(alphabet)
        encryptedMessage += alphabet[ind]
print('Зашифрованное сообщение:', encryptedMessage)