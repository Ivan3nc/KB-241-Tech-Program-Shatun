import csv
from student import Student

class Utils:
    @staticmethod
    def load_from_file(filename, student_list):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    st = Student(row["name"], row["phone"], row["group"], row["email"])
                    student_list.add(st)
            print("Дані завантажено.")
        except FileNotFoundError:
            print("Файл не знайдено, створено новий список.")

    @staticmethod
    def save_to_file(filename, student_list):
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "group", "email"])
            writer.writeheader()
            for st in student_list.students:
                writer.writerow(st.__dict__) # __dict__ автоматично перетворює об'єкт у словник
        print("Дані збережено.")