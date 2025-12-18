class StudentList:
    def __init__(self):
        self.students = []

    def find_index(self, name):
        # Допоміжна функція пошуку (сортування)
        for i, st in enumerate(self.students):
            if name < st.name:
                return i
        return len(self.students)

    def add(self, student):
        pos = self.find_index(student.name)
        self.students.insert(pos, student)
        print("Додано.")

    def delete(self, name):
        for st in self.students:
            if st.name == name:
                self.students.remove(st)
                print("Видалено.")
                return
        print("Не знайдено.")

    def update(self, name, new_student):
        for i, st in enumerate(self.students):
            if st.name == name:
                del self.students[i]
                self.add(new_student)
                print("Оновлено.")
                return
        print("Не знайдено.")
    
    # Додатковий метод, щоб знайти студента для редагування (щоб показати старі дані)
    def get_by_name(self, name):
        for st in self.students:
            if st.name == name:
                return st
        return None