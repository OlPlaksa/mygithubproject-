"""
Модуль для юніт-тестування логіки калькулятора, визначеної у main.py.
"""
import unittest
# Імпортуємо всі функції з головного файлу, які ми хочемо протестувати
from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


class TestCalculatorFunctions(unittest.TestCase):
    """
    Клас, що містить тестові методи для перевірки арифметичних операцій.
    """

    def test_add_numbers(self):
        """Перевіряє коректність функції додавання."""
        # Успішне додавання
        self.assertEqual(add_numbers(10, 5), 15)
        # Додавання з від'ємними числами
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-10, -5), -15)

    def test_subtract_numbers(self):
        """Перевіряє коректність функції віднімання."""
        # Успішне віднімання
        self.assertEqual(subtract_numbers(10, 5), 5)
        # Віднімання, що дає від'ємний результат
        self.assertEqual(subtract_numbers(5, 10), -5)
        # Віднімання від'ємних чисел
        self.assertEqual(subtract_numbers(-10, -5), -5)

    def test_multiply_numbers(self):
        """Перевіряє коректність функції множення."""
        # Стандартне множення
        self.assertEqual(multiply_numbers(10, 5), 50)
        # Множення на нуль
        self.assertEqual(multiply_numbers(100, 0), 0)
        # Множення на від'ємне число
        self.assertEqual(multiply_numbers(-5, 5), -25)

    def test_divide_numbers(self):
        """Перевіряє коректність функції ділення, включаючи ділення на нуль."""
        # Успішне ділення, що дає ціле число
        self.assertEqual(divide_numbers(10, 2), 5.0)
        # Успішне ділення, що дає число з плаваючою точкою
        self.assertEqual(divide_numbers(10, 4), 2.5)

        # Перевірка обробки ділення на нуль
        # У Python float('inf') представляє нескінченність
        self.assertEqual(divide_numbers(10, 0), float('inf'))

        # Перевірка ділення з від'ємними числами
        self.assertEqual(divide_numbers(-10, 2), -5.0)


# Цей блок дозволяє запускати тести, як звичайний Python-файл
if __name__ == '__main__':
    unittest.main()
