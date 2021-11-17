from MyStack import MyStack
from copy import copy, deepcopy

class TaskManager(MyStack):
    """
    Класс, реализующий Менеджер задач

    __listKeys: список приоритетов элементов стека
    __dct: словарь "приоритет: задача"
    """
    __listKeys = list()
    __dct = dict()

    def newTask(self, task, priority):
        """
        Добавление новой задачи

        :param task: задача
        :type task: str
        :param priority: приоритет
        :type priority: int
        """
        self.add((task, priority))
        if not priority in self.__listKeys:
            self.__listKeys.append(priority)

    def __str__(self):
        """
        Вывод задач

        :return: s
        """
        self.fillDict()
        s = ''
        for p, f in self.__dct.items():
            s += '{p} {f}; '.format(p=str(p), f=f)
        return s[:len(s)-2]

    def fillDict(self):
        """
        Заполнение словаря правильной последовательностью задач
        :return:
        """
        self.__dct.clear()
        stack = deepcopy(self)
        stack.__listKeys.sort()
        for i_key in stack.__listKeys:
            stack.__dct[i_key] = list()
        for i in range(stack.get_count()):
            task, priority = stack.delete()
            stack.__dct[priority].append(task)