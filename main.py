"""
Демонстрация работы абстрактного класса BaseProduct и миксина LogMixin.
"""

from src.oop.product import Product, Smartphone, LawnGrass


def main():
    """Демонстрация создания продуктов с логированием."""
    print("=== ДЕМОНСТРАЦИЯ МНОЖЕСТВЕННОГО НАСЛЕДОВАНИЯ ===\n")

    # Создание обычного продукта (срабатывает LogMixin)
    print("1. Создание Product:")
    product = Product("Ноутбук", "Игровой ноутбук", 120000.0, 5)
    print(f"   Создан: {product}\n")

    # Создание смартфона
    print("2. Создание Smartphone:")
    phone = Smartphone(
        "iPhone 15", "Смартфон Apple", 99999.0, 3,
        efficiency=9.8, model="15 Pro", memory=256, color="Black"
    )
    print(f"   Создан: {phone.name}, {phone.model}, {phone.memory}GB\n")

    # Создание газонной травы
    print("3. Создание LawnGrass:")
    grass = LawnGrass(
        "Green Lawn", "Газонная трава", 499.0, 10,
        country="Россия", germination_period=14, color="Зеленый"
    )
    print(f"   Создан: {grass.name}, {grass.country}, {grass.germination_period} дней\n")

    # Демонстрация сложения
    print("4. Сложение продуктов:")
    p1 = Product("A", "", 100.0, 2)
    p2 = Product("B", "", 200.0, 1)
    print(f"   100*2 + 200*1 = {p1 + p2}\n")

    print("=== ГОТОВО ===")


if __name__ == "__main__":
    main()
