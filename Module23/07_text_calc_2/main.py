
summ = 0
def transformationOperation(i_line, summ):
    lst = i_line.split()
    r = 0
    try:
        if len(lst) < 3:
            raise IndexError('Не хватает какого либо из 3х полей для выполнения операции')
        elif not (lst[1] == '+' or lst[1] == '-' or lst[1] == '*' or lst[1] == '%' or lst[1] == '/' or lst[1] == '//'):
            raise SyntaxError('Некорректная операция')
        elif not (lst[0].isdigit() and lst[2].isdigit()):
            raise ValueError('Операнды не являются числами')
        elif (lst[1] == '%' or lst[1] == '/' or lst[1] == '//') and lst[2] == '0':
            raise ZeroDivisionError('division by zero')
    except (IndexError, SyntaxError, ValueError, ZeroDivisionError):
        print('Обнаружена ошибка в строке:', end=' ')
        for i in lst:
            print(i, end=' ')
        answ = input('Хотите исправить? ').lower()
        if answ == 'да':
            correctedLine = input('Введите исправленную строку: ')
            r = transformationOperation(correctedLine, summ)
    else: r = eval(i_line)
    return r


with open('calc.txt', 'r') as calc_file:
    for i_line in calc_file:
        summ += transformationOperation(i_line, summ)
    print('Сумма результатов:', summ)