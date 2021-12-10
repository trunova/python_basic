from typing import Callable, Any
import functools

def debug(func: Callable) -> Any:

    @functools.wraps(func)
    def wrapped_func(name, age=None):
        result = func(name, age)

        if age == None:
            s = '\nВызывается {func_name}("{name}")\n'
        else:
            s = '\nВызывается {func_name}("{name}, age={age}")\n'
        s += '\'{func_name}\' вернула значение \'{result}\''
        print(s.format(func_name=func.__name__, name=name, age=age, result=result))
        print(result)
    return wrapped_func

@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)