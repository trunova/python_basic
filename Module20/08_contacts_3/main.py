def convert(text):
    text = text.lower()
    return text[0].upper() + text[1:]

phone_book = dict()
while True:
    print('Выберите действие: ')
    print('1) “добавить контакт”')
    print('2) “найти человека в списке контактов по фамилии”')
    print('3) “выход”')
    act = int(input('Номер действия: '))

    if act == 1:
        name = (input('Имя: '), input('Фамилия: '))
        number = input('Номер телефона: ')
        if name in phone_book:
            print('{0} {1} уже есть в телефонной книге'.format(
                name[0],
                name[1]
            ))
        else: phone_book[(name)] = number
        print('Текущий словарь контактов: ')
        print(phone_book)

    elif act == 2:
        surname = input('Фамилия: ')
        surname = convert(surname)
        for i_initials, i_num in phone_book.items():
            if i_initials[1] == surname:
                print(i_initials, ':', i_num)
        else: print('Контакта с такой фамилией нет в списке')

    elif act == 3: break
    else: print('Действия под таким номером нет')

