from typing import Callable, Any


def how_are_you(func: Callable) -> Any:
    def wrapped_func(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


@how_are_you
def test2(n: int) -> int:
    return 2 * n


test()
print(test2(4))
