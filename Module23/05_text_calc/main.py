
summ = 0

with open('calc.txt', 'r') as calc_file:
    for i_line in calc_file:
        lst = i_line.split()
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
            print('Невозможно выполнить операцию: ', end= ' ')
            for i in lst:
                print(i, end=' ')
            print('')
        else: summ += eval(i_line)
    print('Сумма результатов:', summ)