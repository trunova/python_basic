def isInt(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

while True:
    ip = input('Введите IP: ')
    ipList = ip.split('.')
    if len(ipList) != 4:
        print('Адрес - это четыре числа, разделенные точками')
    else:
        for i in range(4):
            if not isInt(ipList[i]):
                print(ipList[i], '- не целое число')
                break
            elif int(ipList[i]) < 0:
                print(ipList[i], 'меньше 0')
                break
            elif int(ipList[i]) > 255:
                print(ipList[i], 'превышает 255')
                break
        else:
            print('IP-адрес корректен')
            break