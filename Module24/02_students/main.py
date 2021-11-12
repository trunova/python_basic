
class Student:
    def __init__(self, surname_name, group_number, progress):
        self.surname_name = surname_name
        self.group_number = group_number
        self.progress = progress

    def averageScore(self):
        s = 0
        for i_score in self.progress:
            s += i_score
        try:
            return s / len(self.progress)
        except ZeroDivisionError:
            print('Ошибка: у студента {} {} группы нет оценок'.format(self.surname_name,self.group_number))
            return 0

    def printStudent(self):
        print('Студент: {}, {} группа, успеваемость: {}'.format(self.surname_name,
                                                                self.group_number,
                                                                self.progress),
              end=';\n')



listStudent = [Student('Дмитрий Кузнецов', 1, [3, 4, 3, 5, 5]),
                   Student('Данил Иванов', 4, [5, 5, 5, 4, 5]),
                   Student('Вероника Михайлова', 4, [3, 4, 3, 3, 3]),
                   Student('Екатерина Семёнова', 1, [3, 4, 3, 4, 2]),
                   Student('Вадим Новиков', 2, [4, 4, 4, 4, 5]),
                   Student('Анна Попова', 1, [4, 3, 3, 3, 5]),
                   Student('Оксана Лебедева', 1, [3, 4, 3, 5, 5]),
                   Student('Юлия Волкова', 2, [3, 4, 3, 5, 5]),
                   Student('Артём Митрофанов', 1, [4, 5, 5, 5, 5]),
                   Student('Кирилл Васильев', 3, [2, 4, 5, 5, 5])]

listStudent.sort(key=lambda student: student.averageScore())
for i_student in listStudent:
    i_student.printStudent()