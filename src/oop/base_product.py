"""
Базовый абстрактный класс для продуктов.
"""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный класс для всех продуктов.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Абстрактный конструктор продукта."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения продуктов."""
        pass
