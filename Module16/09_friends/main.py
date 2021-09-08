friends = int(input('Кол-во друзей: '))
promissoryNotes = int(input('Долговых расписок: '))
listFr = [0] * friends
for i in range(promissoryNotes):
    print(i+1, 'расписка')
    toWhom = int(input('Кому: '))
    fromWhom = int(input('От кого: '))
    how = int(input('Сколько: '))
    listFr[toWhom - 1] -= how
    listFr[fromWhom - 1] += how
    print()
print('Баланс друзей:')
for i in range(friends):
    print(i+1,end='')
    print(':', listFr[i])