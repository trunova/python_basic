import functools
from collections.abc import Callable


def check_permission(position: str) -> Callable:
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if position == 'admin':
                    return func(*args, **kwargs)
                else:
                    raise PermissionError()
            except PermissionError as ex:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(func.__name__))

        return wrapped

    return check


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
