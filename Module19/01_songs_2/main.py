violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
time = 0
for i in range(int(input('Сколько песен выбрать? '))):
    print('Название {0} песни:'.format(i+1), end=' ')
    song = violator_songs.get(input())
    if song != None:
        time += song
    else: print('Ошибка: такой песни нет в списке')
print('Общее время звучания песен: {0} минут'.format(round(time, 2)))