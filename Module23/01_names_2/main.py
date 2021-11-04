sum_letter = 0
count_line = 0
with open('people.txt', 'r') as people_file:
    for i_line in people_file:
        count_line += 1
        length = len(i_line)
        if i_line.endswith('\n'):
            length -= 1
        try:
            if length < 3:
                raise BaseException()
        except BaseException:
            print("Длина {0} строки меньше 3 символов".format(count_line))
        sum_letter += length
print('Кол-во символов - {}'.format(sum_letter))