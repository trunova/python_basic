
with open('registrations.txt', 'r', encoding='utf-8') as registrations_file, \
        open('registrations_bad.txt', 'w', encoding='utf-8') as reg_bad_file, \
        open('registrations_good.txt', 'w', encoding='utf-8') as reg_good_file:
    for i_line in registrations_file:
        lst = i_line.split()
        try:
            if len(lst) < 3:
                raise IndexError('НЕ присутствуют все три поля')
            elif not (lst[0].isalpha()):
                raise NameError('Поле имени содержит НЕ только буквы')
            elif not ('@' in lst[1] and '.' in lst[1]):
                raise SyntaxError('Поле емейл НЕ содержит @ и .(точку)')
            elif not(int(lst[2]) >= 10 and int(lst[2]) <= 99):
                raise ValueError('Поле возраст НЕ является числом от 10 до 99')
        except IndexError:
            for i_l in lst:
                reg_bad_file.write(i_l + ' ')
            reg_bad_file.write('IndexError\n')
        except NameError:
            for i_l in lst:
                reg_bad_file.write(i_l + ' ')
            reg_bad_file.write('NameError\n')
        except SyntaxError:
            for i_l in lst:
                reg_bad_file.write(i_l + ' ')
            reg_bad_file.write('SyntaxError\n')
        except ValueError:
            for i_l in lst:
                reg_bad_file.write(i_l + ' ')
            reg_bad_file.write('ValueError\n')
        else:
            for i_l in lst:
                reg_good_file.write(i_l + ' ')
            reg_good_file.write('\n')
