"""
Демонстрация работы абстрактного класса и миксина.
"""

from src.oop.product import LawnGrass, Product, Smartphone
from src.oop.category import Category


def main():
    """Демонстрация создания продуктов и категорий."""
    print("=== ДЕМОНСТРАЦИЯ АБСТРАКТНОГО КЛАССА И МИКСИНА ===\n")

    # Создаем смартфон
    phone = Smartphone(
        name="iPhone 15",
        description="Смартфон Apple",
        price=99999.0,
        quantity=2,
        efficiency=9.8,
        model="15 Pro",
        memory=256,
        color="Black"
    )
    print(f"✅ Создан смартфон: {phone}")

    # Создаем газонную траву
    grass = LawnGrass(
        name="Green Grass",
        description="Трава для газона",
        price=499.0,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="Зеленый"
    )
    print(f"✅ Создана трава: {grass}")

    # Создаем обычный продукт
    product = Product(
        name="Чехол для iPhone",
        description="Силиконовый чехол",
        price=1990.0,
        quantity=5
    )
    print(f"✅ Создан продукт: {product}")

    # Создаем категорию
    cat = Category("Электроника", "Гаджеты", [phone, product])
    print(f"✅ Создана категория: {cat}")
    print(f"   Товаров в категории: {len(cat.get_products_list())}")

    print("\n=== ГОТОВО ===")


if __name__ == "__main__":
    main()
