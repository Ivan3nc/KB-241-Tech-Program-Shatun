def get_num(prompt):
    while True:
        try:
            value = input(prompt)
            if value == 'exit':
                return 'exit'
            return float(value)
        except ValueError:
            print("Помилка: введіть число.")

def get_operator():
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Дія (+, -, *, /): ")
        if op == 'exit':
            return 'exit'
        if op in valid_ops:
            return op
        print("Невідома операція.")