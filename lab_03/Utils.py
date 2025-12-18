import csv
from Student import Student

class FileManager:
    @staticmethod
    def load_from_file(filename):
        students = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    st = Student(row['name'], row['phone'], row['group'], row['email'])
                    students.append(st)
            print(f"Дані завантажено з '{filename}'")
        except FileNotFoundError:
            print(f"Файл '{filename}' не знайдено. Створено новий список.")
        return students

    @staticmethod
    def save_to_file(filename, students):
        try:
            with open(filename, "w", newline='', encoding="utf-8") as csvfile:
                fieldnames = ["name", "phone", "group", "email"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for st in students:
                    writer.writerow({
                        "name": st.name, 
                        "phone": st.phone, 
                        "group": st.group, 
                        "email": st.email
                    })
            print(f"Дані збережено у '{filename}'")
        except Exception as e:
            print(f"Помилка запису: {e}")