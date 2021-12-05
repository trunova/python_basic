from typing import Any, Optional

class ListNode:
    """
    Базовый класс, описывающий элемент односвязного списка

    Args:
        data: значение элемента
        next: ссылка на следующий элемент
    """

    def __init__(self, data: Optional[Any] = None, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """
    Базовый класс, описывающий односвязный список

    """

    def __init__(self):
        self.__head = ListNode()
        self.__tail = ListNode()
        self.__size = 0

    def __iter__(self):
        self.listIterator = ListNode(next=self.__head)
        self.count = 0
        return self

    def __next__(self):
        if self.count == self.__size:
            raise StopIteration
        self.listIterator = self.listIterator.next
        self.count += 1
        return self.listIterator.data

    def getSize(self) -> int:
        return self.__size

    def append(self, elem: Any):
        """ Добавление элеметна в конец списка """

        listNode = ListNode(data=elem)
        if self.__size == 0:
            self.__head = listNode
        else:
            self.__tail.next = listNode
        self.__tail = listNode
        self.__size += 1

    def get(self, index: int) -> ListNode:
        """
        Получение элемента по индексу

        :param index: int
        :return: result
        :rtype: ListNode
        :raise Exception: если index выходит за пределы длины списка
        """

        if index < 0 or index >= self.__size:
            raise Exception("Wrong index")

        result = self.__head
        for i in range(index):
            result = result.next
        return result

    def remove(self, index: int):
        """
        Удаление элемента по индексу

        :param index:
        :return: int
        :raise Exception: если index выходит за пределы длины списка
        """

        if index < 0 or index >= self.__size:
            raise Exception("Wrong index")

        if index == 0:
            self.__head = self.__head.next
            if head == None:
                self.__tail = null;
        else:
            prev = self.get(index - 1)
            prev.next = prev.next.next
            if prev.next == None:
                self.__tail = prev
        self.__size -= 1

    def __str__(self) -> str:
        v = self.__head
        line = '['
        for i in range(self.__size):
            line += '{} '.format(v.data)
            v = v.next
        return line[:len(line) - 1] + ']'