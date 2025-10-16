def discriminant(a, b, c):
    return b**2 - 4*a*c

# Введення коефіцієнтів
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

# Обчислення дискримінанта
D = discriminant(a, b, c)

print("Дискримінант =", D)
