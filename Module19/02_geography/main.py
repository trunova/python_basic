country_dict = dict()
for i in range(int(input('Кол-во стран: '))):
    print('{0} страна:'.format(i+1), end=' ')
    strList = input().split(' ')
    country_dict[strList[0]] = strList[1:]
print(country_dict)
for i in  range(3):
    print('{0} город:'.format(i+1), end=' ')
    city = input()
    for j in country_dict:
        if city in country_dict.get(j):
            print('Город {0} расположен в стране {1}'.format(
                city,
                j
            ))
            break
    else: print('По городу {0} данных нет.'.format(city))
