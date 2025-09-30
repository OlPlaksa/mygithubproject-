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

def multiply_numbers(num1: int, num2: int) -> int:
    """
        Повертає добуток дох чисел
    """
    return num1 * num2

def divide_numbers(num1: int, num2: int) -> float:
    try:
        return num1 / num2
    except ZeroDivisionError:
        return float('inf')


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

    # Перевірка функції множення
    multiply_result = multiply_numbers(5, 6)
    print(f"Результат множення 5 * 6: {multiply_result}")

    # Перевірка функції ділення з обробкою винятків
    devivision_result = divide_numbers(40, 4)
    devivision_error = divide_numbers(40, 0)
    print(f"Результат ділення 40 / 4: {devivision_result}")
    print(f"Результат ділення 40 / 0: {devivision_error}")

    print("--- Калькулятор завершив роботу ---")


if __name__ == "__main__":
    run_project()
