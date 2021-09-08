violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

numberOfSongs = int(input('Сколько песен выбрать? '))
n = 0
for i in range(numberOfSongs):
    print('Название', i+1, 'песни:', end=' ')
    name = input()
    for j in violator_songs:
        if j[0] == name:
            n += j[1]
            break
    else: print('В списке нет такой песни')
print('Общее время звучания песен: ', n, 'минут')