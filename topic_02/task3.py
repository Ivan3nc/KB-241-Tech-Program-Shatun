def plus(x, y): return x + y
def minus(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y

n1 = float(input("Число 1: "))
op = input("Дія (+, -, *, /): ")
n2 = float(input("Число 2: "))

match op:
    case "+":
        print(plus(n1, n2))
    case "-":
        print(minus(n1, n2))
    case "*":
        print(mult(n1, n2))
    case "/":
        if n2 == 0:
            print("Помилка ділення на 0")
        else:
            print(div(n1, n2))
    case _:
        print("Невідома дія")