import functools
from collections.abc import Callable


def decorator_with_args_for_any_decorator(decorated_decorator: Callable) -> Callable:
    def decorator(*args, **kwargs) -> Callable:
        def wrapper(func: Callable) -> Callable:
            return decorated_decorator(func, *args, **kwargs)

        return wrapper

    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*args1, **kwargs1) -> Callable:
        print('Переданные арги и кварги в декоратор: {a} {kw}'.format(a=args, kw=kwargs))
        return func(*args1, **kwargs1)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
