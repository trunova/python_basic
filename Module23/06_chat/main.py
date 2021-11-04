def actions():
    print('Выберите одно из действий(1 / 2): ')
    print('1) Посмотреть текущий текст чата')
    print('2) Отправить сообщение')
    print('3) Выйти из чата')
    return input('Ваш выбор: ')

username = input('Введите имя пользователя: ')
while True:
    try:
        act = actions()
        if act == '1':
            chat_file = open('chat.txt', 'r', encoding='utf-8')
            for i_line in chat_file:
                print(i_line, end=' ')
            chat_file.close()
        elif act == '2':
            message = input('Введите сообщение: ')
            chat_file = open('chat.txt', 'a+', encoding='utf-8')

            chat_file.write(username + ': ' + message + '\n')

            chat_file.flush()
            chat_file.close()
        elif act == '3':
            break
        else: raise ValueError()
    except  ValueError:
        print('Действие {} выбрать нельзя'.format(act))