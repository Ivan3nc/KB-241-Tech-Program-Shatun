import sys
import os
from student import Student
from student_list import StudentList
from utils import Utils

# Ця функція робить введення даних простим і зручним
def get_input(prompt, old_value=""):
    val = input(f"{prompt} [{old_value}]: ")
    return val if val else old_value

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = sys.argv[1] if len(sys.argv) > 1 else os.path.join(script_dir, "lab3.csv")
    
    sl = StudentList()
    Utils.load_from_file(file_name, sl)

    while True:
        choice = input("\n[C]reate, [U]pdate, [D]elete, [P]rint, [X]it: ").lower()

        if choice == "c":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            grp = input("Група: ")
            email = input("Email: ")
            sl.add(Student(name, phone, grp, email))

        elif choice == "u":
            name = input("Кого оновлюємо (ім'я): ")
            old_st = sl.get_by_name(name)
            if old_st:
                new_name = get_input("Нове ім'я", old_st.name)
                new_phone = get_input("Новий телефон", old_st.phone)
                new_grp = get_input("Нова група", old_st.group)
                new_email = get_input("Новий email", old_st.email)
                sl.update(name, Student(new_name, new_phone, new_grp, new_email))
            else:
                print("Студента не знайдено.")

        elif choice == "d":
            name = input("Ім'я для видалення: ")
            sl.delete(name)

        elif choice == "p":
            for st in sl.students:
                print(st)

        elif choice == "x":
            Utils.save_to_file(file_name, sl)
            break

if __name__ == "__main__":
    main()