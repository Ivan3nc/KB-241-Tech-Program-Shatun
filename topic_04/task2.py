def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: на нуль ділити не можна!"

if __name__ == "__main__":
    print("--- Тест ділення ---")

    print("10 / 2 =", divide(10, 2))

    print("5 / 0 =", divide(5, 0))