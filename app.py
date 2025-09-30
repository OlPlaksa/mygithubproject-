# Функція для привітання
def greet(name):
    return f"Hello, {name}! This is a Python script run from PyCharm."

# Викликаємо функцію
if __name__ == "__main__":
    message = greet("PyCharm User")
    print(message)