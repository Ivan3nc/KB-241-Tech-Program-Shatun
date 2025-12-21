def get_num(prompt):
    while True:
        val = input(prompt)
        if val == 'exit':
            return 'exit'
        try:
            return float(val.replace(',', '.'))
        except ValueError:
            print("Помилка: введіть число.")

def get_operator():
    valid = ['+', '-', '*', '/']
    while True:
        op = input("Дія (+, -, *, /): ")
        if op == 'exit':
            return 'exit'
        if op in valid:
            return op
        print("Невідома операція.")