import csv
import sys

student_list = []
# Ім'я файлу, яке буде використовуватись, якщо ми не вкажемо інше при запуску
DEFAULT_FILENAME = "lab2.csv"

#Завантажуємо дані з файлу при старті програми.
def load_from_file(file_name):
    global student_list
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            student_list = []
            for row in reader:
                student_list.append(row)
        print(f"Дані взяли з файлу '{file_name}'")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено. Починаємо з чистого аркуша.")
        student_list = []

#Записуємо всі дані назад у файл перед виходом
def save_to_file(file_name):
    try:
        with open(file_name, "w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "phone", "group", "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_list)
        print(f"Все збережено у '{file_name}'")
    except Exception as e:
        print(f"Щось пішло не так при збереженні: {e}")

#Пошук місця для студента в списку, щоб він завжди був відсортований за алфавітом
def find_insert_position(name):
    for index, item in enumerate(student_list):
        if name < item["name"]:
            return index
    return len(student_list)

#Додаємо нового студента в список
def add_new_element():
    print("--- Додавання студента ---")
    name = input("Ім'я: ")
    phone = input("Телефон: ")
    group = input("Група: ")
    email = input("Email: ")
    
    new_item = {"name": name, "phone": phone, "group": group, "email": email}

    pos = find_insert_position(name)
    student_list.insert(pos, new_item)
    print("Студента додано.")

# Шукаємо студента за ім'ям і видаляємо, якщо знайшли
def delete_element():
    name = input("Ім'я для видалення: ")
    for item in student_list:
        if name == item["name"]:
            student_list.remove(item)
            print("Видалено.")
            return
    print("Такого студента немає.")

# Видаляємо старий запис, а потім вставляємо оновлений
def update_element():
    name = input("Ім'я для оновлення: ")
    for i, item in enumerate(student_list):
        if name == item["name"]:
            print(f"Знайшли: {item}")
            
            del student_list[i]
            
            new_name = input(f"Нове ім'я [{item['name']}]: ") or item['name']
            new_phone = input(f"Новий телефон [{item['phone']}]: ") or item['phone']
            new_group = input(f"Нова група [{item['group']}]: ") or item['group']
            new_email = input(f"Новий email [{item['email']}]: ") or item['email']
            
            updated_item = {"name": new_name, "phone": new_phone, "group": new_group, "email": new_email}

            pos = find_insert_position(new_name)
            student_list.insert(pos, updated_item)
            print("Оновлено.")
            return
    print("Не знайдено.")

# Виводимо список всіх студентів на екран
def print_all_list():
    print("--- Список студентів ---")
    for s in student_list:
        print(f"Name: {s['name']}, Phone: {s['phone']}, Group: {s['group']}, Email: {s['email']}")
# Головна функція
def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = DEFAULT_FILENAME
    load_from_file(file_name)

    while True:
        choice = input("\nДія [C-create, U-update, D-delete, P-print, X-exit]: ").lower()
        if choice == "c":
            add_new_element()
        elif choice == "u":
            update_element()
        elif choice == "d":
            delete_element()
        elif choice == "p":
            print_all_list()
        elif choice == "x":
            save_to_file(file_name)
            print("Вихід.")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()