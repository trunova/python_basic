order_dict = dict()
for i in range(int(input('Введите кол-во заказов: '))):
    listS = input('{0} заказ: '.format(i+1)).split(' ')
    if listS[0] in order_dict:
        if listS[1] in order_dict[listS[0]]:
            order_dict[listS[0]][listS[1]] += int(listS[2])
        else: order_dict[listS[0]][listS[1]] = int(listS[2])
    else:
        order_dict[listS[0]] = {listS[1]:int(listS[2])}
for i in sorted(order_dict):
    print('{0}:'.format(i))
    for j in sorted(order_dict[i]):
        print('       {0}: {1}'.format(j, order_dict[i][j]))

# 1 заказ: Иванов Пепперони 1 Петров Де-Люкс 2 Иванов Мясная 3 Иванов Мексиканская 2 Иванов Пепперони 2 Петров Интересная 5
