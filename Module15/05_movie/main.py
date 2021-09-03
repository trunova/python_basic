films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favoriteFilms = []
print('Сколько фильмов добавить в списак любимых?', end=' ')
for i in range(int(input())):
    print(i+1, 'фильм:', end=' ')
    film = input()
    if film in films:
        favoriteFilms.append(film)
    else: print('Фильма с таким названием нет на сайте, он не будет добавлен в список любимых')
print('Список любимых фильмов:', favoriteFilms)
