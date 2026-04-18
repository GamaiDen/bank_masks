"""
Миксины для классов продуктов.
"""


class LogMixin:
    """
    Миксин для логирования создания объекта.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Логирует создание объекта и вызывает родительский __init__."""
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}")
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        """Возвращает строку с информацией об объекте."""
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"
