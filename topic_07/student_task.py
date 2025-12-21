class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

if __name__ == "__main__":
    print("--- Створення об'єктів ---")
    group = [
        Student("Ivan", 20),
        Student("Maria", 19),
        Student("Petro", 22),
        Student("Oksana", 18)
    ]

    print("\n--- До сортування ---")
    for s in group:
        print(s)

    sorted_group = sorted(group, key=lambda student: student.age)

    print("\n--- Після сортування (за віком) ---")
    for s in sorted_group:
        print(s)