import sys

def sort(dictt):
    sorted_values = sorted(dictt.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in dictt.keys():
            if dictt[k] == i:
                sorted_dict[k] = dictt.pop(k)
                break
    return sorted_dict

def minDictValues(d):
    minInd = ''
    min = sys.maxsize
    for i_key, i_value in d.items():
        if int(i_value) < min:
            min = int(i_value)
            minInd = i_key
    return minInd

n = int(input('Сколько записей вносится в протокол? '))
lst = list()
winners = {}

for i in range(n):
    ls = input('{0} запись: '.format(i+1)).split()
    if i >= 0 and i < 3:
        winners[ls[1]] = int(ls[0])
    else:
        if ls[1] not in winners.keys():
            if int(ls[0]) > int(winners.get(minDictValues(winners))):
                winners.pop(minDictValues(winners))
                winners[ls[1]] = int(ls[0])
        elif int(ls[0]) > int(winners.get(ls[1])):
            winners[ls[1]] = int(ls[0])

print('Итоги соревнований:')
print(winners)
j = 1
for i_winner, i in sort(winners).items():
    print('{0} место. {1} ({2})'.format(
        j,
        i_winner,
        i
    ))
    j += 1