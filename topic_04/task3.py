def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: на нуль ділити не можна!"

def get_data(prompt):
    while True:
        val = input(prompt)
        if val == 'exit':
            return 'exit'
        try:
            return float(val.replace(',', '.'))
        except ValueError:
            print("Це не число. Будь ласка, введіть цифри.")

if __name__ == "__main__":
    print("Калькулятор (напишіть 'exit' щоб вийти)")

    while True:
        n1 = get_data("\nЧисло 1: ")
        if n1 == 'exit': break

        op = input("Дія (+, -, *, /): ")
        if op == 'exit': break

        n2 = get_data("Число 2: ")
        if n2 == 'exit': break

        result = None

        if op == '+':
            result = add(n1, n2)
        elif op == '-':
            result = sub(n1, n2)
        elif op == '*':
            result = mult(n1, n2)
        elif op == '/':
            result = div(n1, n2) 
        else:
            print("Невідома операція.")
            continue

        print("Результат:", result)