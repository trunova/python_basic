import functools
from collections.abc import Callable

app = {}


def callback(route: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        app[route] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped

    return wrapper


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
