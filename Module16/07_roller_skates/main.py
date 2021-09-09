listSkates = []
listPeople = []
for i in range(int(input('Кол-во коньков: '))):
    print('Размер', i+1,'пары:', end=' ')
    listSkates.append(int(input()))
for i in range(int(input('Кол-во людей: '))):
    print('Размер ноги', i+1,'человека:', end=' ')
    listPeople.append(int(input()))
n = 0
for j in range(len(listPeople)):
    for i in range(len(listSkates)):
        if listSkates[i] == listPeople[j]:
            n += 1
            listSkates.remove(listSkates[i])
            break
    else:
        for i in range(len(listSkates)):
            if listSkates[i] > listPeople[j]:
                n += 1
                listSkates.remove(listSkates[i])
                break
print('Наибольшее кол-во людей, которые могут взять ролики:', n)
