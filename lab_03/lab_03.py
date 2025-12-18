import sys
from Student import Student
from StudentList import StudentList
from Utils import FileManager

DEFAULT_FILENAME = "../lab_02/lab2.csv"

def main():
    student_list = StudentList()

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = DEFAULT_FILENAME
    
    loaded_students = FileManager.load_from_file(file_name)

    for st in loaded_students:
        student_list.add(st)

    while True:
        choice = input("\nДія [C-create, U-update, D-delete, P-print, X-exit]: ").lower()
        
        if choice == "c":
            print("--- Додавання ---")
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            group = input("Група: ")
            email = input("Email: ")

            st = Student(name, phone, group, email)
            student_list.add(st)
            
        elif choice == "u":
            name = input("Кого редагуємо (ім'я): ")
            print("Введіть нові дані (Enter - залишити як є):")
            new_data = {
                'name': input("Нове ім'я: "),
                'phone': input("Новий телефон: "),
                'group': input("Нова група: "),
                'email': input("Новий email: ")
            }
            student_list.update(name, new_data)
            
        elif choice == "d":
            name = input("Кого видалити (ім'я): ")
            student_list.delete(name)
            
        elif choice == "p":
            print("--- Список студентів ---")
            for st in student_list.get_all():
                print(st) 
                
        elif choice == "x":
            FileManager.save_to_file(file_name, student_list.get_all())
            print("Вихід.")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()