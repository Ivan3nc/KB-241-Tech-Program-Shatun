class Calculator:
    def plus(self, a, b):
        return a + b
    def minus(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            return "Err: ділення на 0"
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print("Калькулятор (напишіть 'exit' щоб вийти)")

    while True:
        n1 = input("\nЧисло 1: ")
        if n1 == 'exit': break
        op = input("Дія (+, -, *, /): ")
        if op == 'exit': break
        n2 = input("Число 2: ")
        if n2 == 'exit': break
        try:
            num1 = float(n1)
            num2 = float(n2)
            
            res = None
            if op == '+':
                res = calc.plus(num1, num2)
            elif op == '-':
                res = calc.minus(num1, num2)
            elif op == '*':
                res = calc.mult(num1, num2)
            elif op == '/':
                res = calc.div(num1, num2)
            else:
                print("Нема такої операції")
                continue
            print("Результат:", res)

        except ValueError:
            print("Треба вводити цифри")