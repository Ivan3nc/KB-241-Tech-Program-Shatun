import sys
from rpn_modules import Converter, Calculator

def main():
    print("--- Lab 04: Зворотний польський запис ---")
    print("Приклад: 3 + 4 * 2 / ( 1 - 5 ) ^ 2") 

    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
    else:
        expression = input("Введіть вираз: ")

    conv = Converter()
    calc = Calculator()

    rpn_list = conv.to_rpn(expression)
    print(f"ЗПЗ: {' '.join(rpn_list)}")

    result = calc.calculate(rpn_list)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()