import functions as math_func
import operations as ops

def main():
    print("--- Модульний калькулятор ---")
    print("Напишіть 'exit' для виходу.")

    while True:
        n1 = ops.get_num("\nЧисло 1: ")
        if n1 == 'exit': break

        op = ops.get_operator()
        if op == 'exit': break

        n2 = ops.get_num("Число 2: ")
        if n2 == 'exit': break

        result = None
        if op == '+':
            result = math_func.add(n1, n2)
        elif op == '-':
            result = math_func.sub(n1, n2)
        elif op == '*':
            result = math_func.mult(n1, n2)
        elif op == '/':
            result = math_func.div(n1, n2)

        print(f"Результат: {result}")

if __name__ == "__main__":
    main()