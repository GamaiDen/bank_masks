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

## Домашняя работа: Исключения

### Реализовано

**1. Валидация количества в Product**
- При создании продукта с `quantity <= 0` выбрасывается `ValueError` с сообщением:
  `"Товар с нулевым количеством не может быть добавлен"`

**2. Метод `average_price()` в Category**
- Рассчитывает среднюю цену товаров в категории
- Если категория пуста — возвращает `0.0` (обработка `ZeroDivisionError`)

### Тестирование
- Всего тестов OOP: 26
- Покрытие кода: 80%
