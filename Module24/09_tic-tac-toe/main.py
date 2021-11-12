from Field import Field
from Player import Player

field = Field()
field.printField()

print('Кто ходит первым?\n(1)Вы\n(2)Бот')
choice = int(input('Выбор: '))
if choice == 1:
    player = Player('x', field)
    bot = Player('o', field)
elif choice == 2:
    player = Player('o', field)
    bot = Player('x', field)
    bot.botMove()
    field.printField()
else: print('Выбора под номером {} выполнить нельзя'.format(action))

while True:
    print('Введите номер строки и столбца для хода:')
    row = int(input('Строка: '))
    col = int(input('Столбец: '))
    if row < 4 and col < 4:
        try:
            player.move(row, col)
            if player.is_winner():
                print('Вы выиграли!')
                break
            bot.botMove()
            if bot.is_winner():
                print('Вы проиграли.')
                break
        except IndexError:
            print('Это место уже занято!')
        except BaseException:
            print('Ничья.')
            break
    field.printField()

field.printField()