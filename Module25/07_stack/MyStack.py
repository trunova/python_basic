from copy import copy, deepcopy

class MyStack():
    """
    Класс, реализующий Стек

    __count: количество объектов в стеке
    __lst: список элементов стека

    Args:
        lst (list): передаётся список элементов
    """
    def __init__(self, lst = None):
        if lst != None:
            self.__lst = lst
            self.__count = len(lst)
        else:
            self.__lst = []
            self.__count = 0

    def __deepcopy__(self, memodict={}):
        cls = self.__class__
        result = cls.__new__(cls)
        memodict[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memodict))
        return result

    def get_count(self):
        return self.__count

    def get_lst(self):
        return self.__lst

    def add(self, obj):
        """
        Добавление элемента

        :param obj: объект, который нужно добавить в стек
        """
        self.__lst.append(obj)
        self.__count += 1

    def delete(self):
        """
        Удаление элемента

        :return: последний элемент
        """
        self.__count -= 1
        return self.__lst.pop(self.__count - 1)
