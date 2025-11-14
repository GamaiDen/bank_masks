import os
import tempfile
from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест логирования успеха в консоль."""

    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)

    captured = capsys.readouterr()
    assert result == 3
    assert "add ok" in captured.out


def test_log_to_console_error(capsys):
    """Тест логирования ошибки в консоль."""

    @log()
    def divide(a, b):
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out


def test_log_to_file_success():
    """Тест логирования успеха в файл."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_filename = f.name

    try:
        @log(filename=temp_filename)
        def multiply(a, b):
            return a * b

        result = multiply(3, 4)

        with open(temp_filename, 'r', encoding='utf-8') as f:
            content = f.read()

        assert result == 12
        assert "multiply ok" in content
    finally:
        os.unlink(temp_filename)


def test_log_to_file_error():
    """Тест логирования ошибки в файл."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_filename = f.name

    try:
        @log(filename=temp_filename)
        def failing_func():
            raise ValueError("Test error")

        try:
            failing_func()
        except ValueError:
            pass

        with open(temp_filename, 'r', encoding='utf-8') as f:
            content = f.read()

        assert "failing_func error: ValueError" in content
        assert "Inputs: ()" in content
    finally:
        os.unlink(temp_filename)


def test_function_arguments_preserved():
    """Тест сохранения аргументов функции."""

    @log()
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    result = greet("Alice", greeting="Hi")
    assert result == "Hi, Alice!"


def test_original_function_attributes_preserved():
    """Тест сохранения атрибутов оригинальной функции."""

    @log()
    def test_func():
        """Test function docstring."""
        pass

    assert test_func.__name__ == "test_func"
    assert "Test function docstring" in test_func.__doc__


def test_log_with_keyword_arguments(capsys):
    """Тест логирования с keyword arguments."""

    @log()
    def introduce(name, age):
        return f"{name} is {age} years old"

    result = introduce(name="Bob", age=25)
    captured = capsys.readouterr()

    assert result == "Bob is 25 years old"
    assert "introduce ok" in captured.out


def test_multiple_calls_to_same_function(capsys):
    """Тест множественных вызовов одной функции."""

    @log()
    def increment(x):
        return x + 1

    increment(1)
    increment(2)
    increment(3)

    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    assert len(lines) == 3
    assert all("increment ok" in line for line in lines)
