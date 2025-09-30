"""
Головний файл проєкту, що містить логіку калькулятора.
"""


def add_numbers(num1: int, num2: int) -> int:
    """
    Повертає суму двох цілих чисел.

    Args:
        num1: Перше число.
        num2: Друге число.

    Returns:
        Сума чисел.
    """
    return num1 + num2


def subtract_numbers(num1: int, num2: int) -> int:
    """
    Повертає різницю двох цілих чисел.

    Args:
        num1: Число, від якого віднімаємо (зменшуване).
        num2: Число, яке віднімаємо (від'ємник).

    Returns:
        Різниця чисел.
    """
    return num1 - num2


def run_project():
    """
    Запускає логіку проєкту та виводить результати.
    """
    print("--- Запуск калькулятора ---")

    # Перевірка функції додавання (додана в Pull Request #1)
    sum_result = add_numbers(10, 5)
    print(f"Результат додавання 10 + 5: {sum_result}")

    # Перевірка функції віднімання (нова функціональність)
    subtraction_result = subtract_numbers(10, 5)
    print(f"Результат віднімання 10 - 5: {subtraction_result}")

    print("--- Калькулятор завершив роботу ---")


if __name__ == "__main__":
    run_project()
