# main.py
# Це головний файл вашого Python-проєкту.
# Виведемо просте повідомлення, щоб перевірити, чи працює інтерпретатор.

def add_numbers(a: float, b: float) -> float:
    """
    Повертає суму двох чисел.

    Аргументи:
    a (float): Перше число.
    b (float): Друге число.

    Повертає:
    float: Сума a та b.
    """
    return a + b

def run_project():
    """
    Основна функція для запуску логіки проєкту.
    """
    print("Привіт, GitHub!")
    print("Проєкт mygithubproject успішно запущено.")

    # Демонстрація нової функції додавання
    num1 = 5
    num2 = 3.5
    result = add_numbers(num1, num2)

    print(f"\nРезультат додавання {num1} + {num2} = {result}")

if __name__ == "__main__":
    run_project()
