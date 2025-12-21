students = [
    {"name": "Oleg", "grade": 85},
    {"name": "Anna", "grade": 92},
    {"name": "Dmytro", "grade": 60},
    {"name": "Yulia", "grade": 95},
    {"name": "Borys", "grade": 74}
]

print("--- Початковий список ---")
print(students)

sorted_by_name = sorted(students, key=lambda x: x['name'])

print("\n--- Сортування за ім'ям (A-Z) ---")
for s in sorted_by_name:
    print(s)

sorted_by_grade = sorted(students, key=lambda x: x['grade'])

print("\n--- Сортування за оцінкою (зростання) ---")
for s in sorted_by_grade:
    print(s)