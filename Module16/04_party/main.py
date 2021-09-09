guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    statys = input('Гость пришел или ушел? ')
    if statys == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) >= 6:
             print('Прости, '+ name + ', но мест нет')
        else:
            print('Привет, ' + name + '!')
            guests.append(name)
    elif statys == 'ушел':
        name = input('Имя гостя: ')
        if name in guests:
            print('Пока, ' + name + '!')
            guests.remove(name)
        else: print('Гостя с таким именем нет на вечеринке')
    elif statys == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break