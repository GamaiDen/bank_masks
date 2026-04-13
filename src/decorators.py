"""
Модуль с декораторами для логирования.
"""
from functools import wraps
from typing import Any, Callable


def log(filename: str = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Аргументы:
        filename (str, optional): Путь к файлу для записи логов.
                                 Если не указан, логи выводятся в консоль.

    Возвращает:
        Callable: Декорированная функция.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_msg = f"{type(e).__name__}"
                log_message = (
                    f"{func.__name__} error: {error_msg}. "
                    f"Inputs: {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message + "\n")
                else:
                    print(log_message)
                raise e

        return wrapper

    return decorator
