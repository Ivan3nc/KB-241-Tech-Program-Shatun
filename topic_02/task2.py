def plus(x, y): return x + y
def minus(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y

n1 = float(input("Число 1: "))
op = input("Дія (+, -, *, /): ")
n2 = float(input("Число 2: "))

if op == '+':
    print(plus(n1, n2))
elif op == '-':
    print(minus(n1, n2))
elif op == '*':
    print(mult(n1, n2))
elif op == '/':
    if n2 == 0:
        print("На нуль ділити не можна")
    else:
        print(div(n1, n2))
else:
    print("Невідома дія")