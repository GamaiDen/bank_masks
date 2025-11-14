import functools
from typing import Callable, Any, Optional, TypeVar, cast

# Тип для функций
F = TypeVar('F', bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования вызовов функций.

    Логирует успешные выполнения функций и ошибки. Может выводить логи
    в консоль или записывать в файл.

    Args:
        filename (Optional[str]): Имя файла для записи логов.
                                Если None - логи выводятся в консоль.

    Returns:
        Callable: Декорированную функцию с добавленным логированием.

    Examples:
        >>> @log()
        ... def add(a, b):
        ...     return a + b
        >>> add(1, 2)
        add ok

        >>> @log(filename="app.log")
        ... def divide(a, b):
        ...     return a / b
        >>> divide(1, 0)
        divide error: ZeroDivisionError. Inputs: (1, 0), {}

    Notes:
        - При успешном выполнении логируется: "имя_функции ok"
        - При ошибке логируется: "имя_функции error: тип_ошибки. Inputs: args, kwargs"
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
