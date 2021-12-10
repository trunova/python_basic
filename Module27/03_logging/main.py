from typing import Callable, Any
import functools
from datetime import datetime

def logging(func: Callable) -> Any:
    """ Декоратор, отвечающий за логирование декорируемой функции """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('Название функции = {name}\n'
              'Документация:\n{doc}'.format(name=func.__name__, doc=func.__doc__))
        with open('function_errors.log', 'a', encoding='utf-8') as function_errors:
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as exception:
                function_errors.write('Название функции: {name}\t'
                                      'Название ошибки: {nameEx}\t'
                                      'Текущая дата: {date}\n'.format(
                    name=func.__name__,
                    nameEx=type(exception).__name__,
                    date=datetime.now()))
            return result
    return wrapped_func


@logging
def division(dividend: float, divider: float) -> float:
    """ Деление """
    return dividend/divider

@logging
def mul(factor1: float, factor2: float):
    """ Умножение """
    lst = [2, 3, 4]
    tmp = lst[8]
    return factor1 * factor2

print(division(10, 0))
print(mul(10, 2))