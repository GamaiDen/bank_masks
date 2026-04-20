# Bank Masks Project

Проект для маскировки банковских карт и счетов, а также обработки финансовых операций.

## Функциональность

- Маскировка номеров банковских карт в формате XXXX XX** **** XXXX
- Маскировка номеров счетов в формате **XXXX  
- Фильтрация операций по статусу
- Сортировка операций по дате
- Преобразование дат в читаемый формат

## Добавление модуля generators

### Функциональность:
- `filter_by_currency()` - фильтрация транзакций по валюте (итератор)
- `transaction_descriptions()` - генератор описаний транзакций  
- `card_number_generator()` - генератор номеров банковских карт

### Технические детали:
- Все функции используют генераторы (yield)
- 10/10 тестов проходят успешно
- 100% покрытие кода генераторов
- Использованы pytest фикстуры и параметризация
- Интегрировано в основной проект bank_masks

### Результаты тестов:


## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/GamaiDen/bank_masks.git
cd bank_masks

## Модуль Generators

Модуль содержит инструменты для работы с генераторами транзакций.

### Функции

#### 
Фильтрует транзакции по валюте и возвращает итератор.

####   
Генератор описаний транзакций.

#### 
Генератор номеров банковских карт.

### Тестирование
- 10/10 тестов проходят успешно
- 100% покрытие кода
- HTML отчет покрытия: 


## Модуль Generators

Модуль содержит инструменты для работы с генераторами транзакций.

### Функции

#### filter_by_currency(transactions, currency_code)
Фильтрует транзакции по валюте и возвращает итератор.

#### transaction_descriptions(transactions)
Генератор описаний транзакций.

#### card_number_generator(start, stop)
Генератор номеров банковских карт.

### Тестирование
- 10/10 тестов проходят успешно
- 100% покрытие кода
- HTML отчет покрытия: htmlcov/index.html

## 📊 Работа с CSV и Excel файлами

### Функции

#### `read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]`
Читает транзакции из CSV файла.

**Пример:**
```python
from src.file_reader import read_transactions_from_csv
transactions = read_transactions_from_csv("data/transactions.csv")


## 📊 Работа с CSV и Excel файлами

### Функции

#### `read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]`
Читает транзакции из CSV файла.

**Пример:**
```python
from src.file_reader import read_transactions_from_csv
transactions = read_transactions_from_csv("data/transactions.csv")
```

#### `read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]`
Читает транзакции из Excel файла (.xlsx).

**Пример:**
```python
from src.file_reader import read_transactions_from_excel
transactions = read_transactions_from_excel("data/transactions_excel.xlsx")
```

### Требования
- `pandas`
- `openpyxl`
<<<<<<< HEAD
=======

## ООП: Наследование (пакет src/oop)

### Классы-наследники Product

**Smartphone** — дополнительные атрибуты:
- `efficiency` — производительность
- `model` — модель
- `memory` — объем встроенной памяти
- `color` — цвет

**LawnGrass** — дополнительные атрибуты:
- `country` — страна-производитель
- `germination_period` — срок прорастания (дней)
- `color` — цвет

### Ограничения
- Сложение (`__add__`) разрешено только для объектов одного класса (TypeError при разных)
- Метод `add_product()` принимает только объекты Product или его наследников

### Тесты
```bash
poetry run pytest tests/oop_test_*.py -v

## Домашняя работа: Наследование (Smartphone и LawnGrass)

### Реализованные классы

**1. Smartphone (наследник Product)**
- Дополнительные атрибуты: `efficiency`, `model`, `memory`, `color`
- Переопределённый `__add__`: разрешает складывать только с объектами `Smartphone`

**2. LawnGrass (наследник Product)**
- Дополнительные атрибуты: `country`, `germination_period`, `color`
- Переопределённый `__add__`: разрешает складывать только с объектами `LawnGrass`

**3. Усиленная защита в Category**
- Метод `add_product()` проверяет, что добавляемый объект является наследником `Product` (`issubclass`)

### Тестирование
- Всего тестов: 22
- Покрытие кода: 98%
- Отчёт о покрытии: `htmlcov/index.html`
>>>>>>> 461db99 (docs: update README with inheritance homework description)
