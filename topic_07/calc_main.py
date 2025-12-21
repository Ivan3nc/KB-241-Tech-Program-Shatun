from calc_logic import Calculator

def get_num(prompt):
    while True:
        val = input(prompt)
        if val.lower() == 'exit': return 'exit'
        try:
            return float(val.replace(',', '.'))
        except ValueError:
            print("Будь ласка, введіть число.")

def main():
    my_calc = Calculator()

    print("--- ООП Калькулятор ---")
    print("Напишіть 'exit' для виходу.")

    while True:
        n1 = get_num("\nЧисло 1: ")
        if n1 == 'exit': break

        op = input("Дія (+, -, *, /): ")
        if op == 'exit': break

        n2 = get_num("Число 2: ")
        if n2 == 'exit': break

        result = None

        if op == '+':
            result = my_calc.add(n1, n2)
        elif op == '-':
            result = my_calc.sub(n1, n2)
        elif op == '*':
            result = my_calc.mult(n1, n2)
        elif op == '/':
            result = my_calc.div(n1, n2)
        else:
            print("Невідома операція.")
            continue

        print(f"Результат: {result}")

if __name__ == "__main__":
    main()