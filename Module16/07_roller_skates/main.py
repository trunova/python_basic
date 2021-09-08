listSkates = []
listPeople = []
skates = int(input('Кол-во коньков: '))
for i in range(skates):
    print('Размер', i+1,'пары:', end=' ')
    listSkates.append(int(input()))
people = int(input('Кол-во людей: '))
for i in range(people):
    print('Размер ноги', i+1,'человека:', end=' ')
    listPeople.append(int(input()))
n = 0
for j in range(people):
    for i in range(skates):
        if listSkates[i] == listPeople[j]:
            n += 1
            listSkates.remove(listSkates[i])
            break
    else:
        for i in range(skates):
            if listSkates[i] > listPeople[j]:
                n += 1
                listSkates.remove(listSkates[i])
                break
print('Наибольшее кол-во людей, которые могут взять ролики:', n)
