def sort_col(i):
    return i[2]

first_tour_file = open('first_tour.txt', 'r')
second_tour_file = open('second_tour.txt', 'a')

minScore = int(first_tour_file.readline())
line_list = list()
numberOfPlayersInTheSecondTour = 0

for i_line in first_tour_file:
    lst = i_line.split()
    if int(lst[2]) > minScore:
        numberOfPlayersInTheSecondTour += 1
        name = lst[1][:1] + '.'
        lst[1] = lst[0]
        lst[0] = name
        line_list.append(lst)

line_list.sort(key=sort_col, reverse= -1)

second_tour_file.write(str(numberOfPlayersInTheSecondTour) + '\n')
for i in range(1, numberOfPlayersInTheSecondTour + 1):
    second_tour_file.write('{0}) '.format(i))
    for j in range(3):
        second_tour_file.write(line_list[i - 1][j] + ' ')
    second_tour_file.write('\n')

first_tour_file.close()
second_tour_file.close()