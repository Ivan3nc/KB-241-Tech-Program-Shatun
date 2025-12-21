def get_safe_number(prompt):
    while True:
        user_input = input(prompt)

        if user_input == 'exit':
            return 'exit'
            
        try:
            val = float(user_input.replace(',', '.'))
            return val
        except ValueError:
            print("Помилка: введено текст замість числа! Спробуйте ще раз.")

if __name__ == "__main__":
    print("--- Тест функції введення ---")
    num = get_safe_number("Введіть будь-яке число: ")
    print(f"Ви успішно ввели: {num}")