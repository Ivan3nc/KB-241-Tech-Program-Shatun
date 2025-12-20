def get_insert_pos(arr, el):
    for i, val in enumerate(arr):
        if el < val:
            return i
    return len(arr)

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    print("Початковий список:", nums)
    print("Напишіть 'exit' щоб вийти.")

    while True:
        user_input = input("\nЯке число вставити? ")
        
        if user_input == 'exit':
            break

        try:
            val = float(user_input.replace(',', '.'))
            pos = get_insert_pos(nums, val)
            print(f"Число {val} стане на індекс {pos}")
            nums.insert(pos, val)
            print("Список після вставки:", nums)

        except ValueError:
            print("Будь ласка, введіть число.")