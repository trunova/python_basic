file_numbers = open('numbers.txt', 'r', encoding='utf-8')
summ = 0
for i_line in file_numbers:
    for i in i_line:
        if i != ' ' and i != '\n':
            summ += int(i)
file_numbers.close()
file_sum = open('answer.txt', 'w')
file_sum.write(str(summ))
file_sum.close()
