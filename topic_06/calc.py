import functions as f
import operations as o
import datetime 

def write_log(n1, op, n2, res):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"[{now}] {n1} {op} {n2} = {res}\n"

    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(log_line)

def main():
    print("--- Калькулятор (історія пишеться в history.txt) ---")
    
    while True:
        n1 = o.get_num("\nЧисло 1: ")
        if n1 == 'exit': break

        op = o.get_operator()
        if op == 'exit': break

        n2 = o.get_num("Число 2: ")
        if n2 == 'exit': break

        res = None
        if op == '+': res = f.add(n1, n2)
        elif op == '-': res = f.sub(n1, n2)
        elif op == '*': res = f.mult(n1, n2)
        elif op == '/': res = f.div(n1, n2)

        print(f"Результат: {res}")

        write_log(n1, op, n2, res)
        print("(Запис збережено)")

if __name__ == "__main__":
    main()