"""
Лабораторна робота №1. Списки. Словники.
"""

list_students = [
    {"name": "Bob", "phone": "0631234567", "group": "KB-241", "email": "bob@gmail.com"},
    {"name": "Emma", "phone": "0632345678", "group": "KB-241", "email": "emma@gmail.com"},
    {"name": "Jon", "phone": "0633456789", "group": "KB-241", "email": "jon@gmail.com"},
    {"name": "Zak", "phone": "0634567890", "group": "KB-241", "email": "zak@gmail.com"}
]
 
def findInsertPosition(name):
    for index, item in enumerate(list_students):
        if name < item["name"]:
            return index
    return len(list_students)

def findElementIndex(name):
    for index, item in enumerate(list_students):
        if name == item["name"]:
            return index
    return -1

def printAllList():
    print("\n--- Поточний список студентів ---")
    for elem in list_students:
        strForPrint = (f"Ім'я: {elem['name']}, Телефон: {elem['phone']}, "
                       f"Група: {elem['group']}, Email: {elem['email']}")
        print(strForPrint)
    print("---------------------------------\n")
    return
  
def addNewElement():
    print("--- Додавання нового студента ---")
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон: ")
    group = input("Введіть групу: ")
    email = input("Введіть email: ")
    newItem = {"name": name, "phone": phone, "group": group, "email": email}
    insertPosition = findInsertPosition(name)
    list_students.insert(insertPosition, newItem)
    print("Новий елемент успішно додано.\n")
    return

def deleteElement():
    print("--- Видалення студента ---")
    name = input("Введіть ім'я студента для видалення: ")
    deletePosition = findElementIndex(name)
    if deletePosition == -1:
        print("Елемент не знайдено.\n")
    else:
        del list_students[deletePosition]
        print(f"Елемент '{name}' видалено.\n")
    return

def updateElement():
    print("--- Оновлення даних студента ---")
    name = input("Введіть ім'я студента, якого потрібно змінити: ")
    index = findElementIndex(name)
    
    if index == -1:
        print("Елемент не знайдено.\n")
        return
    current_student = list_students[index]
    print(f"Знайдено: {current_student}")
    print("Введіть нові дані (натисніть Enter, щоб залишити поточне значення):")

    new_name = input(f"Нове ім'я [{current_student['name']}]: ") or current_student['name']
    new_phone = input(f"Новий телефон [{current_student['phone']}]: ") or current_student['phone']
    new_group = input(f"Нова група [{current_student['group']}]: ") or current_student['group']
    new_email = input(f"Новий email [{current_student['email']}]: ") or current_student['email']

    del list_students[index]

    updatedItem = {
        "name": new_name, 
        "phone": new_phone, 
        "group": new_group, 
        "email": new_email
    }

    insertPosition = findInsertPosition(new_name)
    list_students.insert(insertPosition, updatedItem)
    print("Дані оновлено успішно.\n")
    return

def main():
    while True:
        choice = input("Оберіть дію [C - create, U - update, D - delete, P - print, X - exit]: ")
        match choice.lower():
            case "c":
                addNewElement()
            case "u":
                updateElement()
            case "d":
                deleteElement()
            case "p":
                printAllList()
            case "x":
                print("Вихід з програми.")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.\n")

if __name__ == "__main__":
    main()