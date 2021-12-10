from typing import Callable, Any
import functools

def counter(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped_func(name, age=None):
        wrapped_func.count += 1
        result = func(name, age)
        print('Функция {} была вызвана {} раз(а)'.format(func.__name__, wrapped_func.count))
        return result

    wrapped_func.count = 0
    return wrapped_func

@counter
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
