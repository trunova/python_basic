import math
import random
from Player import Player
from Card import Card

player = Player('игрок')
dealer = Player('дилер')

player.choose_a_card(count=2)
dealer.choose_a_card(count=2)

while True:
    print('Ваша рука:')
    for i in player.Hand:
        print(i.name)
    print('Сумма ваших очков: {}'.format(player.sumOfPoints))
    print('Выберете действие:\n(1)Взять карту\n(2)Остановиться')
    action = int(input('Выбор '))
    if action == 1:
        player.choose_a_card()
    elif action == 2:
        print('Очки игрока: {}\nОчки дилера: {}'.format(player.sumOfPoints, dealer.sumOfPoints))
        if player.is_win(dealer):
            print('Вы выиграли!')
        else: print('Дилер выиграл')
        break
    else: print('Действие под номером {} выполнить нельзя'.format(action))



