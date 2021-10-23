
def move(N, startTower, additionalTower, endTower):
    if (N == 1):
        print('Переложить диск 1 со стержня номер {} на стержень номер {}'.format(startTower, endTower))
        return
    move(N - 1, startTower, endTower, additionalTower)
    print('Переложить диск {} со стержня номер {} на стержень номер {}'.format(N, startTower, endTower))
    move(N - 1, additionalTower, startTower, endTower)

N = int(input('Введите количество дисков: '))
move(N, '1', '2', '3')