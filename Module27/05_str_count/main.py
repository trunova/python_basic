from typing import Callable, Any
import functools

def counter(func: Callable) -> Any:

    @functools.wraps(func)
    def wrapped_func(name, age=None):
        result = func(name, age)
        if func.__name__ in dict_func.keys():
            dict_func[func.__name__] += 1
        else: dict_func[func.__name__] = 1
        print(dict_func.get(func.__name__))
        return result
    return wrapped_func

@counter
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

dict_func = dict()
greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)