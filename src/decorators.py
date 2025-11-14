import functools
from typing import Any, Callable, Optional, TypeVar, cast

# Тип для функций
F = TypeVar('F', bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Имя файла для логирования. Если None - вывод в консоль.

    Returns:
        Декорированную функцию с логированием.
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                # Успешное выполнение
                log_message = f"{func.__name__} ok\n"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')

                return result

            except Exception as e:
                # Ошибка выполнения
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(error_message)
                else:
                    print(error_message, end='')

                raise e

        return cast(F, wrapper)
    return decorator
