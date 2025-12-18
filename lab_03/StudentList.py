from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def find_insert_position(self, new_name):
        for index, student in enumerate(self.students):
            if new_name < student.name:
                return index
        return len(self.students)

    def add(self, student):
        pos = self.find_insert_position(student.name)
        self.students.insert(pos, student)
        print(f"Студента {student.name} додано.")

    def delete(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Студента {name} видалено.")
                return
        print("Такого студента немає.")

    def update(self, name, new_student_data):
        for i, student in enumerate(self.students):
            if student.name == name:

                del self.students[i]

                updated_name = new_student_data['name'] or student.name
                updated_phone = new_student_data['phone'] or student.phone
                updated_group = new_student_data['group'] or student.group
                updated_email = new_student_data['email'] or student.email
                
                new_student = Student(updated_name, updated_phone, updated_group, updated_email)

                self.add(new_student)
                print("Дані оновлено.")
                return
        print("Студента не знайдено.")

    def get_all(self):
        return self.students