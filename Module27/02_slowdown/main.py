import time
from typing import Callable, Any
def deceleration(func: Callable) -> Any:
    def wrapped_func(*args, **kwargs):
        print('Подождём несколько секунд перед выполнением декорируемой функции.')
        time.sleep(3)
        result = func(*args, **kwargs)
        return result
    return wrapped_func

@deceleration
def test():
    print('<Тут что-то происходит...>')

test()