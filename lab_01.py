# lab_01.py
# Лабораторна робота №1. Списки. Словники. Кортежі.
# Реалізація відсортованого телефонного довідника студентів групи.

students = [
    {"name": "Bob", "phone": "0631234567", "group": "KB-241", "email": "bob@gmail.com"},
    {"name": "Emma", "phone": "0632345678", "group": "KB-241", "email": "emma@gmail.com"},
    {"name": "Jon", "phone": "0633456789", "group": "KB-241", "email": "jon@gmail.com"},
    {"name": "Zak", "phone": "0634567890", "group": "KB-241", "email": "zak@gmail.com"}
]


def printAllList():
    for s in students:
        print(f"Ім'я: {s['name']}, Телефон: {s['phone']}, Група: {s['group']}, Email: {s['email']}")
    print()


def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон: ")
    group = input("Введіть групу: ")
    email = input("Введіть email: ")
    newItem = {"name": name, "phone": phone, "group": group, "email": email}
    pos = 0
    for item in students:
        if name > item["name"]:
            pos += 1
        else:
            break

    students.insert(pos, newItem)
    print("Студента додано.\n")


def deleteElement():
    name = input("Введіть ім'я студента для видалення: ")
    index = -1
    for item in students:
        if name == item["name"]:
            index = students.index(item)
            break
    if index == -1:
        print("Студента не знайдено.\n")
    else:
        del students[index]
        print("Студента видалено.\n")


def updateElement():
    name = input("Введіть ім'я студента, дані якого потрібно змінити: ")
    found = None
    for item in students:
        if name == item["name"]:
            found = item
            break
    if not found:
        print("Студента не знайдено.\n")
        return

    print(f"Поточні дані: {found}")
    new_name = input(f"Нове ім'я [{found['name']}]: ") or found['name']
    new_phone = input(f"Новий телефон [{found['phone']}]: ") or found['phone']
    new_group = input(f"Нова група [{found['group']}]: ") or found['group']
    new_email = input(f"Новий email [{found['email']}]: ") or found['email']

    students.remove(found)

    updated = {
        "name": new_name,
        "phone": new_phone,
        "group": new_group,
        "email": new_email
    }

    pos = 0
    for item in students:
        if new_name > item["name"]:
            pos += 1
        else:
            break

    students.insert(pos, updated)
    print("Дані студента оновлено.\n")


def main():
    while True:
        choice = input("Оберіть дію [C - створити, U - оновити, D - видалити, P - показати, X - вийти]: ").lower()
        if choice == "c":
            addNewElement()
            printAllList()
        elif choice == "u":
            updateElement()
            printAllList()
        elif choice == "d":
            deleteElement()
            printAllList()
        elif choice == "p":
            printAllList()
        elif choice == "x":
            break
        else:
            print("Невірний вибір.\n")


if __name__ == "__main__":
    main()
