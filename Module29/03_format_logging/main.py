import functools
from collections.abc import Callable
from datetime import datetime
import time


def log_methods(format: str) -> Callable:
    decorator = time_method(format)

    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                setattr(cls, i_method, decorator(getattr(cls, i_method)))
        return cls
    return decorate


def time_method(format: str) -> Callable:
    def method(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            dt = ""
            for i in format:
                if i in alphabet:
                    dt += "%"
                dt += i
            print('- Запускается \'{name}\'. Дата и время запуска: {date}'.format(name=func.__name__,
                                                                                  date=datetime.utcnow().strftime(dt)))
            start = time.time()
            ret = func(*args, **kwargs)
            print('- Завершение \'{name}\', время работы = {time}s'.format(name=func.__name__,
                                                                           time=round(time.time() - start, 3)))
            return ret
        return wrapper
    return method


@log_methods("b d Y - H:M:S")
class A:

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()